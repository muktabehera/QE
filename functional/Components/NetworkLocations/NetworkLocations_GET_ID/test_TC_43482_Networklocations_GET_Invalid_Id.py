# -*- coding: UTF-8 -*-

"""PFE Component Tests - Network_Locations.

* TC-43482 - Network_Locations GET:

  Verify that error message is displayed on providing invalid value for 'id' parameter using request GET /networkLocation{id}.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations/invalid"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations/invalid"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Network_Locations')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Network_Locations test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43482')
    @pytest.mark.Network_Locations
    @pytest.mark.GET
    def test_TC_43482_GET_Network_Locations_Invalid_Id(self, context):
        """TC-43482 - Network_Locations-GET
           Verify that error message is displayed on providing invalid value for 'id' parameter using request GET /networkLocation{id}."""
        # Define a test step
        with pytest.allure.step("""Verify that error message is displayed on providing invalid value for 'id' parameter using request GET /networkLocation{id}."""):


            # getEntity the Network_Locations, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Network_Locations.getEntity(
                        id='invalid'
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
