# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44204 - Routes POST:

  Verify that user is able to DELETE a single hop from root with GROUP using request "/routes/{id}/hops/{memberId}".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': True,
   'configurations': [],
   'hops': [{'hops': [],
             'member': {'id': 'GP1', 'name': 'GP1'},
             'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
             'memberType': 'GROUP'}],
   'id': 'deletegroup',
   'name': 'deletegroup',
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Routes')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Routes test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44204')
    @pytest.mark.Routes
    @pytest.mark.POST
    def test_TC_44204_POST_Routes_Singlehopfrom_Root(self, context):
        """TC-44204 - Routes-POST
           Verify that user is able to DELETE a single hop from root with GROUP using request "/routes/{id}/hops/{memberId}"."""

        # Define a test step
        with pytest.allure.step("""First create a Group."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='PROXIMITY_MATCHES',
                dnsName='10.1.25.46',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id='GroupforHOP',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='GroupforHOP',
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
        with pytest.allure.step("""Now create a single hop from root level with GROUP using request "/routes/{id}/hops"."""):

            # Test case configuration
            # To add hops, you can create a route with hops.
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[{
                    'hops': [],
                    'id': 1,
                    'member': {
                        'id': 'GroupforHOP',
                        'name': 'GroupforHOP'
                    },
                    'memberType': 'GROUP',
                    'selected': True,
                    'used': True,
                    'memberRoles': ['EDGE']
                }],
                id='route24',
                name='Route24',
                visibleInAllConfigurations=True
            )
            # createHop the Routes.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Routes.createRoute(
                    body=routeDetails,
                )
            )

        # Define a test step
        with pytest.allure.step("""Now verify that user is able to DELETE a single hop from root with GROUP using request "/routes/{id}/hops/{memberId}"."""):

            # Test case configuration
            # deleteHop the Routes.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Routes.deleteHop(
                    id='route24',
                    memberId='GroupforHOP',
                    memberType='GROUP'
                )
            )
