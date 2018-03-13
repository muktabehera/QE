# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44048 - Routes GET:

  Verify that correct error message is displayed for invalid value of "page" and "sort" parameter using request "routes".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes?page=sdfsdfsd &sort=sdfsdfsd
       &showAll=false"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes?page=sdfsdfsd &sort=sdfsdfsd
       &showAll=false"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Routes')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Routes test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44048')
    @pytest.mark.Routes
    @pytest.mark.GET
    def test_TC_44048_GET_Routes_Correct_Message_Displayed_For_Invalid_Value_Of_Page_And_Sort(self, context):
        """TC-44048 - Routes-GET
           Verify that correct error message is displayed for invalid value of "page" and "sort" parameter using request "routes"."""
        # Define a test step
        with pytest.allure.step("""Verify that correct error message is displayed for invalid value of "page" and "sort" parameter using request "routes"."""):

            # createHop the Routes, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Routes.listAllRoutes(
                        page='sdfsdfsd', 
                        sort='sdfsdfsd', 
                        showAll='false'
                    ),
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Invalid page parameter specified')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
