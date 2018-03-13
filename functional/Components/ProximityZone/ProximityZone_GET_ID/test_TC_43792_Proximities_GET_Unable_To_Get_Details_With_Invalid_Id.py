# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-43792 - Proximity_Zones GET:

  Verify that user is unable to GET the details of  proximities using request /proximities/{id} using wrong/deleted/invalid ID.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/a12345bcd123"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/a12345bcd123"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Proximity_Zones')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Proximity_Zones test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43792')
    @pytest.mark.Proximity_Zones
    @pytest.mark.GET
    def test_TC_43792_GET_Proximity_Zones_Unable_To_Get_Details_With_Invalid_Id(self, context):
        """TC-43792 - Proximity_Zones-GET
           Verify that user is unable to GET the details of  proximities using request /proximities/{id} using wrong/deleted/invalid ID."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to GET the details of  proximities using request /proximities/{id} using wrong/deleted/invalid ID."""):

            # listEntities the Proximity_Zones with invalid Id, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Proximity_Zones.getEntity(id='ProximityPost'),
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 404 error
                get_error_message(e) | expect.any(
                    should.start_with('Delivery Service entity not found')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
