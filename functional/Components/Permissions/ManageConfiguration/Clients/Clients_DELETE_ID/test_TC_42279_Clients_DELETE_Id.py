# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-42279 - Clients DELETE:

  Verify that User is able to View, all the entities under Intelligent Content Routing menu, using token with "Manage Configuration" permission within the token expiration time.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/deleteClientPermission"

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42279')
    @pytest.mark.Clients
    @pytest.mark.DELETE
    def test_TC_42279_DELETE_Clients_Id(self, context):
        """TC-42279 - Clients-DELETE
           Verify that User is able to View, all the entities under Intelligent Content Routing menu, using token with "Manage Configuration" permission within the token expiration time."""
        # Define a test step
        with pytest.allure.step("""Verify that User is able to View, all the entities under Intelligent Content Routing menu, using token with "Manage Configuration" permission within the token expiration time."""):

            ### Positive test example

            # deleteEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Clients.deleteEntity(
                    id='deleteClientPermission')
            )

        with pytest.allure.step("""Verify that User is able to View, all the entities under Intelligent Content Routing menu, using token with "Manage Configuration" permission within the token expiration time."""):

            ### Negative test example

            # deleteEntity the Clients, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Clients.deleteEntity(
                        id='deleteClientPermission'),
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
