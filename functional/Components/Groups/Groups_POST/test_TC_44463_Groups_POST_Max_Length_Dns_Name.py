# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-44463 - Groups POST:

  Verify that user is able to create group on providing max length of 100 character in parameter 'dnsName' using request POST '/groups'.


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
   'deliveryLoadBalancePolicy': 'DNS_NAME',
   'dnsName': 'clientAPI1234!@#clientAPI1234!@#clientAPI1234!@#clientAPI1234!@#clientAPI1234!@#clientAPI1234!@#abdc',
   'edgeDeviceRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
   'id': 'maxLenghtDnsName11',
   'members': [{'id': 'Device_Test_API'}],
   'name': 'Group with DNS NAME Max Length11',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44463')
    @pytest.mark.Groups
    @pytest.mark.POST
    def test_TC_44463_POST_Groups_Max_Length_Dns_Name(self, context):
        """TC-44463 - Groups-POST
           Verify that user is able to create group on providing max length of 100 character in parameter 'dnsName' using request POST '/groups'."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create group on providing max length of 100 character in parameter 'dnsName' using request POST '/groups'."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='DNS_NAME',
                dnsName=
                'clientAPI1234!@#clientAPI1234!@#clientAPI1234!@#clientAPI1234!@#clientAPI1234!@#clientAPI1234!@#abdc',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id='maxLenghtDnsName11',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Group with DNS NAME Max Length11',
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
