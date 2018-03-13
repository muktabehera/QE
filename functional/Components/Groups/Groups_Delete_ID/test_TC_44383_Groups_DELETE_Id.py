# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-44383 - Groups DELETE:

  Verify that user is able to delete the group on providing 'Id' parameter using request DELETE /groups{id}.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups/deleteGroup1"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups/deleteGroup1"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Groups')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Groups test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44383')
    @pytest.mark.Groups
    @pytest.mark.DELETE
    def test_TC_44383_DELETE_Groups_Id(self, context):
        """TC-44383 - Groups-DELETE
           Verify that user is able to delete the group on providing 'Id' parameter using request DELETE /groups{id}."""
        # Define a test step
        with pytest.allure.step("""First create group using request POST /groups."""):
            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='PROXIMITY_MATCHES',
                dnsName='10.1.25.46',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id='GroupD1',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='GroupD1',
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
        with pytest.allure.step("""Now verify that user is able to delete the group on providing 'Id' parameter using request DELETE /groups{id}."""):

            # deleteEntity the Groups.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Groups.deleteEntity(
                    id='GroupD1'
                )
            )

