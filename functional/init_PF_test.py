"""Initialize test environment & context and upgrade SUT.

Configuration file for this test is ``data/qed_env.yml``.
"""
import pytest

from qe_common import *

logger = init_logger()

# Common framwork variables initialization
global env
env = load_config_file(get_config_file_cmdarg('--env'))
# PathFider authority configuration
global pf_auth
pf_auth = load_auth_file(get_config_file_cmdarg('--auth'))


# Make this code load, even when allure fixture is not present
# This will not work across multiple tests nor for tests requiring prior context
if 'allure' not in dir(pytest):
    import __main__ as main
    import qe_modules.PathFinder as PF
    import qe_modules.PathFinderEdge as PFE
    init_allure()
    global context
    context = init_context()
    context.env = env
    context.config.pf_auth = pf_auth
    context.status.PF_Clean_Upgrade = False
    context.status.PFE_Clean_Upgrade = False
    context.PF = PF
    context.PFE = PFE
    # __builtins__['context'] = copy.copy(context)
    __builtins__['context'] = context


def setup_module(module):
    """Test setup example."""
    logger.info('\n\nTest setup.')


def teardown_module(module):
    """Test tear-down example."""
    logger.info('\n\nTest tear-down.')


# Forcing order=0 for initial test environment setup only.
# Other tests should not be use this method for ordering the tests.
# I.e., other tests must be able to run independently and in varying order.
@pytest.mark.run(order=0)
@pytest.allure.feature('Test Setup')
@pytest.allure.story('Load configuration files')
@pytest.mark.init
def test_init(context):
    """Load test configuration files (YAML)."""
    global env, pf_auth
    context.env = env
    context.config.pf_auth = pf_auth
    context.pf = context.PF.PathFinder(
        host=env.QED_Name,
        JWT_alg=pf_auth.JWT_alg,
        JWT_Header=pf_auth.JWT_Header,
        JWT_mac=pf_auth.JWT_mac,
        JWT_iss=pf_auth.JWT_iss,
        JWT_sub=pf_auth.JWT_sub,
        JWT_aud=pf_auth.JWT_aud,
        JWT_qedp=pf_auth.JWT_qedp,
        JWT_exp=pf_auth.JWT_exp
    )
    context.status.PF_Clean_Upgrade = False
    context.status.PFE_Clean_Upgrade = False
    # __builtins__['context'] = copy.copy(context)
    __builtins__['context'] = context


# TODO(perfromance): upgrade SUTs in parallel
@pytest.mark.run(order=0)
@pytest.mark.upgrade
@pytest.allure.feature('Test Setup')
@pytest.allure.story('Upgrade PFEs')
@pytest.mark.parametrize("PFE_IP, PFE_Name", env.PFE_IPs)
def test_upgrade_PFEs(PFE_IP, PFE_Name, context):
    """Upgrade PFEs in the SUT."""
    # global pf, cl
    pfe_upgrader = context.PFE.PathFinderEdge(
        PFE_Hudson=env.PFE_Hudson,
        PFE_Branch=env.PFE_Branch,
        PFE_Type=env.PFE_Type,
        PFE_Installation_Name=env.PFE_Installation_Name)
    pfe_version = pfe_upgrader.get_latest_successful_build()
    with pytest.allure.step('Upgrade PFE {} ({}) with {} '.format(
            PFE_IP, PFE_Name, pfe_version[1])):
        context.PFE.version = pfe_upgrader.upgrade_PFE(PFE_IP)
        context.status.PFE_Clean_Upgrade = True


# @pytest.mark.usefixtures("context")  # Not required - fixture is called below.
@pytest.mark.run(order=0)
@pytest.mark.upgrade
@pytest.allure.feature('Test Setup')
@pytest.allure.story('Upgrade PathFinder')
def test_upgrade_PathFinder(context):
    """Upgrade PF in the SUT."""
    # global pf, cl
    pf_upgrader = context.PF.PathFinderSUT(
        PF_Hudson=env.PF_Hudson, PF_Branch=env.PF_Branch, PF_Type=env.PF_Type)
    pf_version = pf_upgrader.get_latest_successful_build()
    with pytest.allure.step('Upgrade PF {} ({}) with {} '.format(
            env.QED, env.QED_Name, pf_version[1])):
        context.PF.version = pf_upgrader.upgrade_PF(env.QED)
        context.status.PF_Clean_Upgrade = True


