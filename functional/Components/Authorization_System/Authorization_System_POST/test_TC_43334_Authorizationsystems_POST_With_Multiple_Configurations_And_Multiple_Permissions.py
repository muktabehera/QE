# -*- coding: UTF-8 -*-

"""PFE Component Tests - Authorization_Systems.

* TC-43334 - Authorization_Systems POST:

  Verify that user is able to create Authorization System with multiple configurations and multiple permissions using request POST /authorizationSystems.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/authorizationSystems"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/authorizationSystems"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': True,
   'configurations': [{'host': '172.30.5.204', 'id': 'default'},
                      {'host': '172.30.5.205', 'id': 'QA_Test'}],
   'grantablePermissions': ['manageSystem',
                            'matchAny',
                            'provision',
                            'match',
                            'distribute',
                            'generate',
                            'manageConfiguration'],
   'id': 'POST_authorizationSystem_withMultipleConfigurationsAndMultiplePermissions',
   'macKey': '12345689713265487923156234497813265489712654897',
   'name': 'POST_authorizationSystem_withMultipleConfigurationsAndMultiplePermissions',
   'visibleInAllConfigurations': False}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Authorization_Systems')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Authorization_Systems test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43334')
    @pytest.mark.Authorization_Systems
    @pytest.mark.POST
    def test_TC_43334_POST_Authorization_Systems_With_Multiple_Configurations_And_Multiple_Permissions(self, context):
        """TC-43334 - Authorization_Systems-POST
           Verify that user is able to create Authorization System with multiple configurations and multiple permissions using request POST /authorizationSystems."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create Authorization System with multiple configurations and multiple permissions using request POST /authorizationSystems."""):

            # Test case configuration

            configurations = [context.status.globals.configId]
            authorizationSystemDetails = context.sc.AuthorizationSystemDetails(
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'default',
                    'host': 'automation-pf03.qumu.media'
                }, {
                    'id': 'QA_Test',
                    'host': 'automation-pf03b.qumu.media'
                }],
                grantablePermissions=[
                    'manageSystem', 'matchAny', 'provision', 'match', 'distribute',
                    'generate', 'manageConfiguration'
                ],
                id=
                'POST_authorizationSystem_withMultipleConfigurationsAndMultiplePermissions',
                macKey='12345689713265487923156234497813265489712654897',
                name=
                'POST_authorizationSystem_withMultipleConfigurationsAndMultiplePermissions',
                visibleInAllConfigurations=False)


            # createEntity the Authorization_Systems.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Authorization_Systems.createEntity(
                    body=authorizationSystemDetails
                )
            )

