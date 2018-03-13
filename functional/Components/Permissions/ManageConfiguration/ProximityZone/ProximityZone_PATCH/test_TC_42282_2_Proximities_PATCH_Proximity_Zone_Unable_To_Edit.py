# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-42282 - Proximity_Zones PATCH:

  Verify that user is unable to Edit all the entities under Intelligent Content Routing menu, with "Manage Configuration" permission while "Configuration admin can edit" flag is set to false, within the token expiration time.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X PATCH -d @<JSON_data_file> -H "Content-Type:
       application/json"
       "<PF_host>://<client_host>/proximities/<data_ID2_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X PATCH -d @<JSON_data_file> -H "Content-Type:
       application/json"
       "<PF_host>://<client_host>/proximities/unableToEditProximity"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': False,
   'configurations': [{'id': 'automation'}],
   'id': 'unableToEditProximity',
   'name': 'Post: Unable to Edit Proximity',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42282')
    @pytest.mark.Proximity_Zones
    @pytest.mark.PATCH
    def test_TC_42282_PATCH_Proximity_Zones_Proximity_Zone_Unable_To_Edit(self, context):
        """TC-42282 - Proximity_Zones-PATCH
           Verify that user is unable to Edit all the entities under Intelligent Content Routing menu, with "Manage Configuration" permission while "Configuration admin can edit" flag is set to false, within the token expiration time."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to Edit all the entities under Intelligent Content Routing menu, with "Manage Configuration" permission while "Configuration admin can edit" flag is set to false, within the token expiration time."""):

            ### Positive test example

            # Test case configuration
            proximityZoneDetails = context.sc.ProximityZoneDetails(
                configAdminCanEdit=False,
                configurations=[{
                    'id': 'automation'
                }],
                id='unableToEditProximity',
                name='Post: Unable to Edit Proximity',
                proximityDetails=[{
                    'cidr': '0.0.0.0/0',
                    'metric': 1,
                    'notes': ''
                }],
                visibleInAllConfigurations=True)


            # updateEntity the Proximity_Zones.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Proximity_Zones.updateEntity(
                    body=proximityZoneDetails, 
                    id='unableToEditProximity'
                
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is unable to Edit all the entities under Intelligent Content Routing menu, with "Manage Configuration" permission while "Configuration admin can edit" flag is set to false, within the token expiration time."""):

            ### Negative test example

            # Test case configuration
            proximityZoneDetails = context.sc.ProximityZoneDetails(
                configAdminCanEdit=False,
                configurations=[{
                    'id': 'automation'
                }],
                id='unableToEditProximity',
                name='Post: Unable to Edit Proximity',
                proximityDetails=[{
                    'cidr': '0.0.0.0/0',
                    'metric': 1,
                    'notes': ''
                }],
                visibleInAllConfigurations=True)


            # prepare the request, so we can modify it
            request = context.cl.Proximity_Zones.updateEntity(
                    body=proximityZoneDetails, 
                    id='unableToEditProximity'
                
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
                    should.start_with('may not be empty'),
                    should.start_with('Invalid page parameter specified'),
                    should.contain('Invalid Authorization Token')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
