# -*- coding: UTF-8 -*-

"""PFE Component Tests - Network_Locations.

* TC-45623 - Network_Locations GET:

  Verify that user with Match Any permission is unable to fetch list of Matching Audiences/Clients/Network Locations using Get method.


Equivalent test CURL command:

  curl -k -H "Host: <client_host>" -H "Authorization: Bearer
       <valid_token>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations"

Same, with test data:

  curl -k -H "Host: <client_host>" -H "Authorization: Bearer
       <valid_token>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Network_Locations')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Network_Locations test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-45623')
    @pytest.mark.Network_Locations
    @pytest.mark.GET
    def test_TC_45623_GET_Network_Locations_Net_Location(self, context):
        """TC-45623 - Network_Locations-GET
           Verify that user with Match Any permission is unable to fetch list of Matching Audiences/Clients/Network Locations using Get method."""
        # Define a test step
        with pytest.allure.step("""Verify that user with Match Any permission is unable to fetch list of Matching Audiences/Clients/Network Locations using Get method."""):

            ### Positive test example

            # listEntities the Network_Locations.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Network_Locations.listEntities()
            )

        with pytest.allure.step("""Verify that user with Match Any permission is unable to fetch list of Matching Audiences/Clients/Network Locations using Get method."""):

            ### Negative test example

            # listEntities the Network_Locations, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Network_Locations.listEntities(),
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
