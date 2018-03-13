# -*- coding: UTF-8 -*-

"""PFE Component Tests - Pathfinder_Edge_Device.

* TC-42569 - Pathfinder_Edge_Device PATCH:

  Verify that user is able to Edit/Delete all the entities under "VideoNet Configuration" with "Manage Configuration" permission while "Configuration admin can edit" and "Configuration admin can create" flags are set to true within token expiration time.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X PATCH -d @<JSON_data_file> -H "Content-Type:
       application/json"
       "<PF_host>://<client_host>/devices/veDevices/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X PATCH -d @<JSON_data_file> -H "Content-Type:
       application/json"
       "<PF_host>://<client_host>/devices/veDevices/autoVideonetEdge"

JSON data sent to PathFinder in this test:

  {'alertCount': 0,
   'configAdminCanEdit': True,
   'configurations': [{'id': 'automation'}],
   'description': '',
   'deviceGUID': None,
   'deviceHost': '172.30.2.149',
   'deviceProfileId': 'autoProfile',
   'edgeDeviceRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'],
   'multicastHost': '172.30.2.149',
   'name': 'PATCH: Auto Videonet Edge',
   'online': False,
   'overrideProfileProperties': False,
   'proximityDetails': [],
   'proximityZones': [{'id': 'auto_proximity'}],
   'rtspMulticastAddressOverride': '10.10.10.10',
   'rtspMulticastEnabledOverride': True,
   'rtspMulticastTTLOverride': 5,
   'streamingHost': '172.30.2.149',
   'tag': '',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42569')
    @pytest.mark.Pathfinder_Edge_Device
    @pytest.mark.PATCH
    def test_TC_42569_PATCH_Pathfinder_Edge_Device_Id(self, context):
        """TC-42569 - Pathfinder_Edge_Device-PATCH
           Verify that user is able to Edit/Delete all the entities under "VideoNet Configuration" with "Manage Configuration" permission while "Configuration admin can edit" and "Configuration admin can create" flags are set to true within token expiration time."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to Edit/Delete all the entities under "VideoNet Configuration" with "Manage Configuration" permission while "Configuration admin can edit" and "Configuration admin can create" flags are set to true within token expiration time."""):

            ### Positive test example

            # Test case configuration
            videoEdgeDeviceDetails = context.sc.VideoEdgeDeviceDetails(
                alertCount=0,
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'automation'
                }],
                currentEdgeVersion=None,
                deactivateReflectorService=None,
                description='',
                deviceGUID=None,
                deviceHost='172.30.2.149',
                deviceProfileId='autoProfile',
                edgeDeviceRoles=['ORIGIN', 'EDGE', 'DISTRIBUTION'],
                id=None,
                multicastHost='172.30.2.149',
                name='PATCH: Auto Videonet Edge',
                online=False,
                osVersion=None,
                overrideProfileProperties=False,
                proximityDetails=[],
                proximityZones=[{
                    'id': 'auto_proximity'
                }],
                rtspMulticastAddressOverride='10.10.10.10',
                rtspMulticastEnabledOverride=True,
                rtspMulticastTTLOverride=5,
                streamingHost='172.30.2.149',
                tag='',
                visibleInAllConfigurations=False)


            # updateEntity the Pathfinder_Edge_Device.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Pathfinder_Edge_Device.updateEntity(
                    body=videoEdgeDeviceDetails, 
                    id='autoVideonetEdge'
                
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is able to Edit/Delete all the entities under "VideoNet Configuration" with "Manage Configuration" permission while "Configuration admin can edit" and "Configuration admin can create" flags are set to true within token expiration time."""):

            ### Negative test example

            # Test case configuration
            videoEdgeDeviceDetails = context.sc.VideoEdgeDeviceDetails(
                alertCount=0,
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'automation'
                }],
                currentEdgeVersion=None,
                deactivateReflectorService=None,
                description='',
                deviceGUID=None,
                deviceHost='172.30.2.149',
                deviceProfileId='autoProfile',
                edgeDeviceRoles=['ORIGIN', 'EDGE', 'DISTRIBUTION'],
                id=None,
                multicastHost='172.30.2.149',
                name='PATCH: Auto Videonet Edge',
                online=False,
                osVersion=None,
                overrideProfileProperties=False,
                proximityDetails=[],
                proximityZones=[{
                    'id': 'auto_proximity'
                }],
                rtspMulticastAddressOverride='10.10.10.10',
                rtspMulticastEnabledOverride=True,
                rtspMulticastTTLOverride=5,
                streamingHost='172.30.2.149',
                tag='',
                visibleInAllConfigurations=False)


            # prepare the request, so we can modify it
            request = context.cl.Pathfinder_Edge_Device.updateEntity(
                    body=videoEdgeDeviceDetails, 
                    id='autoVideonetEdge'
                
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
