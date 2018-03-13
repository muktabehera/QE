# -*- coding: UTF-8 -*-

"""PFE Component Tests - Pathfinder_Edge_Device.

* TC-44137 - Pathfinder_Edge_Device PATCH:

  Verify that user is un-able to create VE device on providing Characters more than 250 in multicastHost field using request PATCH /devices/veDevices/{id}.


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
   'configAdminCanEdit': False,
   'configurations': [{'id': 'default'}],
   'description': 'Test device',
   'deviceGUID': None,
   'deviceHost': 'POST_veDevices',
   'deviceProfileId': 'No_proxy_profile_POST',
   'edgeDeviceRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'],
   'multicastHost': 'http://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.com',
   'name': 'Update Multicast Host',
   'online': False,
   'overrideProfileProperties': False,
   'proximityZones': [{'id': 'ProximityPost'}],
   'rtspMulticastAddressOverride': '10.10.10.10',
   'rtspMulticastEnabledOverride': True,
   'rtspMulticastTTLOverride': 5,
   'streamingHost': 'POST_veDevices',
   'tag': 'tag1',
   'visibleInAllConfigurations': False}

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44137')
    @pytest.mark.Pathfinder_Edge_Device
    @pytest.mark.PATCH
    def test_TC_44137_PATCH_Pathfinder_Edge_Device_Maxlength_Exceed_For_Multicast_Host(self, context):
        """TC-44137 - Pathfinder_Edge_Device-PATCH
           Verify that user is un-able to create VE device on providing Characters more than 250 in multicastHost field using request PATCH /devices/veDevices/{id}."""
        # Define a test step
        with pytest.allure.step("""Verify that user is un-able to create VE device on providing Characters more than 250 in multicastHost field using request PATCH /devices/veDevices/{id}."""):

            ### Positive test example

            # Test case configuration
            videoEdgeDeviceDetails = context.sc.VideoEdgeDeviceDetails(
                alertCount=0,
                configAdminCanEdit=False,
                configurations=[{
                    'id': 'default'
                }],
                currentEdgeVersion=None,
                deactivateReflectorService=None,
                description='Test device',
                deviceGUID=None,
                deviceHost='POST_veDevices',
                deviceProfileId='No_proxy_profile_POST',
                edgeDeviceRoles=['ORIGIN', 'EDGE', 'DISTRIBUTION'],
                id=None,
                multicastHost=
                'http://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.com',
                name='Update Multicast Host',
                online=False,
                osVersion=None,
                overrideProfileProperties=False,
                proximityDetails=None,
                proximityZones=[{
                    'id': 'ProximityPost'
                }],
                rtspMulticastAddressOverride='10.10.10.10',
                rtspMulticastEnabledOverride=True,
                rtspMulticastTTLOverride=5,
                streamingHost='POST_veDevices',
                tag='tag1',
                visibleInAllConfigurations=False)


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

        with pytest.allure.step("""Verify that user is un-able to create VE device on providing Characters more than 250 in multicastHost field using request PATCH /devices/veDevices/{id}."""):

            ### Negative test example

            # Test case configuration
            videoEdgeDeviceDetails = context.sc.VideoEdgeDeviceDetails(
                alertCount=0,
                configAdminCanEdit=False,
                configurations=[{
                    'id': 'default'
                }],
                currentEdgeVersion=None,
                deactivateReflectorService=None,
                description='Test device',
                deviceGUID=None,
                deviceHost='POST_veDevices',
                deviceProfileId='No_proxy_profile_POST',
                edgeDeviceRoles=['ORIGIN', 'EDGE', 'DISTRIBUTION'],
                id=None,
                multicastHost=
                'http://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.comhttp://abc@abc.com',
                name='Update Multicast Host',
                online=False,
                osVersion=None,
                overrideProfileProperties=False,
                proximityDetails=None,
                proximityZones=[{
                    'id': 'ProximityPost'
                }],
                rtspMulticastAddressOverride='10.10.10.10',
                rtspMulticastEnabledOverride=True,
                rtspMulticastTTLOverride=5,
                streamingHost='POST_veDevices',
                tag='tag1',
                visibleInAllConfigurations=False)


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
