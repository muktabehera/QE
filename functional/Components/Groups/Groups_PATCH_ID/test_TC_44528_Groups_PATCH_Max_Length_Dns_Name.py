# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-44528 - Groups PATCH:

  Verify that user is able to modify group on providing max length of 100 character in parameter 'dnsName' using request PATCH '/groups'.


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
   'dnsName': 'clientAPI1234!@#clientAPI1234!@#clientAPI1234!@#clientAPI1234!@#clientAPI1234!@#clientAPI1234!@#abcd',
   'edgeDeviceRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
   'members': [{'id': 'Device_Test_API'}],
   'name': 'Updated Group with DNS_Name Max length',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44528')
    @pytest.mark.Groups
    @pytest.mark.PATCH
    def test_TC_44528_PATCH_Groups_Max_Length_Dns_Name(self, context):
        """TC-44528 - Groups-PATCH
           Verify that user is able to modify group on providing max length of 100 character in parameter 'dnsName' using request PATCH '/groups'."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to modify group on providing max length of 100 character in parameter 'dnsName' using request PATCH '/groups'."""):


            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='ALL_MEMBERS',
                dnsName=
                'clientAPI1234!@#clientAPI1234!@#clientAPI1234!@#clientAPI1234!@#clientAPI1234!@#clientAPI1234!@#abcd',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id=None,
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Updated Group with DNS_Name Max length',
                originLoadBalancePolicy='DNS_NAME',
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
