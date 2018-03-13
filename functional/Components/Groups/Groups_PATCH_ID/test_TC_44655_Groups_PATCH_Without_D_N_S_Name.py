# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-44655 - Groups PATCH:

  Verify that user is able to modify group with parameter "dnsName", if  'DNS_Name' value is not provided in 'originLoadBalancePolicy' or 'deliveryLoadBalancePolicy' parameters using request PATCH '/groups{id}'.


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
   'edgeDeviceRoles': ['EDGE'],
   'members': [{'id': 'Device_Test_API'}],
   'name': 'Updated Group without DNS Name',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44655')
    @pytest.mark.Groups
    @pytest.mark.PATCH
    def test_TC_44655_PATCH_Groups_Without_D_N_S_Name(self, context):
        """TC-44655 - Groups-PATCH
           Verify that user is able to modify group with parameter "dnsName", if  'DNS_Name' value is not provided in 'originLoadBalancePolicy' or 'deliveryLoadBalancePolicy' parameters using request PATCH '/groups{id}'."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to modify group with parameter "dnsName", if  'DNS_Name' value is not provided in 'originLoadBalancePolicy' or 'deliveryLoadBalancePolicy' parameters using request PATCH '/groups{id}'."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='ALL_MEMBERS',
                dnsName='QEDVCC',
                edgeDeviceRoles=['EDGE'],
                id=None,
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Updated Group without DNS Name',
                originLoadBalancePolicy='ALL_MEMBERS',
                provisioningPolicy='ALL_MEMBERS',
                proximityDetails=None,
                visibleInAllConfigurations=True)


            # updateEntity the Groups.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Groups.updateEntity(
                    id='GroupforPatch2',
                    body=edgeDeviceGroupDetails
                )
            )

