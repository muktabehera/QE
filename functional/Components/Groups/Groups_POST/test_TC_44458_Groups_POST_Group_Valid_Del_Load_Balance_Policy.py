# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-44458 - Groups POST:

  Verify that user is able to create group on providing valid values in parameter 'deliveryLoadBalancePolicy' using request POST '/groups'.


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
   'deliveryLoadBalancePolicy': 'ALL_MEMBERS',
   'dnsName': '10.1.25.46',
   'edgeDeviceRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
   'id': 'delLoadBalancePolicyvalid31',
   'members': [{'id': 'Device_Test_API'}],
   'name': 'Group with valid Del Load Balance Policy31',
   'originLoadBalancePolicy': 'DNS_NAME',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44458')
    @pytest.mark.Groups
    @pytest.mark.POST
    def test_TC_44458_POST_Groups_Group_Valid_Del_Load_Balance_Policy(self, context):
        """TC-44458 - Groups-POST
           Verify that user is able to create group on providing valid values in parameter 'deliveryLoadBalancePolicy' using request POST '/groups'."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is able to create group on providing valid values in parameter 'deliveryLoadBalancePolicy' using request POST '/groups'."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='ALL_MEMBERS',
                dnsName='10.1.25.46',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id='delLoadBalancePolicyvalid31',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Group with valid Del Load Balance Policy31',
                originLoadBalancePolicy='DNS_NAME',
                provisioningPolicy='ALL_MEMBERS',
                proximityDetails=None,
                visibleInAllConfigurations=True)


            # createEntity the Groups.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Groups.createEntity(
                    body=edgeDeviceGroupDetails
                )
            )

        # Define a test step
        with pytest.allure.step("""Test2: Verify that user is able to create group on providing valid values in parameter 'deliveryLoadBalancePolicy' using request POST '/groups'."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='DNS_NAME',
                dnsName='10.1.25.46',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id='delLoadBalancePolicyvalid21',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Group with valid Del Load Balance Policy21',
                originLoadBalancePolicy='DNS_NAME',
                provisioningPolicy='ALL_MEMBERS',
                proximityDetails=None,
                visibleInAllConfigurations=True)


            # createEntity the Groups.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Groups.createEntity(
                    body=edgeDeviceGroupDetails
                )
            )


        # Define a test step
        with pytest.allure.step("""Test3: Verify that user is able to create group on providing valid values in parameter 'deliveryLoadBalancePolicy' using request POST '/groups'."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='PROXIMITY_MATCHES',
                dnsName='10.1.25.46',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id='delLoadBalancePolicyvalid11',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Group with valid Del Load Balance Policy1',
                originLoadBalancePolicy='DNS_NAME',
                provisioningPolicy='ALL_MEMBERS',
                proximityDetails=None,
                visibleInAllConfigurations=True)


            # createEntity the Groups.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Groups.createEntity(
                    body=edgeDeviceGroupDetails
                )
            )