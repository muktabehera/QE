# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44202 - Routes POST:

  Verify that user is able to create route with group using request POST "/routes".


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
             'memberRoles': ['EDGE', 'DISTRIBUTION'],
             'memberType': 'GROUP'},
            {'hops': [],
             'member': {'id': 'GP2', 'name': 'GP2'},
             'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'],
             'memberType': 'GROUP'},
            {'hops': [],
             'member': {'id': 'GP3', 'name': 'GP3'},
             'memberRoles': ['EDGE', 'DISTRIBUTION'],
             'memberType': 'GROUP'}],
   'id': 'group2',
   'name': 'group2',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44202')
    @pytest.mark.Routes
    @pytest.mark.POST
    def test_TC_44202_POST_Routes_Able_To_Create_Route_With_Group(self, context):
        """TC-44202 - Routes-POST
           Verify that user is able to create route with group using request POST "/routes"."""

        # Define a test step
        with pytest.allure.step("""First create group with valid values for parameters 'id' using request POST /groups."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='PROXIMITY_MATCHES',
                dnsName='10.1.25.46',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id='GroupforRoute',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='GroupforRoute',
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
        with pytest.allure.step("""Now verify that user is able to create route with above group using request POST "/routes"."""):

            # Test case configuration
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[
                    {
                        'hops': [],
                        'id': 3,
                        'member': {
                            'id': 'GroupforRoute',
                            'name': 'GroupforRoute'
                        },
                        'memberType': 'GROUP',
                        'selected': True,
                        'used': True,
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION']
                    }
                ],
                id='route11',
                name='Route11',
                visibleInAllConfigurations=True)

            # createHop the Routes.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Routes.createRoute(
                    body=routeDetails
                )
            )