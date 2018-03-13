# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-43864 - Proximity_Zones PATCH:

  Verify that validation message is displayed while removing mandatory field (Configurations) while "visibleInAllConfigurations: false for  Proximity Zone using request PATCH /proximities{id} ".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/ProximtyUpdate"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/ProximtyUpdate"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': False,
   'configurations': [],
   'name': 'MandatoryFieldMissing',
   'proximityDetails': [{'cidr': '0.0.0.0/0', 'metric': 1, 'notes': ''}],
   'visibleInAllConfigurations': False}

"""

import pytest

from qe_common import *

logger = init_logger()







@pytest.mark.components
@pytest.allure.story('Proximity_Zones')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Proximity_Zones test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43864')
    @pytest.mark.Proximity_Zones
    @pytest.mark.PATCH
    def test_TC_43864_PATCH_Proximity_Zones_Verify_Validation_Message_Is_Displayed_While_Removing_Mandatory_Fields(self, context):
        """TC-43864 - Proximity_Zones-PATCH
           Verify that validation message is displayed while removing mandatory field (Configurations) while "visibleInAllConfigurations: false for  Proximity Zone using request PATCH /proximities{id} "."""
        # Define a test step
        with pytest.allure.step("""Verify that validation message is displayed while removing mandatory field (Configurations) while "visibleInAllConfigurations: false for  Proximity Zone using request PATCH /proximities{id} "."""):

            # Test case configuration
            proximityZoneDetails = context.sc.ProximityZoneDetails(
                configAdminCanEdit=False,
                configurations=[],
                id=None,
                name='MandatoryFieldMissing',
                proximityDetails=[{
                    'cidr': '0.0.0.0/0',
                    'metric': 1,
                    'notes': ''
                }],
                visibleInAllConfigurations=False)


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
                    should.start_with('Either provide the configurations where the system resource is visible or mark it visible in all configurations'),
                    should.start_with('must match \"([0-9]{1,3}\\.){3}[0-9]{1,3}\\/[0-9]{1,3}\"'),

                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
