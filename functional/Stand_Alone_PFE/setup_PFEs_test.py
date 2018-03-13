"""Common PathFinderEdge configuration setup.

* create PFE profile
* create stand-alone PFE(s)
* register stand-alone PFE(s)
* clear PFEs alerts
* create stand-alone delivery system(s)
* create stand-alone audience(s)
"""

import pytest

from qe_common import *


logger = init_logger()

# Common framwork variables initialization
global env
env = load_config_file(get_config_file_cmdarg())
global test_config
test_config = load_config_file('setup_PFEs.yml', os.path.dirname(__file__))

# Make this code load, even when allure fixture is not present
# This will not work across multiple tests nor for tests requiring prior context
if 'allure' not in dir(pytest):
    from qe_common import init_allure, init_context
    import qe_modules.PathFinder as PF
    import qe_modules.PathFinderEdge as PFE
    init_allure()
    global context
    context = init_context()
    context.env = env
    context.status.PF_Clean_Upgrade = False
    context.status.PFE_Clean_Upgrade = False
    context.PF = PF
    context.PFE = PFE
    context.pf = PF.PathFinder(env.QED_Name)


faker = Factory.create(env.Locale)


@pytest.mark.run(order=2)
@pytest.mark.init
@pytest.allure.story('Check if PathFinder in configured')
@pytest.allure.feature('Setup PathFinder SUT')
def test_get_PFE_configured_state(context):
    """Check if PFEs are configured already or not."""
    pfe_profiles = len(
        check(
            context.cl.Pathfinder_Edge_Device_Profiles.listEntities(),
            quiet=True)
    )
    pfe_devices = len(check(
        context.cl.Pathfinder_Edge_Device.listEntities(),
        quiet=True))
    if pfe_profiles == 0 or pfe_devices == 0:
        context.status.PF_Clean_Upgrade = True
    else:
        context.status.PF_Clean_Upgrade = False


