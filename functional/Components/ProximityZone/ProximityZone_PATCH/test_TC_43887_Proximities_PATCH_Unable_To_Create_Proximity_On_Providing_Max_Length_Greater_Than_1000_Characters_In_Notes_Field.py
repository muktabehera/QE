# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-43887 - Proximity_Zones PATCH:

  Verify that user is unable to Modify[Notes] by providing length greater than 1000 characters for Proximity Zone using request PATCH /proximities{id} " .


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
   'configurations': [],
   'name': 'UpdatedNotesMaxMoreThanLength1000Character',
   'proximityDetails': [{'cidr': '0.0.0.0/0',
                         'metric': 3,
                         'notes': '12345678901234342342567890123456789012345678901234567890123456789012345678490123456789012345678901234567890123456789012345678901234567890123456789012343423425678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234342342567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123434234256789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012343423425678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234342342567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123434234256789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012343423425678901234567890123456789012'}],
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43887')
    @pytest.mark.Proximity_Zones
    @pytest.mark.PATCH
    def test_TC_43887_PATCH_Proximity_Zones_Unable_To_Create_Proximity_On_Providing_Max_Length_Greater_Than_1000_Characters_In_Notes_Field(self, context):
        """TC-43887 - Proximity_Zones-PATCH
           Verify that user is unable to Modify[Notes] by providing length greater than 1000 characters for Proximity Zone using request PATCH /proximities{id} " ."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to Modify[Notes] by providing length greater than 1000 characters for Proximity Zone using request PATCH /proximities{id} " ."""):

             # Test case configuration
            proximityZoneDetails = context.sc.ProximityZoneDetails(
                configAdminCanEdit=False,
                configurations=[],
                id=None,
                name='UpdatedNotesMaxMoreThanLength1000Character',
                proximityDetails=[{
                    'cidr':
                    '0.0.0.0/0',
                    'metric':
                    3,
                    'notes':
                    '12345678901234342342567890123456789012345678901234567890123456789012345678490123456789012345678901234567890123456789012345678901234567890123456789012343423425678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234342342567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123434234256789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012343423425678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234342342567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123434234256789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012343423425678901234567890123456789012'
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
                get_error_message(e) | expect.any(
                    should.start_with('length must be between 0 and 1000'),
                    should.start_with('must match \"([0-9]{1,3}\\.){3}[0-9]{1,3}\\/[0-9]{1,3}\"'),
                    should.start_with('Invalid configuration identifier')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
