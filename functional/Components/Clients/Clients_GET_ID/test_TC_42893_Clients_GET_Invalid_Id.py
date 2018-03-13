# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-42893 - Clients GET:

  Verify that error message is displayed on providing invalid value for 'id' parameter using request GET /client{id}.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/invalid"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/invalid"

"""

import pytest

from qe_common import *

logger = init_logger()



@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42893')
    @pytest.mark.Clients
    @pytest.mark.GET
    def test_TC_42893_GET_Clients_Invalid_Id(self, context):
        """TC-42893 - Clients-GET
           Verify that error message is displayed on providing invalid value for 'id' parameter using request GET /client{id}."""
        # Define a test step

        with pytest.allure.step("""Verify that error message is displayed on providing invalid value for 'id' parameter using request GET /client{id}."""):

            # getEntity the Clients, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Clients.getEntity(id='wrong'),
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
