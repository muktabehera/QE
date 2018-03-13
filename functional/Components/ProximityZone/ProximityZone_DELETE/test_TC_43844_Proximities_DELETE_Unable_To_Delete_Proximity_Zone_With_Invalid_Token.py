# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-43844 - Proximity_Zones DELETE:

  Verify that user is unable to delete the Proximity Zone using request DELETE /proximities{id}  with invalid token.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer
       <data_ID1_under_test>" -X DELETE -H "Content-Type:
       application/json" "<PF_host>://<client_host>/proximities/bbb"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer
       eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJkZWZhdWx0Iiwic3ViIjoiYWRtaW5AMTcyLjMwLjIuMTQ5OjgwODAuY29tIiwiYXVkIjoicWVkOmRlZmF1bHQiLCJxZWRwIjpbInMiLCJjIiwiZyIsInAiLCJkIiwibSIsImEiXX0.uh1W0Hs2nemsjiRFRSiyiZgo4io5bUmmCSJqrjfjfehff"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/bbb"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Proximity_Zones')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Proximity_Zones test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43844')
    @pytest.mark.Proximity_Zones
    @pytest.mark.DELETE
    def test_TC_43844_DELETE_Proximity_Zones_Unable_To_Delete_Proximity_Zone_With_Invalid_Token(self, context):
        """TC-43844 - Proximity_Zones-DELETE
           Verify that user is unable to delete the Proximity Zone using request DELETE /proximities{id}  with invalid token."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to delete the Proximity Zone using request DELETE /proximities{id}  with invalid token."""):

             # deleteEntity the Proximity_Zones with Invalid token, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Proximity_Zones.deleteEntity(id='ProximityPost'),
                    token='invalid_token',
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        #403 error
                get_error_message(e) | expect.any(
                    should.contain('Invalid Authorization Token')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
