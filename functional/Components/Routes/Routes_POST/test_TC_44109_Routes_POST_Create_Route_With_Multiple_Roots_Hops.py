# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44109 - Routes POST:

  Verify that user is able to create route with root-5 hops->10 hops each from router using request POST "/routes".


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
   'constraintViolations': ['ROUTE_PROXIMITY_MISSING'],
   'creationDate': '2017-09-05T05:49:43Z',
   'hops': [{'constraintViolations': ['HOP_MEMEBER_NO_PROXIMITY'],
             'hops': [{'constraintViolations': ['HOP_MEMEBER_NO_PROXIMITY'],
                       'hops': [],
                       'member': {'id': 'Test1_auto1_1', 'name': 'Test1_auto1_1'},
                       'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                       'memberType': 'EDGE_DEVICE'},
                      {'constraintViolations': ['HOP_MEMEBER_NO_PROXIMITY'],
                       'hops': [],
                       'member': {'id': 'Test1_auto1_2', 'name': 'Test1_auto1_2'},
                       'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                       'memberType': 'EDGE_DEVICE'}],
             'member': {'id': 'auto1', 'name': 'auto1'},
             'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
             'memberType': 'EDGE_DEVICE'},
            {'constraintViolations': ['HOP_MEMEBER_NO_PROXIMITY'],
             'hops': [{'constraintViolations': ['HOP_MEMEBER_NO_PROXIMITY'],
                       'hops': [],
                       'member': {'id': 'Test2_auto2_1', 'name': 'Test2_auto2_1'},
                       'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                       'memberType': 'EDGE_DEVICE'},
                      {'constraintViolations': ['HOP_MEMEBER_NO_PROXIMITY'],
                       'hops': [],
                       'member': {'id': 'Test2_auto2_2', 'name': 'Test2_auto2_2'},
                       'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                       'memberType': 'EDGE_DEVICE'}],
             'member': {'id': 'auto2', 'name': 'auto2'},
             'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
             'memberType': 'EDGE_DEVICE'},
            {'constraintViolations': ['HOP_MEMEBER_NO_PROXIMITY'],
             'hops': [{'constraintViolations': ['HOP_MEMEBER_NO_PROXIMITY'],
                       'hops': [],
                       'member': {'id': 'Test3_auto3_1', 'name': 'Test3_auto3_1'},
                       'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                       'memberType': 'EDGE_DEVICE'},
                      {'constraintViolations': ['HOP_MEMEBER_NO_PROXIMITY'],
                       'hops': [],
                       'member': {'id': 'Test3_auto3_2', 'name': 'Test3_auto3_2'},
                       'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                       'memberType': 'EDGE_DEVICE'}],
             'member': {'id': 'auto3', 'name': 'auto3'},
             'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
             'memberType': 'EDGE_DEVICE'},
            {'constraintViolations': ['HOP_MEMEBER_NO_PROXIMITY'],
             'hops': [{'constraintViolations': ['HOP_MEMEBER_NO_PROXIMITY'],
                       'hops': [],
                       'member': {'id': 'Test4_auto4_1', 'name': 'Test4_auto4_1'},
                       'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                       'memberType': 'EDGE_DEVICE'},
                      {'constraintViolations': ['HOP_MEMEBER_NO_PROXIMITY'],
                       'hops': [],
                       'member': {'id': 'Test4_auto4_2', 'name': 'Test4_auto4_2'},
                       'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                       'memberType': 'EDGE_DEVICE'}],
             'member': {'id': 'auto4', 'name': 'auto4'},
             'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
             'memberType': 'EDGE_DEVICE'},
            {'constraintViolations': ['HOP_MEMEBER_NO_PROXIMITY'],
             'hops': [{'constraintViolations': ['HOP_MEMEBER_NO_PROXIMITY'],
                       'hops': [],
                       'member': {'id': 'Test5_auto5_1', 'name': 'Test5_auto5_1'},
                       'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                       'memberType': 'EDGE_DEVICE'},
                      {'constraintViolations': ['HOP_MEMEBER_NO_PROXIMITY'],
                       'hops': [],
                       'member': {'id': 'Test5_auto5_2', 'name': 'Test5_auto5_2'},
                       'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                       'memberType': 'EDGE_DEVICE'}],
             'member': {'id': 'auto5', 'name': 'auto5'},
             'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
             'memberType': 'EDGE_DEVICE'},
            {'constraintViolations': ['HOP_MEMEBER_NO_PROXIMITY'],
             'hops': [{'constraintViolations': ['HOP_MEMEBER_NO_PROXIMITY'],
                       'hops': [],
                       'member': {'id': 'GP2', 'name': 'GP2'},
                       'memberRoles': ['EDGE', 'DISTRIBUTION', 'ORIGIN'],
                       'memberType': 'GROUP'},
                      {'constraintViolations': ['HOP_MEMEBER_NO_PROXIMITY'],
                       'hops': [],
                       'member': {'id': 'GP3', 'name': 'GP3'},
                       'memberRoles': ['EDGE', 'DISTRIBUTION'],
                       'memberType': 'GROUP'}],
             'member': {'id': 'GP1', 'name': 'GP1'},
             'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
             'memberType': 'GROUP'}],
   'id': 'Test44109',
   'modificationDate': '2017-09-06T12:09:00Z',
   'name': 'Test44109',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44109')
    @pytest.mark.Routes
    @pytest.mark.POST
    def test_TC_44109_POST_Routes_Create_Route_With_Multiple_Roots_Hops(self, context):
        """TC-44109 - Routes-POST
           Verify that user is able to create route with root-5 hops->10 hops each from router using request POST "/routes"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create route with root-5 hops->10 hops each from router using request POST "/routes"."""):

            # Test case configuration
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[{
                    'hops': [],
                    'id': 7,
                    'member': {
                        'id': 'ZL-PFE-03',
                        'name': 'ZL-PFE-03'
                    },
                    'memberType': 'EDGE_DEVICE',
                    'selected': True,
                    'used': True,
                    'memberRoles': ['EDGE']
                },
                    {
                        'hops': [],
                        'id': 2,
                        'member': {
                            'id': 'ZL-PFE-04',
                            'name': 'ZL-PFE-04'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'selected': True,
                        'used': True,
                        'memberRoles': ['EDGE']
                    },
                    {
                        'hops': [],
                        'id': 1,
                        'member': {
                            'id': 'ZL-PFE-05',
                            'name': 'ZL-PFE-05'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'selected': True,
                        'used': True,
                        'memberRoles': ['EDGE']
                    },
                    {
                        'hops': [],
                        'id': 1,
                        'member': {
                            'id': 'POST_veDevices_AllConfigAdminMulticastTrue',
                            'name': 'POST_veDevices_AllConfigAdminMulticastTrue'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'selected': True,
                        'used': True,
                        'memberRoles': ['EDGE']
                    },
                    {
                        'hops': [],
                        'id': 1,
                        'member': {
                            'id': 'POST_veDevices_AllConfigAdminMulticastTrueTWO',
                            'name': 'POST_veDevices_AllConfigAdminMulticastTrueTWO'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'selected': True,
                        'used': True,
                        'memberRoles': ['EDGE']
                    }
                ],
                id='route7',
                name='Route7',
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
