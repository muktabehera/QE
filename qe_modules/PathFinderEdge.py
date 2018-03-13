"""PFE / VNE remote control, upgrade, and register"""
import logging
# import logging.handlers
from plumbum import ProcessExecutionError
from plumbum import SshMachine
import requests
from requests.auth import HTTPBasicAuth
from rpyc.utils.zerodeploy import DeployedServer
import time


global PFE_SUTs, PFE_Hudson, PFE_Branch, PFE_Type, PFE_Installation_Name

PFE_SUTs = {'172.30.4.229': 'ZL-PFE-03',
            '172.30.1.76': 'ZL-PFE-05',
            '172.30.1.77': 'ZL-PFE-04'}

PFE_Hudson = 'build2:8080'
PFE_Branch = 'VNEX_8.0'
PFE_Type = 'qumu-videonet-edge-centos'
PFE_Installation_Name = 'qumu-videonet-edge-centos.noarch'

# Set logging level:
# DEBUG will show also plumbum logs
# INFO for local DEBUG
# ERROR for production environment
DEBUG_LEVEL = logging.INFO  # 'CRITICAL', 'DEBUG', 'ERROR', 'FATAL', 'INFO'

# Logger configuration
logging.basicConfig(level=DEBUG_LEVEL)
logger = logging.getLogger(__name__)
# Uncomment for remote syslog:
# handler = logging.handlers.SysLogHandler(address=(helperServer, 514))
# logger.addHandler(handler)


class UpgradeError(Exception):
    """Upgrade error exception."""

    def __init__(self, sut):
        """SUT is the system under test failing to upgrade."""
        self.sut = sut

    def __str__(self):
        """Get failed SUT."""
        return repr(self.sut)


