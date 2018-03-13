# -*- coding: UTF-8 -*-

"""PFE Component Tests - Pathfinder_Edge_Device.

* TC-42694 - Pathfinder_Edge_Device PATCH:

  Verify that correct message is displayed for mandatory fields (prozimityZoneID) PATCH "/devices/veDevices/{id}".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veDevices/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veDevices/UpdateDevice"

JSON data sent to PathFinder in this test:

  {'alertCount': 0,
   'configAdminCanEdit': True,
   'configurations': [],
   'description': 'Updated Description',
   'deviceGUID': None,
   'deviceHost': 'POST_veDevicesUpdated',
   'deviceProfileId': 'No_proxy_profile_POST',
   'edgeDeviceRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'],
   'multicastHost': 'POST_veDevices',
   'name': 'Update Proximity',
   'online': False,
   'overrideProfileProperties': False,
   'proximityZones': [{'id': ''}],
   'rtspMulticastAddressOverride': '10.10.10.10',
   'rtspMulticastEnabledOverride': True,
   'rtspMulticastTTLOverride': 5,
   'streamingHost': 'POST_veDevices',
   'tag': 'TagUpdated',
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Pathfinder_Edge_Device')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Pathfinder_Edge_Device test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42694')
    @pytest.mark.Pathfinder_Edge_Device
    @pytest.mark.PATCH
    def test_TC_42694_PATCH_Pathfinder_Edge_Device_Verify_Correct_Message_Is_Displayed_If_Proximity_Zone_Id_Is_Missing(self, context):
        """TC-42694 - Pathfinder_Edge_Device-PATCH
           Verify that correct message is displayed for mandatory fields (prozimityZoneID) PATCH "/devices/veDevices/{id}"."""
        # Define a test step
        with pytest.allure.step("""Verify that correct message is displayed for mandatory fields (prozimityZoneID) PATCH "/devices/veDevices/{id}"."""):

            ### Positive test example

            # Test case configuration
            videoEdgeDeviceDetails = context.sc.VideoEdgeDeviceDetails(
                alertCount=0,
                configAdminCanEdit=True,
                configurations=[],
                currentEdgeVersion=None,
                deactivateReflectorService=None,
                description='Updated Description',
                deviceGUID=None,
                deviceHost='POST_veDevicesUpdated',
                deviceProfileId='No_proxy_profile_POST',
                edgeDeviceRoles=['ORIGIN', 'EDGE', 'DISTRIBUTION'],
                id=None,
                multicastHost='POST_veDevices',
                name='Update Proximity',
                online=False,
                osVersion=None,
                overrideProfileProperties=False,
                proximityDetails=None,
                proximityZones=[{
                    'id': ''
                }],
                rtspMulticastAddressOverride='10.10.10.10',
                rtspMulticastEnabledOverride=True,
                rtspMulticastTTLOverride=5,
                streamingHost='POST_veDevices',
                tag='TagUpdated',
                visibleInAllConfigurations=True)


            # updateEntity the Pathfinder_Edge_Device.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Pathfinder_Edge_Device.updateEntity(
                    body=videoEdgeDeviceDetails, 
                    id='UpdateDevice'
                
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that correct message is displayed for mandatory fields (prozimityZoneID) PATCH "/devices/veDevices/{id}"."""):

            ### Negative test example

            # Test case configuration
            videoEdgeDeviceDetails = context.sc.VideoEdgeDeviceDetails(
                alertCount=0,
                configAdminCanEdit=True,
                configurations=[],
                currentEdgeVersion=None,
                deactivateReflectorService=None,
                description='Updated Description',
                deviceGUID=None,
                deviceHost='POST_veDevicesUpdated',
                deviceProfileId='No_proxy_profile_POST',
                edgeDeviceRoles=['ORIGIN', 'EDGE', 'DISTRIBUTION'],
                id=None,
                multicastHost='POST_veDevices',
                name='Update Proximity',
                online=False,
                osVersion=None,
                overrideProfileProperties=False,
                proximityDetails=None,
                proximityZones=[{
                    'id': ''
                }],
                rtspMulticastAddressOverride='10.10.10.10',
                rtspMulticastEnabledOverride=True,
                rtspMulticastTTLOverride=5,
                streamingHost='POST_veDevices',
                tag='TagUpdated',
                visibleInAllConfigurations=True)


            # prepare the request, so we can modify it
            request = context.cl.Pathfinder_Edge_Device.updateEntity(
                    body=videoEdgeDeviceDetails, 
                    id='UpdateDevice'
                
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateEntity the Pathfinder_Edge_Device, and check we got the error we expect
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
