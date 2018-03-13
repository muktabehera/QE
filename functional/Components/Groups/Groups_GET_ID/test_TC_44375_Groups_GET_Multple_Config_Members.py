# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-44375 - Groups GET:

  Verify that user is able to get the details of multiple 'Configurations' and 'Members' on providing 'Id' parameter using request GET /groups{id}.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups/groupMultipleConfigMembers1"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups/groupMultipleConfigMembers1"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Groups')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Groups test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44375')
    @pytest.mark.Groups
    @pytest.mark.GET
    def test_TC_44375_GET_Groups_Multple_Config_Members(self, context):
        """TC-44375 - Groups-GET
           Verify that user is able to get the details of multiple 'Configurations' and 'Members' on providing 'Id' parameter using request GET /groups{id}."""

        # Define a test step
        with pytest.allure.step("""First create a group with multiple configurations and multiple Memebrs using request POST '/groups'."""):
            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'default'
                }, {
                    'id': 'QA_Test'
                }],
                deliveryLoadBalancePolicy='PROXIMITY_MATCHES',
                dnsName='10.1.25.46',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id='Group_Testing1',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }, {
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrueTWO'
                }],
                name='Group_Testing1',
                originLoadBalancePolicy='DNS_NAME',
                provisioningPolicy='ALL_MEMBERS',
                proximityDetails=None,
                visibleInAllConfigurations=False)

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
        with pytest.allure.step("""Verify that user is able to get the details of multiple 'Configurations' and 'Members' on providing 'Id' parameter using request GET /groups{id}."""):

            # getEntity the Groups.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Groups.getEntity(
                    id='Group_Testing1'
                )
            )
