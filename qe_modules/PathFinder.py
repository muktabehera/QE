"""
.. module:: PathFinder

PathFinder module for handling remote control, upgrade, and RESTful API communication.

* ``Schema`` class is holding the Swagger schema retrieved from the PathFinder server, with potential patches to the schema.
* ``PathFinderSUT`` class is for hadnling PathFinder upgrades.
* ``PathFinder`` class wrapps the RESTful / Swagger API calls to the PathFinder server under test.

All objects are having sane defaults, to allow easy usage in San-Bruno lab environment.
This means that in SB lab, calling most functions should "just work" as-is,
but porper configuration variables should be applied elsewhere.
Please see below for more details.
"""
# from attrdict import AttrDict
from box import Box
from bravado.client import SwaggerClient
from bravado.exception import HTTPForbidden
from datetime import datetime
from datetime import timedelta
# from calendar import timegm
import json
import jwt
import logging
# import logging.handlers
from plumbum import ProcessExecutionError
from plumbum import SshMachine
import requests
from requests.auth import HTTPBasicAuth
from rpyc.utils.zerodeploy import DeployedServer
import time

from qe_common import *

global PF_SUT, PF_Hudson, PF_Branch, PF_Type

PF_SUT = '172.30.5.153'
PF_SUT_Name = 'automation-pf03.qumu.media'
PF_Hudson = 'build2:8080'
PF_Branch = 'DeliveryService_1.3'
PF_Type = 'qed-server'

# Set logging level:
# DEBUG will show also plumbum logs
# INFO for local debugging
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
        """Failed to upgrade SUT."""
        return repr(self.sut)


class PathFinderNotInitialized(Exception):
    """PathFinder exception for non-initialized class."""

    def __init__(self, sut):
        """PathFinder under test should be initialized (retreive schema from PF)."""
        self.sut = sut

    def __str__(self):
        """PathFinder under test should be initialized (retreive schema from PF)."""
        return repr(self.sut)


