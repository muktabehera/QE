# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-45623 - Clients GET:

  Verify that user with Match Any permission is unable to fetch list of Matching Audiences/Clients/Network Locations using Get method.


Equivalent test CURL command:

  curl -k -H "Host: <client_host>" -H "Authorization: Bearer
       <valid_token>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

Same, with test data:

  curl -k -H "Host: <client_host>" -H "Authorization: Bearer
       <valid_token>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-45623')
    @pytest.mark.Clients
    @pytest.mark.GET
    def test_TC_45623_GET_Clients_Client(self, context):
        """TC-45623 - Clients-GET
           Verify that user with Match Any permission is unable to fetch list of Matching Audiences/Clients/Network Locations using Get method."""
        # Define a test step
        with pytest.allure.step("""Verify that user with Match Any permission is unable to fetch list of Matching Audiences/Clients/Network Locations using Get method."""):

            ### Positive test example

            # listEntities the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Clients.listEntities()
            )

        with pytest.allure.step("""Verify that user with Match Any permission is unable to fetch list of Matching Audiences/Clients/Network Locations using Get method."""):

            ### Negative test example

            # listEntities the Clients, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Clients.listEntities(),
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
