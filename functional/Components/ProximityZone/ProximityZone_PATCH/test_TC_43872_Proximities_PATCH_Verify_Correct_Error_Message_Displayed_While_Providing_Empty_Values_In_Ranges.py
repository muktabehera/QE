# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-43872 - Proximity_Zones PATCH:

  Verify that correct error message should be displayed while  providing empty values in  'Ranges' for Proximity Zone using request PATCH /proximities{id} ".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/ProximityUpdate"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/ProximityUpdate"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': False,
   'configurations': [{'host': '172.30.2.149', 'id': 'default'}],
   'name': 'PromximityUpdatedWithInvalidRange',
   'proximityDetails': [],
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()







@pytest.mark.components
@pytest.allure.story('Proximity_Zones')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Proximity_Zones test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43872')
    @pytest.mark.Proximity_Zones
    @pytest.mark.PATCH
    def test_TC_43872_PATCH_Proximity_Zones_Verify_Correct_Error_Message_Displayed_While_Providing_Empty_Values_In_Ranges(self, context):
        """TC-43872 - Proximity_Zones-PATCH
           Verify that correct error message should be displayed while  providing empty values in  'Ranges' for Proximity Zone using request PATCH /proximities{id} "."""
        # Define a test step
        with pytest.allure.step("""Verify that correct error message should be displayed while  providing empty values in  'Ranges' for Proximity Zone using request PATCH /proximities{id} "."""):

            # Test case configuration
            proximityZoneDetails = context.sc.ProximityZoneDetails(
                configAdminCanEdit=False,
                configurations=[{
                    'id': 'default',
                    'host': '172.30.6.174'
                }],
                id=None,
                name='PromximityUpdatedWithInvalidRange',
                proximityDetails=[],
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
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('size must be between 1 and 2147483647'),
                    should.start_with('Invalid configuration identifier')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
