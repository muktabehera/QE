# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-44656 - Groups PATCH:

  Verify that user is unable to modify group on providing invalid values parameter 'edgeDeviceRoles' using request PATCH '/groups{id}'.


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
   'dnsName': 'QEDVCC',
   'edgeDeviceRoles': ['ABCD'],
   'members': [{'id': 'Device_Test_API'}],
   'name': 'Updated Group invalid Role value',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44656')
    @pytest.mark.Groups
    @pytest.mark.PATCH
    def test_TC_44656_PATCH_Groups_Group_Invalid_Role(self, context):
        """TC-44656 - Groups-PATCH
           Verify that user is unable to modify group on providing invalid values parameter 'edgeDeviceRoles' using request PATCH '/groups{id}'."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is unable to modify group on providing invalid values parameter 'edgeDeviceRoles' using request PATCH '/groups{id}'."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='ALL_MEMBERS',
                dnsName='QEDVCC',
                edgeDeviceRoles=['ABCD'],
                id=None,
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Updated Group invalid Role value',
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
                    should.start_with('Invalid request. Can not construct instance of com.qumu.qed.delivery.route.EdgeDeviceRole from String value'),
                    should.contain('value not one of declared Enum instance names: [ORIGIN, DISTRIBUTION, EDGE]')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))


        # Define a test step
        with pytest.allure.step("""Test2: Verify that user is unable to modify group on providing invalid values parameter 'edgeDeviceRoles' using request PATCH '/groups{id}'."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='ALL_MEMBERS',
                dnsName='QEDVCC',
                edgeDeviceRoles=[1234],
                id=None,
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Updated Group invalid Role value',
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
                    should.start_with('Invalid request. Can not construct instance of com.qumu.qed.delivery.route.EdgeDeviceRole from number value'),
                    should.contain('index value outside legal index range [0..2]')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))



        # Define a test step
        with pytest.allure.step("""Test3: Verify that user is unable to modify group on providing invalid values parameter 'edgeDeviceRoles' using request PATCH '/groups{id}'."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='ALL_MEMBERS',
                dnsName='QEDVCC',
                edgeDeviceRoles=[],
                id=None,
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Updated Group invalid Role value',
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
                    should.start_with('Invalid request. Can not construct instance of com.qumu.qed.delivery.route.EdgeDeviceRole from number value'),
                    should.contain('index value outside legal index range [0..2]'),
                    should.start_with('size must be between 1 and 2147483647'),
                    should.start_with('may not be empty'),
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))