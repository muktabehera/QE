# -*- coding: UTF-8 -*-

"""PFE Component Tests - Authorization_Systems.

* TC-43342 - Authorization_Systems POST:

  Verify that user is able to create Authorization System having Mackey length of at least 32 characters with using request POST /authorizationSystems.


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
   'configurations': [],
   'grantablePermissions': ['manageSystem',
                            'matchAny',
                            'provision',
                            'match',
                            'distribute',
                            'generate',
                            'manageConfiguration'],
   'id': 'POST_authorizationSystem_ableToCreate_macKeyAtleaset32Characters',
   'macKey': '12345678901234567890123456789012',
   'name': 'POST_authorizationSystem_ableToCreate_macKeyAtleaset32Characters',
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Authorization_Systems')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Authorization_Systems test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43342')
    @pytest.mark.Authorization_Systems
    @pytest.mark.POST
    def test_TC_43342_POST_Authorization_Systems_Able_To_Create_Mac_Key_At_Least_32_Characters(self, context):
        """TC-43342 - Authorization_Systems-POST
           Verify that user is able to create Authorization System having Mackey length of at least 32 characters with using request POST /authorizationSystems."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create Authorization System having Mackey length of at least 32 characters with using request POST /authorizationSystems."""):

            # Test case configuration
            authorizationSystemDetails = context.sc.AuthorizationSystemDetails(
                configAdminCanEdit=True,
                configurations=[],
                grantablePermissions=[
                    'manageSystem', 'matchAny', 'provision', 'match', 'distribute',
                    'generate', 'manageConfiguration'
                ],
                id='POST_authorizationSystem_ableToCreate_macKeyAtleaset32Characters',
                macKey='12345678901234567890123456789012',
                name='POST_authorizationSystem_ableToCreate_macKeyAtleaset32Characters',
                visibleInAllConfigurations=True)


            # createEntity the Authorization_Systems.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Authorization_Systems.createEntity(
                    body=authorizationSystemDetails
                )
            )

