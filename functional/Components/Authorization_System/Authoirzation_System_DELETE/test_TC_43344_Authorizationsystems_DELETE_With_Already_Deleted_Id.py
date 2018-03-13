# -*- coding: UTF-8 -*-

"""PFE Component Tests - Authorization_Systems.

* TC-43344 - Authorization_Systems DELETE:

  Verify that error message is displayed on providing Authorization system ID which is already deleted using request DELETE authorizationSystems/{id}  .


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


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Authorization_Systems')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Authorization_Systems test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43344')
    @pytest.mark.Authorization_Systems
    @pytest.mark.DELETE
    def test_TC_43344_DELETE_Authorization_Systems_With_Already_Deleted_Id(self, context):
        """TC-43344 - Authorization_Systems-DELETE
           Verify that error message is displayed on providing Authorization system ID which is already deleted using request DELETE authorizationSystems/{id}  ."""
        # Define a test step

        with pytest.allure.step("""Verify that error message is displayed on providing Authorization system ID which is already deleted using request DELETE authorizationSystems/{id}  ."""):


            # deleteEntity the Authorization_Systems, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Authorization_Systems.deleteEntity(
                        id='Delete_authorizationSystem_testdata'),
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Delivery Service entity not found'),
                    should.contain('Delivery Service entity not found')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
