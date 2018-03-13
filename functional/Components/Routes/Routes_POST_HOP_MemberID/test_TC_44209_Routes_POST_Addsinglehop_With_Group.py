# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44209 - Routes POST:

  Verify that user is able to add single hop with GROUP using request POST "/routes/{id}/hops/{memberId}".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/BSRoute1/hops/auto1?memberType=EDGE_DEVICE"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/BSRoute1/hops/auto1?memberType=EDGE_DEVICE"

JSON data sent to PathFinder in this test:

  {'constraintViolations': ['HOP_MEMEBER_NO_PROXIMITY'],
   'hops': [],
   'member': {'id': 'GP1', 'name': 'GP1'},
   'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
   'memberType': 'GROUP'}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Routes')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Routes test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44209')
    @pytest.mark.Routes
    @pytest.mark.POST
    def test_TC_44209_POST_Routes_Addsinglehop_With_Group(self, context):
        """TC-44209 - Routes-POST
           Verify that user is able to add single hop with GROUP using request POST "/routes/{id}/hops/{memberId}"."""
        # Define a test step
        with pytest.allure.step("""First create a Group."""):
            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='PROXIMITY_MATCHES',
                dnsName='10.1.25.46',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id='2GroupforHOP',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='2GroupforHOP',
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
            with pytest.allure.step( """Now create a Route with a GROUP "POST/routes"."""):
                # Test case configuration
                # To add hops, you can create a route with hops.
                routeDetails = context.sc.RouteDetails(
                    configAdminCanEdit=True,
                    configurations=[],
                    hops=[
                        {
                            'hops': [],
                            'id': 1,
                            'member': {
                                'id': '2GroupforHOP',
                                'name': '2GroupforHOP'
                            },
                            'memberType': 'GROUP',
                            'selected': True,
                            'used': True,
                            'memberRoles': ['ORIGIN']
                        }
                    ],
                    id='route26',
                    name='Route26',
                    visibleInAllConfigurations=True)

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
        with pytest.allure.step("""Now verify that user is able to add single hop with GROUP using request POST "/routes/{id}/hops/{memberId}"."""):

            # Test case configuration
            hopDetails = context.sc.HopDetails(
                member={'id': 'ZL-PFE-04',
                        'name': 'ZL-PFE-04'
                        },
                memberType='EDGE_DEVICE',
                memberRoles=['ORIGIN', 'DISTRIBUTION'],
                hops=[
                    {
                        'member': {
                            'id': 'ZL-PFE-03',
                            'name': 'ZL-PFE-03'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['EDGE']
                    }]
            )


            # addHop the Routes.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Routes.addHop(
                    id='route26',
                    body=hopDetails,
                    memberType='GROUP',
                    memberId= '2GroupforHOP'

                )
            )