@pytest.mark.run(order=0)
@pytest.allure.issue('QED-1903')
@pytest.allure.issue('QED-1909')
# @pytest.allure.link('https://jira.qumu.com/browse/QED-1903')
# @pytest.allure.link('https://jira.qumu.com/browse/QED-1909')
@pytest.mark.init
@pytest.allure.feature('Test Setup')
@pytest.allure.story('Get PathFinder schema')
def test_get_PathFinder_schema(context,
                               host=env.QED_Name,
                               patchFile=env.pfSchemaPatch):
    """Get latest PF schema from SUT.

    Update schema per patch file, if specified.
    """
    context.cl = context.pf.get_schema_objects(host=host, patchFile=patchFile)
    context.sc = context.pf.schema
    for key in context.pf.spec['definitions'].keys():
        globals()[key] = context.cl.get_model(key)
    return context.cl


# Interactive shell support.
# This code is not required in other test scripts.
def init_interactive_sa():
    """Get all object definitions from schema to be used in an interactive shell."""
    global context, env, pf_auth
    context.pf = context.PF.PathFinder(
        host=env.QED_Name,
        JWT_alg=pf_auth.JWT_alg,
        JWT_Header=pf_auth.JWT_Header,
        JWT_mac=pf_auth.JWT_mac,
        JWT_iss=pf_auth.JWT_iss,
        JWT_sub=pf_auth.JWT_sub,
        JWT_aud=pf_auth.JWT_aud,
        JWT_qedp=pf_auth.JWT_qedp,
        JWT_exp=pf_auth.JWT_exp
    )
    context.pf.cl = context.pf.get_schema_objects(
        host=env.QED_Name, patchFile=env.pfSchemaPatch)
    context.cl = context.pf.cl  # same links as in pytest run
    context.sc = context.pf.schema
    for key in context.pf.spec['definitions'].keys():
        globals()[key] = context.cl.get_model(key)


def init_interactive(context):
    """Get all object definitions from schema to be used in an interactive shell."""
    if hasattr(main, '__file__'):  # i.e., whe are in a shell
        context.pf = context.PF.PathFinder(
            host=env.QED_Name,
            JWT_alg=pf_auth.JWT_alg,
            JWT_Header=pf_auth.JWT_Header,
            JWT_mac=pf_auth.JWT_mac,
            JWT_iss=pf_auth.JWT_iss,
            JWT_sub=pf_auth.JWT_sub,
            JWT_aud=pf_auth.JWT_aud,
            JWT_qedp=pf_auth.JWT_qedp,
            JWT_exp=pf_auth.JWT_exp
        )
        context.pf.cl = context.pf.get_schema_objects(
            host=env.QED_Name, patchFile=env.pfSchemaPatch)
        context.cl = context.pf.cl  # same links as in pytest run
        context.sc = context.pf.schema
        for key in context.pf.spec['definitions'].keys():
            globals()[key] = context.cl.get_model(key)


if 'main' in dir():  # we may be in an interactive shell
    init_interactive(context)
elif 'get_ipython' in dir():
    init_interactive_sa()


@pytest.mark.run(order=0)
@pytest.mark.version
@pytest.mark.init
@pytest.allure.feature('Test Setup')
@pytest.allure.story('Record PF version details')
def test_get_PF_version_and_system_details(context):
    """Get version info and system details from QED server."""
    buildInfo = check(
        context.cl.System.getBuildInfo()
    )
    settings = check(
        context.cl.Settings.getSettings()
    )
    systemProperties = check(
        context.cl.System.getSystemProperties()
    )
    systemInfo = check(
        context.cl.System.getSystemInfo()
    )
    versionInfo = '\n--- PathFinder SUT version:\n\n'
    versionInfo += 'Build Version: {}\n'.format(buildInfo.buildVersion)
    versionInfo += 'git Branch: {}\n'.format(buildInfo.gitBranch)
    versionInfo += 'Patch: {}\n'.format(buildInfo.patch)
    versionInfo += 'Build JDK: {}\n'.format(buildInfo.buildJdk)
    versionInfo += '\n--- PathFinder SUT settings and status:\n\n'
    versionInfo += 'configured: {}\n'.format(settings.configured)
    versionInfo += 'sslPort: {}\n'.format(settings.sslPort)
    versionInfo += 'java.version: {}\n'.format(
        systemProperties['java.version'])
    versionInfo += 'Uptime: {}\n'.format(systemInfo['Uptime'])
    if not context.PF.version:
        context.PF.version = buildInfo
    if settings.configured is False or settings.configured == "False":
        # System seems to be not configured
        context.status.PF_Clean_Upgrade = True
    with pytest.allure.step(versionInfo):
        logger.info(versionInfo)
