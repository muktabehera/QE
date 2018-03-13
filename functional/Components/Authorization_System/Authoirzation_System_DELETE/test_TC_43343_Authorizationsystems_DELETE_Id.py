# -*- coding: UTF-8 -*-

"""PFE Component Tests - Authorization_Systems.

* TC-43343 - Authorization_Systems DELETE:

  Verify that user is able to delete the Authorization system using request DELETE authorizationSystems/{id}  with 'id' parameter.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/authorizationSystems/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/authorizationSystems/Delete_authorizationSystem_testdata"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Authorization_Systems')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Authorization_Systems test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43343')
    @pytest.mark.Authorization_Systems
    @pytest.mark.DELETE
    def test_TC_43343_DELETE_Authorization_Systems_Id(self, context):
        """TC-43343 - Authorization_Systems-DELETE
           Verify that user is able to delete the Authorization system using request DELETE authorizationSystems/{id}  with 'id' parameter."""
        # Define a test step
        with pytest.allure.step("""create Authorization system"""):


            # Test case configuration
            authorizationSystemDetails = context.sc.AuthorizationSystemDetails(
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'default',
                    'host': '172.30.5.204'
                }],
                grantablePermissions=[
                    'manageSystem', 'matchAny', 'provision', 'match', 'distribute',
                    'generate', 'manageConfiguration'
                ],
                id='Delete_authorizationSystem_testdata',
                macKey='1123456897813256498713254698713564987321654987314654',
                name='Delete_authorizationSystem_testdata',
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
        with pytest.allure.step("""Verify that user is able to delete the Authorization system using request DELETE authorizationSystems/{id}  with 'id' parameter."""):

            # deleteEntity the Authorization_Systems.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Authorization_Systems.deleteEntity(
                    id='Delete_authorizationSystem_testdata')
            )

