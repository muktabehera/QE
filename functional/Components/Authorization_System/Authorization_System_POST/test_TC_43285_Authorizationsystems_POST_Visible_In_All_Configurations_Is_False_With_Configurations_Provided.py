# -*- coding: UTF-8 -*-

"""PFE Component Tests - Authorization_Systems.

* TC-43285 - Authorization_Systems POST:

  Verify that user is able to create Authorization System with parameters  if "visibleInAllConfigurations"is set to false and configurations are selected using request POST /authorizationSystems.


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
   'configurations': [{'host': '172.30.5.204', 'id': 'default'}],
   'grantablePermissions': ['manageSystem', 'generate', 'manageConfiguration'],
   'id': 'POST_authorizationSystem_visibleInAllConfigurationsIsFalse_withConfigurationsProvided',
   'macKey': '1123456897813256498713254698713564987321654987314654',
   'name': 'POST_authorizationSystem_visibleInAllConfigurationsIsFalse_withConfigurationsProvided',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43285')
    @pytest.mark.Authorization_Systems
    @pytest.mark.POST
    def test_TC_43285_POST_Authorization_Systems_Visible_In_All_Configurations_Is_False_With_Configurations_Provided(self, context):
        """TC-43285 - Authorization_Systems-POST
           Verify that user is able to create Authorization System with parameters  if "visibleInAllConfigurations"is set to false and configurations are selected using request POST /authorizationSystems."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create Authorization System with parameters  if "visibleInAllConfigurations"is set to false and configurations are selected using request POST /authorizationSystems."""):

            # Test case configuration
            authorizationSystemDetails = context.sc.AuthorizationSystemDetails(
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'default',
                    'host': '172.30.5.204'
                }],
                grantablePermissions=['manageSystem', 'generate', 'manageConfiguration'],
                id=
                'POST_authorizationSystem_visibleInAllConfigurationsIsFalse_withConfigurationsProvided',
                macKey='1123456897813256498713254698713564987321654987314654',
                name=
                'POST_authorizationSystem_visibleInAllConfigurationsIsFalse_withConfigurationsProvided',
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
