# -*- coding: UTF-8 -*-

"""PFE Component Tests - Authorization_Systems.

* TC-43295 - Authorization_Systems POST:

  Verify that able to create  Authorization System with same Name but with Unique ID value using request POST /authorizationSystems.


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
   'grantablePermissions': ['manageSystem', 'generate', 'manageConfiguration'],
   'id': 'POST_authorizationSystem_createWithDuplicateName_uniqueID',
   'macKey': '12345689713265487923156497813265489712654897',
   'name': 'POST_authorizationSystem_correctMessage_forSameIdValue',
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Authorization_Systems')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Authorization_Systems test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43295')
    @pytest.mark.Authorization_Systems
    @pytest.mark.POST
    def test_TC_43295_POST_Authorization_Systems_Create_With_Duplicate_Name_Unique_Id(self, context):
        """TC-43295 - Authorization_Systems-POST
           Verify that able to create  Authorization System with same Name but with Unique ID value using request POST /authorizationSystems."""
        # Define a test step
        with pytest.allure.step("""Verify that able to create  Authorization System with same Name but with Unique ID value using request POST /authorizationSystems."""):

            # Test case configuration
            authorizationSystemDetails = context.sc.AuthorizationSystemDetails(
                configAdminCanEdit=True,
                configurations=[],
                grantablePermissions=['manageSystem', 'generate', 'manageConfiguration'],
                id='POST_authorizationSystem_createWithDuplicateName_uniqueID',
                macKey='12345689713265487923156497813265489712654897',
                name='POST_authorizationSystem_correctMessage_forSameIdValue',
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