@pytest.mark.run(order=2)
@pytest.mark.init
@pytest.allure.story('PathFinderEdge common configuration')
@pytest.allure.feature('Setup PathFinder SUT')
class Test_Setup_StandAlonePFE(object):
    """PFE stand-alone test cases common setup."""

    @pytest.mark.config
    @pytest.mark.parametrize("PFE_IP, PFE_Name", env.PFE_IPs, ids=baseName)
    def test_global_variables_parametrized(self, PFE_IP, PFE_Name, context):
        """Parametrized globals to be used by later tests."""
        with pytest.allure.step("Create PFE `{}` test data.".format(PFE_Name)):
            context.status['PFEs'][PFE_IP] = Box()
            context.status['PFEs'][PFE_IP]['broadcasts'] = OrderedDict()
            context.status['PFEs'][PFE_IP]['audiences'] = OrderedDict()
            context.status['PFEs'][PFE_IP]['distributions'] = OrderedDict()

    @pytest.mark.config
    def test_create_PFE_profile(self, context):
        """Create Video Edge Profile.

        name = "Profile1"
        id = "pfeprofile1"
        """
        # Create a place in context.status for storing PFE Profiles
        name = "Profile1"
        id = "pfeprofile1"
        if 'PFEprofiles' not in context.status:
            context.status.PFEprofiles = Box()
        videoEdgeHTTPService = context.sc.VideoEdgeHTTPServiceDetails(
            serviceActive=True,
            protocol=test_config.videoEdgeHTTPService.protocol,
            # vodPublishingPoints=[]
            httpPort=80,
            httpsPort=443,)
        context.status.PFEprofiles[id] = context.sc.VideoEdgeDevicePropertyDetails(
            name=name,
            id=id,
            description="Profile 1 description",
            proxyMode=test_config.videoEdgeDeviceProperty.proxyMode,
            enableTokenAuthentication=test_config.videoEdgeDeviceProperty.enableTokenAuthentication,
            restrictedBandwidthStart=test_config.videoEdgeDeviceProperty.restrictedBandwidthStart,
            restrictedBandwidthEnd=test_config.videoEdgeDeviceProperty.restrictedBandwidthEnd,
            restrictedPeriodDownloadBandwidth=test_config.videoEdgeDeviceProperty.restrictedPeriodDownloadBandwidth,
            nonRestrictedPeriodDownloadBandwidth=test_config.videoEdgeDeviceProperty.nonRestrictedPeriodDownloadBandwidth,
            enablePrepositioning=test_config.videoEdgeDeviceProperty.enablePrepositioning,
            maximumDownloadTime=test_config.videoEdgeDeviceProperty.maximumDownloadTime,
            manifestRequestFrequency=test_config.videoEdgeDeviceProperty.manifestRequestFrequency,
            httpService=videoEdgeHTTPService,
            visibleInAllConfigurations=True,
            configurations=[context.status.globals.configId])
        if context.status.PF_Clean_Upgrade:
            check(context.cl.Pathfinder_Edge_Device_Profiles.createEntity(
                body=context.status.PFEprofiles[id]))

    @pytest.mark.config
    @pytest.mark.parametrize("PFE_IP, PFE_Name", env.PFE_IPs, ids=baseName)
    def test_create_stand_alone_PFE(self, PFE_IP, PFE_Name, context):
        """Create Stand-Alone PFE."""
        logger.info("\nCreating stand-alone PFE: " + PFE_IP)
        # testEnv['PFEs'] = Box()
        # context.status['PFEs'][PFE_IP] = Box()
        context.status['PFEs'][PFE_IP].videoEdgeDevice = context.sc.VideoEdgeDeviceDetails(
            id=PFE_Name,
            name=PFE_Name,
            description="Test PFE {}.".format(PFE_IP),
            tag="Test tag",
            deviceHost=PFE_IP,
            streamingHost=PFE_IP,
            multicastHost=PFE_IP,
            deviceProfileId="pfeprofile1",
            edgeDeviceRoles=test_config.videoEdgeDevice.edgeDeviceRoles.to_list(),
            visibleInAllConfigurations=False,
            configAdminCanEdit=True,
            configurations=[context.status.globals.configId],
            overrideProfileProperties=True,
            deactivateReflectorService=False)
        if context.status.PF_Clean_Upgrade:
            check(context.cl.Pathfinder_Edge_Device.createEntity(
                body=context.status['PFEs'][PFE_IP].videoEdgeDevice))

    @pytest.mark.config
    @pytest.mark.parametrize("PFE_IP, PFE_Name", env.PFE_IPs, ids=baseName)
    def test_register_PFE(self, PFE_IP, PFE_Name, context):
        """Register PFE with PF."""
        # Get registration code
        if context.status.PF_Clean_Upgrade:
            regToken = check(context.cl.Pathfinder_Edge_Device.getRegistrationToken(
                id=PFE_Name))
            logger.info("\nPFE registration token: {} ".format(regToken.token))
            context.status['PFEs'][PFE_IP].token = regToken.token
            # Register PFE
            PFE_registar = context.PFE.PathFinderEdge(
                PFE_Hudson=env.PFE_Hudson,
                PFE_Branch=env.PFE_Branch,
                PFE_Type=env.PFE_Type,
                PFE_Installation_Name=env.PFE_Installation_Name)
            PFE_registar.register_PFE(
                env.QED_Name, PFE_IP, regToken.token,
                env.PFE_Auth.user, env.PFE_Auth.password)

    @pytest.mark.parametrize("PFE_IP, PFE_Name", env.PFE_IPs, ids=baseName)
    def test_clear_PFE_alerts(self, PFE_IP, PFE_Name, context):
        """Clear alerts on PFEs created."""
        logger.info("\nClearing alerts for PFE: " + PFE_IP)
        time.sleep(3)  # Wait for alerts from PFE to start
        check(context.cl.Pathfinder_Edge_Device.deleteEntities(
            id=PFE_Name))

    @pytest.mark.parametrize("PFE_IP, PFE_Name", env.PFE_IPs, ids=baseName)
    def test_create_stand_alone_delivery_system(self, PFE_IP, PFE_Name, context):
        """Create Stand-Alone PFE delivery system."""
        logger.info("\nCreating stand-alone delivery system for PFE: " + PFE_IP)
        context.status['PFEs'][PFE_IP].deliverySystem = context.sc.DeliverySystemDetails(
            id="videoedge-{}".format(PFE_Name),
            name="VideoEdge Delivery System {}".format(PFE_Name),
            deliverySystemType="videoedge",
            deliverySystemRoles=test_config.deliverySystem.deliverySystemRoles.to_list(),
            configurations=[context.status.globals.configId],
            settings={"deviceId": PFE_Name},
            visibleInAllConfigurations=False,
            configAdminCanEdit=True,
        )
        if context.status.PF_Clean_Upgrade:
            check(context.cl.Delivery_Systems.createDeliveryOption(
                body=context.status['PFEs'][PFE_IP].deliverySystem))

    @pytest.mark.parametrize("PFE_IP, PFE_Name", env.PFE_IPs, ids=baseName)
    def test_create_stand_alone_PFE_audience(self, context,  # broadcastTests,
                                             PFE_IP, PFE_Name,
                                             AudienceId=None):
        """Create Stand-Alone PFE audience.

        This test is generating an AudienceId, if not available in context.data
        and is not assigned in the function call.
        This is done to make this function re-usable for other tests & frameworks,
        and should not be the normal use case.
        """
        logger.info("\nCreating stand-alone delivery system for PFE: " + PFE_IP)

        # Create AudienceId, if we don't have one already
        if AudienceId is None:
            if 'broadcasts' not in context.data:
                context.data.broadcasts = Box()
            if PFE_IP not in context.data.broadcasts:
                context.data.broadcasts[PFE_IP] = Box()
            if 'AudienceIds' not in context.data.broadcasts[PFE_IP]:
                context.data.broadcasts[PFE_IP]['AudienceIds'] = list()
            if len(context.data.broadcasts[PFE_IP]['AudienceIds']) == 0:
                AudienceId = "audiencevne-{}".format(PFE_Name)
                context.data.broadcasts[PFE_IP]['AudienceIds'].append(AudienceId)
            else:
                AudienceId = context.data.broadcasts[PFE_IP]['AudienceIds'][-1]  # Latest on the list
        else:
            context.data.broadcasts[PFE_IP]['AudienceIds'].append(AudienceId)

        # Create AudienceDetails schema object, and store it in the test status
        context.status['PFEs'][PFE_IP]['audiences'][AudienceId] = context.sc.AudienceDetails(
            id=AudienceId,
            name="VideoEdge Audience {}".format(PFE_Name),
            deliverySystems=[{"id": "videoedge-{}".format(PFE_Name)}],
            configurationId=context.status.globals.configId,
            # Optional AudienceDetails fields not used in this test:
            # clients=[{"id": "test"}],
            # networkLocations=[{"id": "test"}],
            # estimatedTimeForMulticastStreamsToBeAvailable=0,
        )
        # We need to create the Audience only on a newly configured system
        if context.status.PF_Clean_Upgrade:
            check(context.cl.Audiences.createEntity(
                body=context.status['PFEs'][PFE_IP]['audiences'][AudienceId]))
