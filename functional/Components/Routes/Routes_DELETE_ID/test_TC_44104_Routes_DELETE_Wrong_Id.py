# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44104 - Routes DELETE:

  Verify that error message is displayed in the response body if user provides the wrong id using request DELETE "/routes/{id}".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/dbnskdn"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/dbnskdn"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Routes')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Routes test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44104')
    @pytest.mark.Routes
    @pytest.mark.DELETE
    def test_TC_44104_DELETE_Routes_Wrong_Id(self, context):
        """TC-44104 - Routes-DELETE
           Verify that error message is displayed in the response body if user provides the wrong id using request DELETE "/routes/{id}"."""
        # Define a test step
        with pytest.allure.step("""Verify that error message is displayed in the response body if user provides the wrong id using request DELETE "/routes/{id}"."""):

            # createHop the Routes, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Routes.deleteEntity(
                        id='wrongid'
                    ),
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden, HTTPNotFound) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Delivery Service entity not found')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
