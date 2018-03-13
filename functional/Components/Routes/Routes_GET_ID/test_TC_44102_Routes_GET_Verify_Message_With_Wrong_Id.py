# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44102 - Routes GET:

  Verify that error message is displayed in the response body if user provides the wrong id using request GET "/routes/{id}".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/BSRoute1fsf"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/BSRoute1fsf"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Routes')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Routes test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44102')
    @pytest.mark.Routes
    @pytest.mark.GET
    def test_TC_44102_GET_Routes_Verify_Message_With_Wrong_Id(self, context):
        """TC-44102 - Routes-GET
           Verify that error message is displayed in the response body if user provides the wrong id using request GET "/routes/{id}"."""
        # Define a test step
        with pytest.allure.step("""Verify that error message is displayed in the response body if user provides the wrong id using request GET "/routes/{id}"."""):

            request= context.cl.Routes.getEntity(
                id='wrongid'
            )

            # listEntities the Routes, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden, HTTPNotFound) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Delivery Service entity not found'),
                    should.start_with('Invalid page parameter specified'),
                    should.contain('Invalid Authorization Token')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
