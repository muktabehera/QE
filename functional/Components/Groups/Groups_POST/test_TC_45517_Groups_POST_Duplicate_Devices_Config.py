# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-45517 - Groups POST:

  Verify that user is not able to add duplicate Devices and configurations in Groups using request POST "/groups".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': False,
   'configurations': [{'id': 'default'}, {'id': 'default'}, {'id': 'default'}],
   'deliveryLoadBalancePolicy': 'PROXIMITY_MATCHES',
   'dnsName': '10.1.25.46',
   'edgeDeviceRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'],
   'id': 'POST_groups_duplicateDevicesConfig1',
   'members': [{'id': 'Device_Test_API'},
               {'id': 'Device_Test_API'},
               {'id': 'Device_Test_API'}],
   'name': 'POST_groups_duplicateDevicesConfig1',
   'originLoadBalancePolicy': 'DNS_NAME',
   'provisioningPolicy': 'ONE_OR_MORE',
   'proximityDetails': [],
   'visibleInAllConfigurations': False}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Groups')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Groups test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-45517')
    @pytest.mark.Groups
    @pytest.mark.POST
    def test_TC_45517_POST_Groups_Duplicate_Devices_Config(self, context):
        """TC-45517 - Groups-POST
           Verify that user is not able to add duplicate Devices and configurations in Groups using request POST "/groups"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is not able to add duplicate Devices and configurations in Groups using request POST "/groups"."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=False,
                configurations=[{
                    'id': 'default'
                }, {
                    'id': 'default'
                }, {
                    'id': 'default'
                }],
                deliveryLoadBalancePolicy='PROXIMITY_MATCHES',
                dnsName='10.1.25.46',
                edgeDeviceRoles=['ORIGIN', 'EDGE', 'DISTRIBUTION'],
                id='POST_groups_duplicateDevicesConfig1',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }, {
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }, {
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='POST_groups_duplicateDevicesConfig1',
                originLoadBalancePolicy='DNS_NAME',
                provisioningPolicy='ONE_OR_MORE',
                proximityDetails=[],
                visibleInAllConfigurations=False)


            # prepare the request, so we can modify it
            request = context.cl.Groups.createEntity(
                    body=edgeDeviceGroupDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # createEntity the Groups, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Invalid group details. Group members shall be unique.')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