class PathFinderEdge(object):
    """Helper class to deal with PFE upgrades."""

    def __init__(self,
                 PFE_Hudson=PFE_Hudson,
                 PFE_Branch=PFE_Branch,
                 PFE_Type=PFE_Type,
                 PFE_Installation_Name=PFE_Installation_Name):
        """Sane default values."""
        self.PFE_Hudson = PFE_Hudson
        self.PFE_Branch = PFE_Branch
        self.PFE_Type = PFE_Type
        self.PFE_Installation_Name = PFE_Installation_Name
        # Extra time to wait for PFE service:
        self.PFE_ShutDown_Delay = 5  # seconds
        self.PFE_StartUp_Delay = 20  # seconds
        self.latestBuildNumber = None
        self.version = None

    def get_latest_successful_build(self):
        """Identify latest successful build on Jekins."""
        latestBuild = requests.get(
            'http://{}/hudson/job/{}/lastSuccessfulBuild/api/json'.format(
                self.PFE_Hudson, self.PFE_Branch)).json()
        logger.info('Latest PFE build: {}'.format(latestBuild['fullDisplayName']))
        self.latestBuildNumber = latestBuild['number']
        for artifact in latestBuild['artifacts']:
            if artifact['fileName'].startswith(PFE_Type) and 'veupgrade' not in artifact['fileName']:
                self.PFE_fileName = artifact['fileName']
                self.relativePath = artifact['relativePath']
                break
        self.PFE_download_path = 'http://{}/hudson/job/{}/lastSuccessfulBuild/artifact/{}'.format(
            self.PFE_Hudson, self.PFE_Branch, self.relativePath)
        logger.debug(self.PFE_download_path)
        self.version = ".".join([str(self.PFE_Branch), str(self.latestBuildNumber)])
        return self.latestBuildNumber, self.PFE_fileName, self.PFE_download_path

    def upgrade_PFE(self, PFE_IP):
        """Upgrade PFE to latest successful version."""
        if not self.latestBuildNumber:
            self.get_latest_successful_build()

        logger.info("Updating PFE at: " + PFE_IP)
        # Connect to remote PF server as user1
        # Requires destination to be set with SSH key
        pfe_u = SshMachine(PFE_IP, user="applianceadmin")
        server_u = DeployedServer(pfe_u)
        # conn_u = server_u.classic_connect()

        # Access remote commands
        # require update to /etc/sudoers:
        # applianceadmin   ALL=(ALL:ALL) NOPASSWD: ALL
        pfe_sudo = pfe_u["sudo"]
        pfe_systemctl = pfe_u["systemctl"]
        pfe_yum = pfe_u["yum"]
        pfe_rpm = pfe_u["rpm"]
        pfe_curl = pfe_u["curl"]
        pfe_ps = pfe_u["ps"]
        pfe_grep = pfe_u["grep"]
        pfe_wc = pfe_u["wc"]
        pfe_rm = pfe_u["rm"]

        def pfe_process_up():
            """Check if PFE process is running."""
            try:
                c = int((pfe_ps['xfaw'] | pfe_grep['kodiak'] | pfe_wc['-l'])())
                return c > 2
            except ProcessExecutionError:
                return False

        # Stop PF
        logger.info("Stop PFE: " + pfe_sudo[pfe_systemctl["stop", "vne.service"]]())
        time.sleep(self.PFE_ShutDown_Delay)
        if pfe_process_up():
            logger.critical("Failed to stop PFE process at {} ".format(PFE_IP))
            raise UpgradeError("Failed to stop PFE process at {} ".format(PFE_IP))

        # Download latest successful build
        logger.info("Delete old downloads: " +
                    pfe_rm['-rf', '/tmp/{}'.format(self.PFE_Type)]())
        logger.info("Download latest PFE build: " +
                    pfe_curl['-o', '/tmp/{}'.format(self.PFE_fileName), self.PFE_download_path]())
        # TODO(): Check download was successful
        # Uninstall previous PFE version
        logger.info("Uninstall previous version: " +
                    pfe_sudo[pfe_yum['-y', 'remove', self.PFE_Installation_Name]]())
        # Install new version
        logger.info("Install PFE build #{}: ".format(self.latestBuildNumber) +
                    pfe_sudo[pfe_rpm['-i', '/tmp/{}'.format(self.PFE_fileName)]]())

        # Start PF and wait
        logger.info("Start PFE:" + pfe_sudo[pfe_systemctl["start", "vne.service"]]())
        time.sleep(self.PFE_StartUp_Delay)
        if not pfe_process_up():
            time.sleep(self.PFE_StartUp_Delay)
            if not pfe_process_up():
                logger.critical("Failed to start PFE process at {} ".format(PFE_IP))
                raise UpgradeError("Failed to start PFE process at {} ".format(PFE_IP))

        # Clean-up
        server_u.close()
        logger.info("Done.\n")
        return self.version

    def register_PFE(self, QED_Name, PFE_IP, regToken, PFE_user, PFE_password):
        """Register PFE device with PathFInder.

        * ``QED_Name`` - DNS / IP of the PathFidner Server.
        * ``PFE_IP`` - address of the PathFinderEndge to register.
        * ``regToken`` - token received from PathFinder for registering the PFE.
        * ``PFE_User`` & ``PFE_password`` - user credentials to the PFE.

        :param QED_Name: DNS / IP of the PathFidner Server.
        :type QED_Name: str.
        :param PFE_IP: address of the PathFinderEndge to register.
        :type PFE_IP: str.
        :param regToken: token received from PathFinder for registering the PFE.
        :type regToken: str.
        :param PFE_User: user credentials to the PFE.
        :type PFE_User: str.
        :param PFE_password: user credentials to the PFE.
        :type PFE_password: str.
        :returns: bool -- registration response status (.ok).
        :raises: UpgradeError

        """
        regData = dict()
        regData["controllerUrl"] = "http://{}".format(QED_Name)
        regData["deviceAddress"] = PFE_IP
        regData["token"] = regToken
        # testEnv['PFEs'][PFE_IP].token = regToken.token
        regHeaders = dict()
        regHeaders['Accept'] = 'application/json'
        regHeaders['Content-Type'] = 'application/json'
        reg_session = requests.Session()
        reg_req = requests.Request('OPTIONS',
                                   'http://{}/admin/registration'.format(
                                       PFE_IP),
                                   auth=HTTPBasicAuth(PFE_user, PFE_password))
        reg_prepped = reg_session.prepare_request(reg_req)
        resp = reg_session.send(reg_prepped)
        logger.debug("PFE registration OPTIONS: ({}) {} ".format(
            resp.status_code, resp.headers))
        reg_req2 = requests.Request('POST',
                                    'http://{}/admin/registration'.format(
                                        PFE_IP),
                                    json=regData,
                                    headers=regHeaders,
                                    auth=HTTPBasicAuth(PFE_user, PFE_password))
        reg_prepped2 = reg_session.prepare_request(reg_req2)
        reg_resp2 = reg_session.send(reg_prepped2)
        logger.debug("PFE registration POST: ({}) {} ".format(
            reg_resp2.status_code, reg_resp2.text))
        if not reg_resp2.json()['success'] or not reg_resp2.ok:
            logger.critical(
                '\nFailed to register PFE {} with PF: {} {}'.format(
                    PFE_IP, reg_resp2.status_code, reg_resp2.text))
            raise UpgradeError(PFE_IP)
        else:
            logger.info('\nRegistered PFE {} successfuly.'.format(PFE_IP))
        return reg_resp2.ok


if __name__ == '__main__':
    pfe = PathFinderEdge(PFE_Hudson=PFE_Hudson,
                         PFE_Branch=PFE_Branch,
                         PFE_Type=PFE_Type,
                         PFE_Installation_Name=PFE_Installation_Name)
    for pfe_sut in PFE_SUTs.keys():
        pfe.upgrade_PFE(pfe_sut)
