# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-44373 - Groups GET:

  Verify that user is able to GET all the details of groups on providing 'Id' parameter using request GET /groups{id}.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups/PostGroupWithAllParameter"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups/PostGroupWithAllParameter"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Groups')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Groups test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44373')
    @pytest.mark.Groups
    @pytest.mark.GET
    def test_TC_44373_GET_Groups_Valid_Id(self, context):
        """TC-44373 - Groups-GET
           Verify that user is able to GET all the details of groups on providing 'Id' parameter using request GET /groups{id}."""

        # Define a test step
        with pytest.allure.step("""First create group with valid values for parameters 'id' using request POST /groups."""):
            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='PROXIMITY_MATCHES',
                dnsName='10.1.25.46',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id='Group_testing',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Group_testing',
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
        with pytest.allure.step("""Now verify that user is able to GET all the details of groups on providing 'Id' parameter using request GET /groups{id}."""):
            # getEntity the Groups.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Groups.getEntity(
                    id='Group_testing'
                )
            )
