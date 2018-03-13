# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-44461 - Groups POST:

  Verify that user is unable to create group on providing invalid values in parameter 'originLoadBalancePolicy' using request POST '/groups'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': True,
   'configurations': [],
   'deliveryLoadBalancePolicy': 'PROXIMITY_MATCHES',
   'dnsName': '10.1.25.46',
   'edgeDeviceRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
   'id': 'originLoadBalancePolicyInvalid3',
   'members': [{'id': 'Device_Test_API'}],
   'name': 'Group with invalid originLoadBalancePolicy 3',
   'originLoadBalancePolicy': '!@#$%',
   'provisioningPolicy': 'ALL_MEMBERS',
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Groups')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Groups test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44461')
    @pytest.mark.Groups
    @pytest.mark.POST
    def test_TC_44461_POST_Groups_Group_Invalid_Origin_Load_Balance_Policy(self, context):
        """TC-44461 - Groups-POST
           Verify that user is unable to create group on providing invalid values in parameter 'originLoadBalancePolicy' using request POST '/groups'."""

        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is unable to create group on providing invalid values in parameter 'originLoadBalancePolicy' using request POST '/groups'."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='PROXIMITY_MATCHES',
                dnsName='10.1.25.46',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id='originLoadBalancePolicyInvalid3',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Group with invalid originLoadBalancePolicy 3',
                originLoadBalancePolicy='!@#$%',
                provisioningPolicy='ALL_MEMBERS',
                proximityDetails=None,
                visibleInAllConfigurations=True)


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
                    should.start_with('Invalid request. Can not construct instance of com.qumu.qed.group.DeliveryLoadBalancePolicy from String value'),
                    should.contain('value not one of declared Enum instance names: [DNS_NAME, PROXIMITY_MATCHES,ALL_MEMBERS]'),
                    should.contain('value not one of declared Enum instance names: [DNS_NAME, ORDERED, STRICT_ORDERED, ALL_MEMBERS]')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))


        # Define a test step
        with pytest.allure.step("""Test2: Verify that user is unable to create group on providing invalid values in parameter 'originLoadBalancePolicy' using request POST '/groups'."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='PROXIMITY_MATCHES',
                dnsName='10.1.25.46',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id='originLoadBalancePolicyInvalid4',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Group with invalid originLoadBalancePolicy 4',
                originLoadBalancePolicy='ABCD123!',
                provisioningPolicy='ALL_MEMBERS',
                proximityDetails=None,
                visibleInAllConfigurations=True)


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
                    should.start_with('Invalid request. Can not construct instance of com.qumu.qed.group.DeliveryLoadBalancePolicy from String value'),
                    should.contain('value not one of declared Enum instance names: [DNS_NAME, PROXIMITY_MATCHES,ALL_MEMBERS]'),
                    should.contain('value not one of declared Enum instance names: [DNS_NAME, ORDERED, STRICT_ORDERED, ALL_MEMBERS]')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))

        # Define a test step
        with pytest.allure.step("""Test3: Verify that user is unable to create group on providing invalid values in parameter 'originLoadBalancePolicy' using request POST '/groups'."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='PROXIMITY_MATCHES',
                dnsName='10.1.25.46',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id='originLoadBalancePolicyInvalid2',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Group with invalid originLoadBalancePolicy 2',
                originLoadBalancePolicy='123456',
                provisioningPolicy='ALL_MEMBERS',
                proximityDetails=None,
                visibleInAllConfigurations=True)


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
                    should.start_with('Invalid request. Can not construct instance of com.qumu.qed.group.DeliveryLoadBalancePolicy from String value'),
                    should.contain('value not one of declared Enum instance names: [DNS_NAME, PROXIMITY_MATCHES,ALL_MEMBERS]'),
                    should.contain('value not one of declared Enum instance names: [DNS_NAME, ORDERED, STRICT_ORDERED, ALL_MEMBERS]')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))


        # Define a test step
        with pytest.allure.step("""Test4: Verify that user is unable to create group on providing invalid values in parameter 'originLoadBalancePolicy' using request POST '/groups'."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='PROXIMITY_MATCHES',
                dnsName='10.1.25.46',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id='originLoadBalancePolicyInvalid1',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Group with invalid originLoadBalancePolicy',
                originLoadBalancePolicy='ABCD',
                provisioningPolicy='ALL_MEMBERS',
                proximityDetails=None,
                visibleInAllConfigurations=True)


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
                    should.start_with('Invalid request. Can not construct instance of com.qumu.qed.group.DeliveryLoadBalancePolicy from String value'),
                    should.contain('value not one of declared Enum instance names: [DNS_NAME, PROXIMITY_MATCHES,ALL_MEMBERS]'),
                should.contain(' value not one of declared Enum instance names: [DNS_NAME, ORDERED, STRICT_ORDERED, ALL_MEMBERS]')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
