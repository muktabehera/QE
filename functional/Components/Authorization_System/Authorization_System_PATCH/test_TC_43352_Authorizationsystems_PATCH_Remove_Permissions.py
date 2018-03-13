# -*- coding: UTF-8 -*-

"""PFE Component Tests - Authorization_Systems.

* TC-43352 - Authorization_Systems PATCH:

  Verify that user is able to update [Remove Permissions] for Authorization System using request PATCH authorizationSystems/{id}  ".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/authorizationSystems/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/authorizationSystems/PATCH_authorizationSystem_testdata"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': True,
   'configurations': [],
   'creationDate': '2016-04-21T07:00:16Z',
   'grantablePermissions': ['manageConfiguration', 'matchAny'],
   'modificationDate': '2016-04-21T07:00:16Z',
   'name': 'PATCH_authorizationSystem_removePermissions',
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Authorization_Systems')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Authorization_Systems test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43352')
    @pytest.mark.Authorization_Systems
    @pytest.mark.PATCH
    def test_TC_43352_PATCH_Authorization_Systems_Remove_Permissions(self, context):
        """TC-43352 - Authorization_Systems-PATCH
           Verify that user is able to update [Remove Permissions] for Authorization System using request PATCH authorizationSystems/{id}  "."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to update [Remove Permissions] for Authorization System using request PATCH authorizationSystems/{id}  "."""):


            # Test case configuration
            authorizationSystemDetails = context.sc.AuthorizationSystemDetails(
                configAdminCanEdit=True,
                configurations=[],
                grantablePermissions=['manageConfiguration', 'matchAny'],
                id=None,
                macKey=None,
                name='PATCH_authorizationSystem_removePermissions',
                visibleInAllConfigurations=True)


            # updateEntity the Authorization_Systems.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Authorization_Systems.updateEntity(
                    body=authorizationSystemDetails, 
                    id='PATCH_authorizationSystem_testdata'
                
                )
            )

