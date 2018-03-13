# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-44654 - Groups PATCH:

  Verify that user is unable to modify group on providing blank value in "dnsName" parameter, if  'DNS_Name' value is provided in 'originLoadBalancePolicy' or 'deliveryLoadBalancePolicy' parameters using request PATCH '/groups{id}'.


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
   'deliveryLoadBalancePolicy': 'ALL_MEMBERS',
   'dnsName': '',
   'edgeDeviceRoles': ['EDGE'],
   'members': [{'id': 'Device_Test_API'}],
   'name': 'Updated Group with Blank DNS_NAME',
   'originLoadBalancePolicy': 'DNS_NAME',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44654')
    @pytest.mark.Groups
    @pytest.mark.PATCH
    def test_TC_44654_PATCH_Groups_Group_Blank_D_N_S_Name(self, context):
        """TC-44654 - Groups-PATCH
           Verify that user is unable to modify group on providing blank value in "dnsName" parameter, if  'DNS_Name' value is provided in 'originLoadBalancePolicy' or 'deliveryLoadBalancePolicy' parameters using request PATCH '/groups{id}'."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is unable to modify group on providing blank value in "dnsName" parameter, if  'DNS_Name' value is provided in 'originLoadBalancePolicy' or 'deliveryLoadBalancePolicy' parameters using request PATCH '/groups{id}'."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='ALL_MEMBERS',
                dnsName='',
                edgeDeviceRoles=['EDGE'],
                id=None,
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Updated Group with Blank DNS_NAME',
                originLoadBalancePolicy='DNS_NAME',
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
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('may not be empty'),
                    should.start_with('size must be between 1 and 100')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))



        # Define a test step
        with pytest.allure.step("""Test2: Verify that user is unable to modify group on providing blank value in "dnsName" parameter, if  'DNS_Name' value is provided in 'originLoadBalancePolicy' or 'deliveryLoadBalancePolicy' parameters using request PATCH '/groups{id}'."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='DNS_NAME',
                dnsName='',
                edgeDeviceRoles=['EDGE'],
                id=None,
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Updated Group with Blank DNS_NAME',
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
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('may not be empty'),
                    should.start_with('size must be between 1 and 100')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
