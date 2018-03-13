"""PathFinder sanity tests, to make sure it is up and running.

* Create temporary configuration with a random ID.
* Get the temporary configuration back.
* Delete the temporary configuration.
"""
import pytest

from qe_common import *

logger = init_logger()

# Common framwork variables initialization
global env
env = load_config_file(get_config_file_cmdarg())

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
    # context.interactive = True

# Used for generating random test data
faker = Factory.create(env.Locale)


@pytest.mark.run(order=2)    # we want tests to stop early on environment issue
@pytest.mark.sanity
@pytest.allure.feature('PF Sanity Test')
@pytest.allure.story('Sanity PF Test')
def test_PF_Sanity_create_and_delete_configuration(context):
    """PF sanity test - create, get, and delete configuration."""
    tmpId = faker.word() + str(faker.random_int())    # random configuration id
    config = context.pf.schema.ConfigurationDetails(
        host=env.QED_Name + str(faker.random_int()),  # to avoid resource conflict
        id=tmpId,
        configAdminCanCreate=True,
        configurationType='ON_PREMISE')
    with pytest.allure.step('Create temporary configuration, id="{}"'.format(tmpId)):
        check(context.cl.Configurations.createEntity(
            body=config))
    with pytest.allure.step('Get temporary configuration back by id'):
        check(context.cl.Configurations.getEntity(
            id=tmpId))
    with pytest.allure.step('Delete temporary configuration by id'):
        swag, response = check(context.cl.Configurations.deleteEntity(
            id=tmpId), returnResponse=True)
        logger.debug('Deleting response {}'.format(response.reason))
