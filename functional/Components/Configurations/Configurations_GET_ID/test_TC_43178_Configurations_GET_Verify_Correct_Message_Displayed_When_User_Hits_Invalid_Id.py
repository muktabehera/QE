# -*- coding: UTF-8 -*-

"""PFE Component Tests - Configurations.

* TC-43178 - Configurations GET:

  Verify that correct error message is displayed for wrong ID using request GET "/configurations/{id}".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/configurations/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/configurations/POST_GETID"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Configurations')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Configurations test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43178')
    @pytest.mark.Configurations
    @pytest.mark.GET
    def test_TC_43178_GET_Configurations_Verify_Correct_Message_Displayed_When_User_Hits_Invalid_Id(self, context):
        """TC-43178 - Configurations-GET
           Verify that correct error message is displayed for wrong ID using request GET "/configurations/{id}"."""
        # Define a test step
        with pytest.allure.step("""Verify that correct error message is displayed for wrong ID using request GET "/configurations/{id}"."""):

            ### Positive test example

            # getEntity the Configurations.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Configurations.getEntity(
                    id='POST_GETID')
            )

        with pytest.allure.step("""Verify that correct error message is displayed for wrong ID using request GET "/configurations/{id}"."""):

            ### Negative test example

            # getEntity the Configurations, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Configurations.getEntity(
                        id='POST_GETID'),
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