class PathFinderSUT(object):
    """Helper class to deal with PathFinder SUT (System Under Test) upgrades.

    Class is initialized with the PathFinder IP address (or DNS entry).
    """

    def __init__(self,
                 PF_Hudson=PF_Hudson,
                 PF_Branch=PF_Branch,
                 PF_Type=PF_Type):
        """Sane default values."""
        self.PF_Hudson = PF_Hudson
        self.PF_Branch = PF_Branch
        self.PF_Type = PF_Type
        # Extra time to wait for PF service:
        self.PF_ShutDown_Delay = 5  # seconds
        self.PF_StartUp_Delay = 30  # seconds
        self.latestBuildNumber = None
        self.version = None

    def get_latest_successful_build(self):
        """Identify latest successful build on Jenkins.

        Jenkins configuration is determined in *data/qed_env.yml*.
        """
        latestBuild = requests.get('http://{}/hudson/job/{}/lastSuccessfulBuild/api/json'.format(
            self.PF_Hudson, self.PF_Branch)).json()
        logger.info('Latest PF build: {} '.format(
            latestBuild['fullDisplayName']))
        self.latestBuildNumber = latestBuild['number']
        for artifact in latestBuild['artifacts']:
            if artifact['fileName'].startswith(self.PF_Type):
                self.PF_fileName = artifact['fileName']
                self.relativePath = artifact['relativePath']
                break
        self.PF_download_path = 'http://{}/hudson/job/{}/lastSuccessfulBuild/artifact/{}'.format(
            self.PF_Hudson, self.PF_Branch, self.relativePath)
        logger.debug(self.PF_download_path)
        self.version = ".".join(
            [str(self.PF_Branch), str(self.latestBuildNumber)])
        return self.latestBuildNumber, self.PF_fileName, self.PF_download_path

    def upgrade_PF(self, pfSUT):
        """Upgrade PFE to latest successful version/build.

        Jenkins configuration is determined in *data/qed_env.yml*.

        :param pfSUT: PathFinder IP or DNS name to upgrade.
        :type name: str.
        :raises: UpgradeError.

        """
        if not self.latestBuildNumber:
            self.get_latest_successful_build()

        # Connect to remote PF server as user1
        # Requires destination to be set with SSH key
        pf_u = SshMachine(pfSUT, user="user1")
        server_u = DeployedServer(pf_u)
        # conn_u = server_u.classic_connect()

        # Access remote commands
        # require update to /etc/sudoers:
        # %sudo   ALL=(ALL:ALL) NOPASSWD: ALL
        pf_sudo = pf_u["sudo"]
        pf_service = pf_u["service"]
        pf_mysql = pf_u["mysql"]
        # pfe_systemctl = pf_u["systemctl"]
        # pfe_yum = pf_u["yum"]
        # pfe_rpm = pf_u["rpm"]
        pf_curl = pf_u["curl"]
        pf_ps = pf_u["ps"]
        pf_grep = pf_u["grep"]
        pf_wc = pf_u["wc"]
        pf_rm = pf_u["rm"]
        pf_jar = pf_u['/usr/local/qed/jre/bin/jar']

        # Get latest PF code
        logger.info("Updating PF at: " + pfSUT)

        def pf_process_up():
            """Check if PathFinder process is running on the remote server."""
            try:
                c = int((pf_ps['xfaw'] | pf_grep['qed/server'] |
                         pf_grep['-v', 'grep'] | pf_wc['-l'])())
                return c >= 2
            except ProcessExecutionError:
                return False

        # Stop PF
        logger.info("Stopping PF service: " +
                    pf_sudo[pf_service["qed", "stop"]]())
        time.sleep(self.PF_ShutDown_Delay)
        if pf_process_up():
            logger.critical("Failed to stop PF process at {} ".format(pfSUT))
            raise UpgradeError(
                "Failed to stop PF process at {} ".format(PF_IP))
        logger.info(not(pf_process_up()))

        # Download latest successful build
        logger.info("Delete old downloads: " +
                    pf_rm['-rf', '/tmp/{}'.format(self.PF_Type)]())
        logger.info("Download latest PF build: " +
                    pf_curl['-o', '/tmp/{}'.format(self.PF_fileName), self.PF_download_path]())
        # TODO(): Check download was successful
        # Remove previous PF version
        with pf_u.cwd('/usr/local/qed/base/webapps/ROOT'):
            logger.info("Remove previous version: " +
                        pf_sudo[pf_rm['-rf', 'com', 'content', 'META-INF', 'WEB-INF']]())
        # Extract new PF version
        with pf_u.cwd('/usr/local/qed/base/webapps/ROOT'):
            logger.info("Extract PF build #{}:\n".format(self.latestBuildNumber) +
                        pf_sudo[pf_jar['-xvf', '/tmp/{}'.format(self.PF_fileName)]]())

        # mysql - drop and create PF database
        logger.info("Re-create PF database: ")
        logger.info("Available DBs before drop:\n" +
                    pf_mysql["--user=qed", "--password=qed", "-e show databases;"]())
        logger.debug(
            "Drop PF DB: " + pf_mysql["--user=qed", "--password=qed", "-e drop database qed;"]())
        logger.info("Available DBs after drop:\n" +
                    pf_mysql["--user=qed", "--password=qed", "-e show databases;"]())
        logger.debug("Create PF DB: " +
                     pf_mysql["--user=qed", "--password=qed", "-e create database qed;"]())
        logger.info("Available DBs after creating new:\n" +
                    pf_mysql["--user=qed", "--password=qed", "-e show databases;"]())

        # Start PF and wait
        logger.info("Starting PF service: " +
                    pf_sudo[pf_service["qed", "start"]]())
        time.sleep(self.PF_StartUp_Delay)
        if not pf_process_up():
            time.sleep(self.PF_StartUp_Delay)
            if not pf_process_up():
                logger.critical(
                    "Failed to start PF process at {} ".format(pfSUT))
                raise UpgradeError(
                    "Failed to start PF process at {} ".format(PF_IP))
        logger.info(pf_process_up())

        # Clean-up
        server_u.close()
        logger.info("Done.\n")
        return self.version


