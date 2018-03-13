# -*- coding: UTF-8 -*-

"""PFE Component Tests - Pathfinder_Edge_Global_Configuration.

* TC-44141 - Pathfinder_Edge_Global_Configuration GET:

  Verify that user is able to GET the details of Browsers using GET /useragent/capabilities without providing any parameter.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       <PF_host>://<client_host>/devices/veGlobalConfig

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44141')
    @pytest.mark.Pathfinder_Edge_Global_Configuration
    @pytest.mark.GET
    def test_TC_44141_GET_Pathfinder_Edge_Global_Configuration_Capabilities(self, context):
        """TC-44141 - Pathfinder_Edge_Global_Configuration-GET
           Verify that user is able to GET the details of Browsers using GET /useragent/capabilities without providing any parameter."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of Browsers using GET /useragent/capabilities without providing any parameter."""):

            ### Positive test example

            # getGlobalConfig the Pathfinder_Edge_Global_Configuration.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Pathfinder_Edge_Global_Configuration.getGlobalConfig()
            )

        with pytest.allure.step("""Verify that user is able to GET the details of Browsers using GET /useragent/capabilities without providing any parameter."""):

            ### Negative test example

            # getGlobalConfig the Pathfinder_Edge_Global_Configuration, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Pathfinder_Edge_Global_Configuration.getGlobalConfig(),
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
