# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-44382 - Groups DELETE:

  Verify that error message is displayed on providing non existing 'Id' in 'id' parameter using request DELETE /groups{id}.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups/deleteNonExist"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups/deleteNonExist"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Groups')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Groups test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44382')
    @pytest.mark.Groups
    @pytest.mark.DELETE
    def test_TC_44382_DELETE_Groups_Non_Exist_Id(self, context):
        """TC-44382 - Groups-DELETE
           Verify that error message is displayed on providing non existing 'Id' in 'id' parameter using request DELETE /groups{id}."""
        # Define a test step
        with pytest.allure.step("""Verify that error message is displayed on providing non existing 'Id' in 'id' parameter using request DELETE /groups{id}."""):

            # deleteEntity the Groups, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Groups.deleteEntity(
                        id='nonexisting'
                    ),
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden, HTTPNotFound) as e:        # 400, 403, 404 error
                get_error_message(e) | expect.any(
                    should.start_with('Delivery Service entity not found')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
