# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-43849 - Proximity_Zones PATCH:

  Verify that user is unable to Modify  Proximity Zone using request PATCH /proximities{id} " with invalid token.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer
       <data_ID1_under_test>" -X PATCH -d @<JSON_data_file> -H "Content-
       Type: application/json"
       "<PF_host>://<client_host>/proximities/ProximityUpdate"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer
       eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJkZWZhdWx0Iiwic3ViIjoiYWRtaW5AMTcyLjMwLjIuMTQ5OjgwODAuY29tIiwiYXVkIjoicWVkOmRlZmF1bHQiLCJxZWRwIjpbInMiLCJjIiwiZyIsInAiLCJkIiwibSIsImEiXX0.uh1W0Hs2nemsjiRFRSiyiZgo4io5bUmmCSJqrjfjfehff"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/ProximityUpdate"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': False,
   'configurations': [],
   'name': 'ProximityUpdatedInvalid Token',
   'proximityDetails': [{'cidr': '0.0.0.0/0', 'metric': 1, 'notes': ''}],
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Proximity_Zones')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Proximity_Zones test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43849')
    @pytest.mark.Proximity_Zones
    @pytest.mark.PATCH
    def test_TC_43849_PATCH_Proximity_Zones_Unable_Modify_With_Invalid_Token(self, context):
        """TC-43849 - Proximity_Zones-PATCH
           Verify that user is unable to Modify  Proximity Zone using request PATCH /proximities{id} " with invalid token."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to Modify  Proximity Zone using request PATCH /proximities{id} " with invalid token."""):

            # Test case configuration
            proximityZoneDetails = context.sc.ProximityZoneDetails(
                configAdminCanEdit=False,
                configurations=[],
                id=None,
                name='ProximityUpdatedInvalid Token123',
                proximityDetails=[{
                    'cidr': '0.0.0.0/0',
                    'metric': 1,
                    'notes': ''
                }],
                visibleInAllConfigurations=True)


            # prepare the request, so we can modify it
            request = context.cl.Proximity_Zones.updateEntity(
                    id='ProximityPost1',
                    body=proximityZoneDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateEntity the Proximity_Zones, and check we got the error we expect
            try:
                client, response = check(
                    request, token = 'invalid_token',
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.contain('Invalid Authorization Token'),
                    should.start_with('must match \"([0-9]{1,3}\\.){3}[0-9]{1,3}\\/[0-9]{1,3}\"'),
                    should.start_with('Invalid configuration identifier')

                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