class PathFinder(object):
    """PathFinder Swagger client, with support for JWT authentication.

    *get_token* and *get_token_with_options* are provided as statuc methods,
    and do not require class instance.
    """

    request_options = {'also_return_response': True}
    empty_options = {}

    def __init__(
            self,
            host=None,
            JWT_alg=None,
            JWT_Header=None,
            JWT_mac=None,
            JWT_iss=None,
            JWT_sub=None,
            JWT_aud=None,
            JWT_qedp=None,
            JWT_exp=None):
        """Initialize PathFInder schema schema.

        ``host`` (string) -  PathFinder server IP or DNS entry. Use of IP is recommended.
        ``JWT_*`` (string) - PathFinder authorization configuration.
        """
        self.host = host
        self.schema = Box()
        self.pfLocked = False   # whetner PF auth was locked.
        # TODO(Keep last secure token, to save calculation)
        self.lastToken = None
        if JWT_mac is not None:
            self.JWT_alg = JWT_alg
            self.JWT_Header = JWT_Header
            self.JWT_mac = JWT_mac
            self.JWT_iss = JWT_iss
            self.JWT_sub = JWT_sub
            self.JWT_aud = JWT_aud
            self.JWT_qedp = JWT_qedp
            self.JWT_exp = JWT_exp
        return

    @staticmethod
    def get_secure_token(
            JWT_alg='HS256',
            JWT_Header='Bearer %s',
            JWT_mac='This_is_a_Test_QED_MAC_Key_Which_Needs_to_be_at_Least_32_Bytes_Long',
            JWT_iss='default',
            JWT_sub='admin@{}.com'.format(PF_SUT_Name),
            JWT_aud='qed:default',
            JWT_qedp=['s', 'c', 'g', 'p', 'd', 'm', 'a'],
            JWT_exp=None):
        """Generate JWT header token for communication with PathFinder API."""
        payload = dict()
        payload['iss'] = JWT_iss
        payload['sub'] = JWT_sub
        payload['aud'] = JWT_aud
        payload['qedp'] = JWT_qedp
        if JWT_exp:
            payload['exp'] = datetime.utcnow() + timedelta(int(JWT_exp))
        token = jwt.encode(payload, JWT_mac, JWT_alg)
        request_headers_name = 'Authorization'
        request_header_payload = JWT_Header % token.decode('ascii')
        request_headers = {
            "headers": {
                request_headers_name: request_header_payload
            }
        }
        request_headers["headers"].update({"Content-Type": "application/json"})
        # return request_headers_name, request_header_payload
        return request_headers

    @staticmethod
    def get_token_with_options(
            JWT_alg='HS256',
            JWT_Header='Bearer %s',
            JWT_mac='This_is_a_Test_QED_MAC_Key_Which_Needs_to_be_at_Least_32_Bytes_Long',
            JWT_iss='default',
            JWT_sub='admin@{}.com'.format(PF_SUT_Name),
            JWT_aud='qed:default',
            JWT_qedp=['s', 'c', 'g', 'p', 'd', 'm', 'a'],
            JWT_exp=None):
        """Combine Swagger client request options with JWT security options.

        This will result in swagger response tuple that contains both
        "regular" swagger response as well as the the
        undelying :mod:`requests` object.
        """
        jwt_request_header = PathFinder.get_secure_token(
            JWT_alg=JWT_alg,
            JWT_Header=JWT_Header,
            JWT_mac=JWT_mac,
            JWT_iss=JWT_iss,
            JWT_sub=JWT_sub,
            JWT_aud=JWT_aud,
            JWT_qedp=JWT_qedp,
            JWT_exp=JWT_exp
        )
        secure_request_options = PathFinder.request_options.copy()
        secure_request_options.update(jwt_request_header)
        return secure_request_options

    def get_token(
            self,
            secure=None,
            returnResponse=False,
            JWT_alg=None,
            JWT_Header=None,
            JWT_mac=None,
            JWT_iss=None,
            JWT_sub=None,
            JWT_aud=None,
            JWT_qedp=None,
            JWT_exp=None):
        """Generate token for communication with PathFinder API.

           By defauly this code will try to figure out if a secure token is required.
           Behavior can be tuned via:

           ``secure`` (~bool) - change to True or False to force secure/not-secure token.
                                by default, None, which translate to auto-detect.

           ``returnResponse`` (bool) - when True, return tuple of swagger response
                                       and :mod:`requests` object.
                                       Default is False, which returns only swagger response.

           ``JWT_*`` (string) - Update PathFinder authorization configuration.

        """
        if JWT_mac is None:
            if self.JWT_mac is None:
                raise PathFinderNotInitialized(self.host)
        else:
            self.JWT_alg = JWT_alg
            self.JWT_Header = JWT_Header
            self.JWT_mac = JWT_mac
            self.JWT_iss = JWT_iss
            self.JWT_sub = JWT_sub
            self.JWT_aud = JWT_aud
            self.JWT_qedp = JWT_qedp
            self.JWT_exp = JWT_exp
        if secure is None:
            """Check if PF is locked already or not."""
            settings = Box()
            settings.configured = None
            try:
                settings = self.cl.Settings.getSettings().result()
            except HTTPForbidden:
                settings = self.cl.Settings.getSettings(
                    _request_options=self.get_secure_token(
                        self.JWT_alg, self.JWT_Header, self.JWT_mac,
                        self.JWT_iss, self.JWT_sub, self.JWT_aud, self.JWT_qedp,
                        self.JWT_exp)
                ).result()
                self.pfLocked = True
            except AttributeError:
                raise PathFinderNotInitialized(self.host)
            except Exception:
                raise
            else:
                if settings.configured is True:
                    self.pfLocked = True
                elif settings.configured is False:
                    self.pfLocked = False
                else:
                    raise Exception(
                        "Unexpected Condition - cannot get settings from PF.")
            if self.pfLocked:
                secure = True
            else:
                secure = False
        if secure is True:
            if returnResponse:
                return self.get_token_with_options(
                    self.JWT_alg, self.JWT_Header, self.JWT_mac, self.JWT_iss,
                    self.JWT_sub, self.JWT_aud, self.JWT_qedp, self.JWT_exp)
            else:
                return self.get_secure_token(
                    self.JWT_alg, self.JWT_Header, self.JWT_mac, self.JWT_iss,
                    self.JWT_sub, self.JWT_aud, self.JWT_qedp, self.JWT_exp)
        elif secure is False:
            if returnResponse:
                return PathFinder.request_options
            else:
                return PathFinder.empty_options

    def get_PathFinder_schema(self, host=None, patchFile=None):
        """Get latest PF schema from SUT.

        Update schema per patch file, if specified.
        """
        if not host and self.host is not None:
            host = self.host
        self.spec = requests.get(
            'http://{}/services/apidocs/qed.json'.format(host)).json()
        self.spec["host"] = host
        self.spec["basePath"] = "/"
        if patchFile:
            try:
                patchFS = open(patchFile)
            except IOError:     # search parent folder for patch file, for Sphinx
                patchFS = open(os.path.join('..', patchFile))
            except Exception:
                raise
            specPatch = json.load(patchFS)
            patchFS.close()
            del(patchFS)
            for key in specPatch.keys():
                for subKey in specPatch[key]:
                    self.spec[key][subKey] = specPatch[key][subKey][0]
            # Jira QED-1903 work-around
            self.spec['definitions']['BroadcastCreate'][
                'required'].remove('sourceGroups')
            self.spec['definitions']['BroadcastCreate'][
                'required'].remove('streamGroups')
            self.spec['definitions']['BroadcastCreate']['required'].remove('streams')
            self.spec['definitions']['BroadcastCreate']['required'].remove('tags')
            # Jira QED-1909 work-around
            self.spec['definitions']['DistributionFileDetails'][
                'required'].remove('streamMetadata')
            # Jira QED-1938 work-around
            self.spec['definitions']['ExpressionDetails']['properties']['matchValue']['type'] = "string"
            # Jira QED-1939 work-around
            self.spec['paths']['/proximities/{id}']['delete']['responses']['default'] = {
                'description': 'successful operation'}
            # JIRA QED-1972 work-around
            self.spec['paths']['/clients/systemClients']['get']['operationId'] = 'listSystemEntities'
        # Create swagger client
        self.cl = SwaggerClient.from_spec(
            self.spec,
            config={
                'validate_swagger_spec': False,
                'validate_requests': False,
                'validate_responses': False,
                'also_return_response': False
            }, )
        return self.cl

    def get_schema_objects(self, host=None, patchFile=None):
        """Get all object definitions from schema.

        Calls self.get_PathFinder_schema, and then
        Returns a swagger client.
        Keeps schema in class instance method .schema.
        """
        if not host and self.host is not None:
            host = self.host
        self.cl = self.get_PathFinder_schema(host, patchFile)
        for key in self.spec['definitions'].keys():
            self.schema[key] = self.cl.get_model(key)
        return self.cl

    def print_schema_tree(self, host=None, patchFile=None):
        """Print schema tree structure, showing call methods vs schema path."""
        if not host and self.host is not None:
            host = self.host
        if 'cl' not in dir(self):
            print('Error: get_schema_objects first')
        elif not self.cl:
            print('Error: get_schema_objects first')
        else:
            for m in dir(self.cl):
                print(m)
                cm = getattr(self.cl, m)
                for r in dir(cm):
                    obj = ''
                    doc = getattr(cm, r).__doc__
                    for d in doc.splitlines():
                        if ':type body:' in d:
                            obj = d.split('/definitions/')[1]
                    print('\t{:40}- {:6}\t{:36}\t{}'.format(
                        r,
                        getattr(cm, r).operation.http_method,
                        obj,
                        getattr(cm, r).operation.path_name
                    ))


if __name__ == '__main__':
    pf = PathFinder(PF_Hudson=PF_Hudson,
                    PF_Branch=PF_Branch,
                    PF_Type=PF_Type)
    pf.upgrade_PF(PF_SUT)
