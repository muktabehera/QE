# -*- coding: UTF-8 -*-

"""PFE Component Tests - Broadcasts.

* TC-44478 - Broadcasts DELETE:

  Verify that error message is displayed on providing invalid id using request DELETE "/broadcasts/{id}".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/broadcasts/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/broadcasts/Broadcast_DeleteByID"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Broadcasts')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Broadcasts test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44478')
    @pytest.mark.Broadcasts
    @pytest.mark.DELETE
    def test_TC_44478_DELETE_Broadcasts_Error_Message_Is_Displayed_While_Providing_Invalid_Id(self, context):
        """TC-44478 - Broadcasts-DELETE
           Verify that error message is displayed on providing invalid id using request DELETE "/broadcasts/{id}"."""
        # Define a test step
        with pytest.allure.step("""Verify that error message is displayed on providing invalid id using request DELETE "/broadcasts/{id}"."""):

            ### Positive test example

            # deleteEntity the Broadcasts.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Broadcasts.deleteEntity(
                    id='Broadcast_DeleteByID')
            )

        with pytest.allure.step("""Verify that error message is displayed on providing invalid id using request DELETE "/broadcasts/{id}"."""):

            ### Negative test example

            # deleteEntity the Broadcasts, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Broadcasts.deleteEntity(
                        id='Broadcast_DeleteByID'),
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('may not be empty'),
                    should.start_with('Invalid page parameter specified'),
                    should.contain('Invalid Authorization Token')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
