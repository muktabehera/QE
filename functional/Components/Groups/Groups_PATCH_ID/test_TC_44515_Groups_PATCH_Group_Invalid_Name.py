# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-44515 - Groups PATCH:

  Verify that correct error message is displayed in response on modifying group with invalid values in parameters 'Name' using request PATCH /groups.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups/updateGroup"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups/updateGroup"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': True,
   'configurations': [],
   'deliveryLoadBalancePolicy': 'DNS_NAME',
   'dnsName': 'autoQEDVCC1',
   'edgeDeviceRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
   'members': [{'id': 'Device_Test_API'}],
   'name': '12POST@ID',
   'originLoadBalancePolicy': 'ALL_MEMBERS',
   'provisioningPolicy': 'ALL_MEMBERS',
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Groups')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Groups test cases."""

    @pytest.allure.issue('https://jira.qumu.com/browse/QED-1917')
    @pytest.allure.link('https://jira.qumu.com/browse/TC-44515')
    @pytest.mark.Groups
    @pytest.mark.PATCH
    def test_TC_44515_PATCH_Groups_Group_Invalid_Name(self, context):
        """TC-44515 - Groups-PATCH
           Verify that correct error message is displayed in response on modifying group with invalid values in parameters 'Name' using request PATCH /groups."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that correct error message is displayed in response on modifying group with invalid values in parameters 'Name' using request PATCH /groups."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='DNS_NAME',
                dnsName='autoQEDVCC1',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id=None,
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='12POST@ID',
                originLoadBalancePolicy='ALL_MEMBERS',
                provisioningPolicy='ALL_MEMBERS',
                proximityDetails=None,
                visibleInAllConfigurations=True)


            # prepare the request, so we can modify it
            request = context.cl.Groups.updateEntity(
                    id='GroupforPatch2',
                    body=edgeDeviceGroupDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateEntity the Groups, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden, HTTPNotFound) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Delivery Service entity not found')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))

        # Define a test step
        with pytest.allure.step("""Test2: Verify that correct error message is displayed in response on modifying group with invalid values in parameters 'Name' using request PATCH /groups."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='DNS_NAME',
                dnsName='autoQEDVCC1',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id=None,
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Ab12/<>|\^',
                originLoadBalancePolicy='ALL_MEMBERS',
                provisioningPolicy='ALL_MEMBERS',
                proximityDetails=None,
                visibleInAllConfigurations=True)


            # prepare the request, so we can modify it
            request = context.cl.Groups.updateEntity(
                    id='GroupforPatch2',
                    body=edgeDeviceGroupDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateEntity the Groups, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden, HTTPNotFound) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Delivery Service entity not found'),
                    should.start_with('Invalid name, the pattern must match \"^[\\p{IsAlphabetic}\\p{IsDigit}]+[\\p{Blak}\\p{IsAlphabetic}\\p{IsDigit}[\\p{Punct}&&[^/\\<>\\|\\^]]]*$\"')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))


        # Define a test step
        with pytest.allure.step("""Test3: Verify that correct error message is displayed in response on modifying group with invalid values in parameters 'Name' using request PATCH /groups."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='DNS_NAME',
                dnsName='autoQEDVCC1',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id=None,
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='/<>|\^,!@ABCD',
                originLoadBalancePolicy='ALL_MEMBERS',
                provisioningPolicy='ALL_MEMBERS',
                proximityDetails=None,
                visibleInAllConfigurations=True)


            # prepare the request, so we can modify it
            request = context.cl.Groups.updateEntity(
                    id='GroupforPatch2',
                    body=edgeDeviceGroupDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateEntity the Groups, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden, HTTPNotFound) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Delivery Service entity not found'),
                    should.start_with('Invalid name, the pattern must match \"^[\\p{IsAlphabetic}\\p{IsDigit}]+[\\p{Blak}\\p{IsAlphabetic}\\p{IsDigit}[\\p{Punct}&&[^/\\<>\\|\\^]]]*$\"')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))