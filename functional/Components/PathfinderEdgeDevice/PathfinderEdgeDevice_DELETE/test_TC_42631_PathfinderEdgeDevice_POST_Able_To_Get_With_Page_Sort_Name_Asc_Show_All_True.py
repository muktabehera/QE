# -*- coding: UTF-8 -*-

"""PFE Component Tests - Pathfinder_Edge_Device.

* TC-42631 - Pathfinder_Edge_Device POST:

  Verify that user is able to GET the details of VideoEdge device  request /devices/veDevices  with page,sort=name;asc and showall=true parameter .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veDevices"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veDevices"

JSON data sent to PathFinder in this test:

  {'alertCount': 0,
   'configAdminCanEdit': True,
   'configurations': [],
   'description': '',
   'deviceGUID': None,
   'deviceHost': 'DELETE_device_POST1',
   'deviceProfileId': 'No_proxy_profile_POST',
   'edgeDeviceRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
   'id': 'DELETE_device_POST',
   'multicastHost': 'auto2',
   'name': 'DELETE_device_POST',
   'online': False,
   'overrideProfileProperties': False,
   'proximityDetails': [],
   'proximityZones': [],
   'rtspMulticastAddressOverride': '',
   'rtspMulticastEnabledOverride': False,
   'rtspMulticastTTLOverride': 5,
   'streamingHost': 'auto2',
   'tag': '',
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Pathfinder_Edge_Device')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Pathfinder_Edge_Device test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42631')
    @pytest.mark.Pathfinder_Edge_Device
    @pytest.mark.POST
    def test_TC_42631_POST_Pathfinder_Edge_Device_Able_To_Get_With_Page_Sort_Name_Asc_Show_All_True(self, context):
        """TC-42631 - Pathfinder_Edge_Device-POST
           Verify that user is able to GET the details of VideoEdge device  request /devices/veDevices  with page,sort=name;asc and showall=true parameter ."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of VideoEdge device  request /devices/veDevices  with page,sort=name;asc and showall=true parameter ."""):

            ### Positive test example

            # Test case configuration
            videoEdgeDeviceDetails = context.sc.VideoEdgeDeviceDetails(
                alertCount=0,
                configAdminCanEdit=True,
                configurations=[],
                currentEdgeVersion=None,
                deactivateReflectorService=None,
                description='',
                deviceGUID=None,
                deviceHost='DELETE_device_POST1',
                deviceProfileId='No_proxy_profile_POST',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id='DELETE_device_POST',
                multicastHost='auto2',
                name='DELETE_device_POST',
                online=False,
                osVersion=None,
                overrideProfileProperties=False,
                proximityDetails=[],
                proximityZones=[],
                rtspMulticastAddressOverride='',
                rtspMulticastEnabledOverride=False,
                rtspMulticastTTLOverride=5,
                streamingHost='auto2',
                tag='',
                visibleInAllConfigurations=True)


            # createEntity the Pathfinder_Edge_Device.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Pathfinder_Edge_Device.createEntity(
                    body=videoEdgeDeviceDetails
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is able to GET the details of VideoEdge device  request /devices/veDevices  with page,sort=name;asc and showall=true parameter ."""):

            ### Negative test example

            # Test case configuration
            videoEdgeDeviceDetails = context.sc.VideoEdgeDeviceDetails(
                alertCount=0,
                configAdminCanEdit=True,
                configurations=[],
                currentEdgeVersion=None,
                deactivateReflectorService=None,
                description='',
                deviceGUID=None,
                deviceHost='DELETE_device_POST1',
                deviceProfileId='No_proxy_profile_POST',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id='DELETE_device_POST',
                multicastHost='auto2',
                name='DELETE_device_POST',
                online=False,
                osVersion=None,
                overrideProfileProperties=False,
                proximityDetails=[],
                proximityZones=[],
                rtspMulticastAddressOverride='',
                rtspMulticastEnabledOverride=False,
                rtspMulticastTTLOverride=5,
                streamingHost='auto2',
                tag='',
                visibleInAllConfigurations=True)


            # prepare the request, so we can modify it
            request = context.cl.Pathfinder_Edge_Device.createEntity(
                    body=videoEdgeDeviceDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # createEntity the Pathfinder_Edge_Device, and check we got the error we expect
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
