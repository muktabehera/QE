# -*- coding: UTF-8 -*-

"""PFE Component Tests - Configurations.

* TC-43191 - Configurations DELETE:

  Verify that correct message is displayed on providing if user hit the request DELETE "/configurations/{id}" with invalid token.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/configurations/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/configurations/POST_DELETE"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Configurations')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Configurations test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43191')
    @pytest.mark.Configurations
    @pytest.mark.DELETE
    def test_TC_43191_DELETE_Configurations_Verify_Correct_Message_Is_Displayed_With_Invalid_Token(self, context):
        """TC-43191 - Configurations-DELETE
           Verify that correct message is displayed on providing if user hit the request DELETE "/configurations/{id}" with invalid token."""
        # Define a test step
        with pytest.allure.step("""Verify that correct message is displayed on providing if user hit the request DELETE "/configurations/{id}" with invalid token."""):

            ### Positive test example

            # deleteEntity the Configurations.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Configurations.deleteEntity(
                    id='POST_DELETE')
            )

        with pytest.allure.step("""Verify that correct message is displayed on providing if user hit the request DELETE "/configurations/{id}" with invalid token."""):

            ### Negative test example

            # deleteEntity the Configurations, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Configurations.deleteEntity(
                        id='POST_DELETE'),
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
