# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-42999 - Clients DELETE:

  Verify that error message is displayed on providing invalid value for 'id' parameter using request DELETE /client{id}.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/invalid"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/invalid"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42999')
    @pytest.mark.Clients
    @pytest.mark.DELETE
    def test_TC_42999_DELETE_Clients_Invalid_Id(self, context):
        """TC-42999 - Clients-DELETE
           Verify that error message is displayed on providing invalid value for 'id' parameter using request DELETE /client{id}."""
        # Define a test step
        with pytest.allure.step("""Verify that error message is displayed on providing invalid value for 'id' parameter using request DELETE /client{id}."""):

            ### Positive test example

            # deleteEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Clients.deleteEntity()
            )

        with pytest.allure.step("""Verify that error message is displayed on providing invalid value for 'id' parameter using request DELETE /client{id}."""):

            ### Negative test example

            # deleteEntity the Clients, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Clients.deleteEntity(),
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
