# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-43964 - Proximity_Zones PATCH:

  Verify that user is unable to Modify[Metric] on providing value starting with 0 for Proximity Zone using request PATCH /proximities{id}".


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
    "id": "1112",
    "name": "ab1",
    "proximityDetails": [
    
      {
        "cidr": " ",
        "metric": 01,
        "notes": ""
      }
    ]
  }


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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43964')
    @pytest.mark.Proximity_Zones
    @pytest.mark.PATCH
    def test_TC_43964_PATCH_Proximity_Zones_Unable_To_Create_Proximity_Zone_If_Matrix_Field_Value_Starts_With_Zero(self, context):
        """TC-43964 - Proximity_Zones-PATCH
           Verify that user is unable to Modify[Metric] on providing value starting with 0 for Proximity Zone using request PATCH /proximities{id}"."""
        # Define a test step
        with pytest.allure.step("Create a Proximity Zone"):

            proximityZoneDetails = context.sc.ProximityZoneDetails(
                configAdminCanEdit=False,
                configurations=[],
                id= 'UpdatedEmptyMatrixValue',
                name='UpdatedEmptyMatrixValue',
                proximityDetails=[{
                    'cidr': '0.0.0.0/0',
                    'metric': 1,
                    'notes': "one"
                }],
                visibleInAllConfigurations=True)

            check(
                context.cl.Proximity_Zones.createEntity(
                    body=proximityZoneDetails
                )
            )

        with pytest.allure.step("""Verify that user is unable to Modify[Metric] on providing value starting with 0 for Proximity Zone using request PATCH /proximities{id}"."""):

            # Test case configuration

            proximityZoneDetails = context.sc.ProximityZoneDetails(
                configAdminCanEdit=False,
                configurations=[],
                id=None,
                name='UpdatedEmptyMatrixValue2',
                proximityDetails=[{
                    'cidr': '0.0.0.0/0',
                    'metric': '01234',
                    'notes': "notes"
                }],
                visibleInAllConfigurations=True)

            # prepare the request, so we can modify it
            request = context.cl.Proximity_Zones.updateEntity(
                    id='UpdatedEmptyMatrixValue',
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
                    should.start_with('Invalid request. Invalid numeric value: Leading zeroes not allowed'),
                    should.start_with('Invalid configuration identifier'),
                    should.contain('must match \"([0-9]{1,3}\\.){3}[0-9]{1,3}\\/[0-9]{1,3}\"')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
