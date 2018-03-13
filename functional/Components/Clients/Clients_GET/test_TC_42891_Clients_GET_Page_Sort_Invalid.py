# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-42891 - Clients GET:

  Verify that error message is displayed on providing invalid value for page,sort parameter using request GET /clients.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients?page=pagee &sort=sortt"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients?page=pagee &sort=sortt"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42891')
    @pytest.mark.Clients
    @pytest.mark.GET
    def test_TC_42891_GET_Clients_Page_Sort_Invalid(self, context):
        """TC-42891 - Clients-GET
           Verify that error message is displayed on providing invalid value for page,sort parameter using request GET /clients."""
        # Define a test step

        with pytest.allure.step("""Verify that error message is displayed on providing invalid value for page,sort parameter using request GET /clients."""):


            # listEntities the Clients, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Clients.listEntities(
                        page='pagee', 
                        sort='sortt'
                    ),
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Invalid page parameter specified. No seperator')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
