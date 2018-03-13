# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-43881 - Proximity_Zones PATCH:

  Verify that user is unable to Modify[Proximity Zone] on providing empty value for 'Metric' field using request PATCH /proximities{id} " .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/ProximityUpdate"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/ProximityUpdate"

JSON data sent to PathFinder in this test:

  {
    "visibleInAllConfigurations": true,
    "configAdminCanEdit": false,
    "configurations": [],
    "name": "UpdatedEmptyMatrixValue",
    "proximityDetails": [
    
      {
        "cidr": "0.0.0.0/0",
        "metric": ,
        "notes": ""
      }
    ]
  }


"""

import pytest

from qe_common import *

logger = init_logger()

@pytest.mark.draft      # need to investigate on null value for Metric
@pytest.mark.components
@pytest.allure.story('Proximity_Zones')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Proximity_Zones test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43881')
    @pytest.mark.Proximity_Zones
    @pytest.mark.PATCH
    def test_TC_43881_PATCH_Proximity_Zones_Unable_To_Modify_Proximity_Zone_With_Empty_Metric_Value(self, context):
        """TC-43881 - Proximity_Zones-PATCH
           Verify that user is unable to Modify[Proximity Zone] on providing empty value for 'Metric' field using request PATCH /proximities{id} " ."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to Modify[Proximity Zone] on providing empty value for 'Metric' field using request PATCH /proximities{id} " ."""):

            # Test case configuration, # tried null , None, [] ,

            proximityZoneDetails = context.sc.ProximityZoneDetails(
                configAdminCanEdit=False,
                configurations=[],
                id=None,
                name='UpdatedEmptyMatrixValue',
                proximityDetails=[{
                    'cidr': '0.0.0.0/0',
                    'metric': '' ,
                    'notes': ""
                }],
                visibleInAllConfigurations=True)

            # prepare the request, so we can modify it
            request = context.cl.Proximity_Zones.updateEntity(
                    id='ProximityUpdate',
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
                get_error_message(e) | expect.all(
                    should.start_with('Invalid request. Unexpected character'),
                    should.contain('expected a valid value')
                    )

            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
