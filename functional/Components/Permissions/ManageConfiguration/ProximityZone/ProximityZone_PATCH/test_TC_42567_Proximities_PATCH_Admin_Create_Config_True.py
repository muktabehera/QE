# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-42567 - Proximity_Zones PATCH:

  Verify that user is able to Create entities under "VideoNet Configuration" with "Manage Configuration" permission while "Config admin can create" flag is set to true, within the token expiration time.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X PATCH -d @<JSON_data_file> -H "Content-Type:
       application/json"
       "<PF_host>://<client_host>/proximities/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X PATCH -d @<JSON_data_file> -H "Content-Type:
       application/json"
       "<PF_host>://<client_host>/proximities/auto_proximity"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': True,
   'configurations': [{'id': 'automation'}],
   'name': 'Post auto_proximity Updated',
   'proximityDetails': [{'cidr': '0.0.0.0/0', 'metric': 1, 'notes': ''}],
   'visibleInAllConfigurations': False}

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42567')
    @pytest.mark.Proximity_Zones
    @pytest.mark.PATCH
    def test_TC_42567_PATCH_Proximity_Zones_Admin_Create_Config_True(self, context):
        """TC-42567 - Proximity_Zones-PATCH
           Verify that user is able to Create entities under "VideoNet Configuration" with "Manage Configuration" permission while "Config admin can create" flag is set to true, within the token expiration time."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to Create entities under "VideoNet Configuration" with "Manage Configuration" permission while "Config admin can create" flag is set to true, within the token expiration time."""):

            ### Positive test example

            # Test case configuration
            proximityZoneDetails = context.sc.ProximityZoneDetails(
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'automation'
                }],
                id=None,
                name='Post auto_proximity Updated',
                proximityDetails=[{
                    'cidr': '0.0.0.0/0',
                    'metric': 1,
                    'notes': ''
                }],
                visibleInAllConfigurations=False)


            # updateEntity the Proximity_Zones.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Proximity_Zones.updateEntity(
                    body=proximityZoneDetails, 
                    id='auto_proximity'
                
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is able to Create entities under "VideoNet Configuration" with "Manage Configuration" permission while "Config admin can create" flag is set to true, within the token expiration time."""):

            ### Negative test example

            # Test case configuration
            proximityZoneDetails = context.sc.ProximityZoneDetails(
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'automation'
                }],
                id=None,
                name='Post auto_proximity Updated',
                proximityDetails=[{
                    'cidr': '0.0.0.0/0',
                    'metric': 1,
                    'notes': ''
                }],
                visibleInAllConfigurations=False)


            # prepare the request, so we can modify it
            request = context.cl.Proximity_Zones.updateEntity(
                    body=proximityZoneDetails, 
                    id='auto_proximity'
                
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
