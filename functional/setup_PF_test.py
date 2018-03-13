"""Common PathFinder configuration setup.

* create configuration
* create authorization
* lock server
* create origin
* create PFE global configuration

Common configuration file is ``data/qed_env.yml``.
Additional configuration for this test is ``setup_PF.yml`` file.
"""

import pytest

from qe_common import *


logger = init_logger()

# Common framwork variables initialization
global env
env = load_config_file(get_config_file_cmdarg())
global test_config
test_config = load_config_file('setup_PF.yml', os.path.dirname(__file__))
global pf_auth
pf_auth = load_auth_file(get_config_file_cmdarg('--auth'))

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


@pytest.mark.run(order=1)
@pytest.mark.init
@pytest.allure.story('PathFinder common configuration')
@pytest.allure.feature('Setup PathFinder SUT')
# @pytest.mark.usefixtures("context")
class Test_StandAlonePFE(object):
    """PFE stand-alone test cases."""

    @pytest.mark.config
    def test_global_variables(self, context):
        """Globals to be used by later tests."""
        with pytest.allure.step("Create common PF test data."):
            context.status['globals'] = Box()
            context.status['globals']['configId'] = context.sc.IdContainer(
                id='default', host=env.QED_Name)
            context.status['globals']['tenantConfigId'] = context.sc.IdContainer(
                id='QA_Test', host=env.QED_Tenant_b)
            context.status['globals']['broadcasts'] = OrderedDict()
            context.status['PFEs'] = Box()

    @pytest.mark.config
    def test_create_configuration(self, context):
        """Create Configuration."""
        with pytest.allure.step("Create PathFinder configuration."):
            context.status.configuration = context.sc.ConfigurationDetails(
                host=env.QED_Name,
                id='default',
                configAdminCanCreate=True,
                configurationType='ON_PREMISE')
            if context.status.PF_Clean_Upgrade:
                check(context.cl.Configurations.createEntity(
                    body=context.status.configuration))

    def test_create_tenant_configuration(self, context):
        """Create 2nd tenant Configuration, for tests that require more than one configuration."""
        with pytest.allure.step("Create PathFinder configuration for 2nd tenant."):
            context.status.tenantConfiguration = context.sc.ConfigurationDetails(
                host=env.QED_Tenant_b,
                id='QA_Test',
                configAdminCanCreate=True,
                configurationType='ON_PREMISE')
            if context.status.PF_Clean_Upgrade:
                check(context.cl.Configurations.createEntity(
                    body=context.status.tenantConfiguration))

    @pytest.mark.config
    def test_create_authorization_system(self, context):
        """Create Authorization System."""
        with pytest.allure.step("Create PathFinder Authorization system."):
            context.status.authorizationSystem = context.sc.AuthorizationSystemDetails(
                id="default",
                name="Test Auth System",
                macKey=pf_auth.JWT_mac,
                grantablePermissions=[
                    "manageSystem", "manageConfiguration", "generate", "provision",
                    "distribute", "match", "matchAny"
                ],
                visibleInAllConfigurations=True,
                configAdminCanEdit=True,
                configurations=[context.status.globals.configId], )
            if context.status.PF_Clean_Upgrade:
                check(context.cl.Authorization_Systems.createEntity(
                    body=context.status.authorizationSystem))

    @pytest.mark.config
    def test_lock_the_server(self, context):
        """Lock server."""
        with pytest.allure.step("Lock PathFinder server."):
            if context.status.PF_Clean_Upgrade:
                settings = context.sc.SettingsDetails(configured=True)
                swag, response = check(context.cl.Settings.updateSettings(
                    body=settings), returnResponse=True)
                logger.info('System lock response:' + response.reason)

    @pytest.mark.config
    def test_create_origin(self, context):
        """Create Origin."""
        with pytest.allure.step("Create PathFinder origin."):
            originBase = context.sc.OriginBaseUri(
                uri='file://./content/origin/', roles=[u'common.filesystemfetch'])
            context.status.origin = context.sc.OriginDetails(
                id="Origin1",
                name="Sample Content Origin",
                baseUris=[originBase],
                visibleInAllConfigurations=False,
                configAdminCanEdit=True,
                configurations=[context.status.globals.configId])
            if context.status.PF_Clean_Upgrade:
                resp, soc = check(context.cl.Origins.createEntity(
                    body=context.status.origin), returnResponse=True)
                logger.info(resp)

    @pytest.mark.config
    def test_create_PFE_global_configuration(self, context):
        """Create PFE Edge Global Configuration."""
        with pytest.allure.step("Create PathFinderEdge global configuration."):
            context.status.videoEdgeGlobalConfig = context.sc.VideoEdgeGlobalConfigDetails(
                deliveryServiceHost=env.QED_Name,
                deliveryServiceProtocol=test_config.videoEdgeGlobalConfig.deliveryServiceProtocol,
                deliveryServicePort=test_config.videoEdgeGlobalConfig.deliveryServicePort,
                configRequestFrequency="10")
            if context.status.PF_Clean_Upgrade:
                check(context.cl.Pathfinder_Edge_Global_Configuration.updateEntity(
                    body=context.status.videoEdgeGlobalConfig))
