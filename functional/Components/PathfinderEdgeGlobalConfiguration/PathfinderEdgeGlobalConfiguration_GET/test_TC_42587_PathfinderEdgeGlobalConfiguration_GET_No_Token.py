# -*- coding: UTF-8 -*-

"""PFE Component Tests - Pathfinder_Edge_Global_Configuration.

* TC-42587 - Pathfinder_Edge_Global_Configuration GET:

  Verify that user is not able to GET the details of VideoEdge Global configuration request /devices/veGlobalConfig  without token.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer abcwqe" -X GET
       -H "Content-Type: application/json"
       <PF_host>://<client_host>/devices/veGlobalConfig

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer abcwqe" -X GET
       -H "Content-Type: application/json"
       <PF_host>://<client_host>/devices/veGlobalConfig

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Pathfinder_Edge_Global_Configuration')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Pathfinder_Edge_Global_Configuration test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42587')
    @pytest.mark.Pathfinder_Edge_Global_Configuration
    @pytest.mark.GET
    def test_TC_42587_GET_Pathfinder_Edge_Global_Configuration_No_Token(self, context):
        """TC-42587 - Pathfinder_Edge_Global_Configuration-GET
           Verify that user is not able to GET the details of VideoEdge Global configuration request /devices/veGlobalConfig  without token."""
        # Define a test step
        with pytest.allure.step("""Verify that user is not able to GET the details of VideoEdge Global configuration request /devices/veGlobalConfig  without token."""):

            ### Positive test example

            # getGlobalConfig the Pathfinder_Edge_Global_Configuration.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Pathfinder_Edge_Global_Configuration.getGlobalConfig(),
                token='invalid_token'
            )

        with pytest.allure.step("""Verify that user is not able to GET the details of VideoEdge Global configuration request /devices/veGlobalConfig  without token."""):

            ### Negative test example

            # getGlobalConfig the Pathfinder_Edge_Global_Configuration, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Pathfinder_Edge_Global_Configuration.getGlobalConfig(),
                    token='invalid_token',
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
