# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44120 - Routes PATCH:

  Verify that user is able to Modify route structure having multiple(10) hops from root device using request PATCH "/routes/{id}".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/BSRoute1"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/BSRoute1"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': True,
   'configurations': [{'host': '172.30.5.204', 'id': 'default'},
                      {'host': '172.30.5.205', 'id': 'QA_Test'}],
   'creationDate': '2016-02-24T10:51:17Z',
   'hops': [{'hops': [],
             'member': {'id': '172.30.3.24', 'name': 'Windows Edge 172.30.3.24'},
             'memberRoles': ['EDGE'],
             'memberType': 'EDGE_DEVICE'}],
   'modificationDate': '2016-02-24T10:51:17Z',
   'name': 'BSRoute11NewName',
   'visibleInAllConfigurations': False}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Routes')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Routes test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44120')
    @pytest.mark.Routes
    @pytest.mark.PATCH
    def test_TC_44120_PATCH_Routes_Modify_Route_Structure(self, context):
        """TC-44120 - Routes-PATCH
           Verify that user is able to Modify route structure having multiple(10) hops from root device using request PATCH "/routes/{id}"."""
        # Define a test step
        with pytest.allure.step("""First create route with multiple hops from root device using request POST "/routes"."""):
            # Test case configuration
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[
                    {
                        'hops': [],
                        'id': 1,
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
                        'id': 3,
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
                        'id': 4,
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
                        'id': 5,
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
                id='route15',
                name='Route15',
                visibleInAllConfigurations=True)

            # createHop the Routes.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response1 = check(
                context.cl.Routes.createRoute(
                    body=routeDetails
                )
            )


        # Define a test step
        with pytest.allure.step("""Then verify that user is able to Modify route structure having multiple hops from root device using request PATCH "/routes/{id}"."""):

            # Test case configuration
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[
                    {
                        'hops': [],
                        'id': 1,
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
                        'id': 3,
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
                        'id': 4,
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
                        'id': 5,
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
                name='Route15 Updated',
                visibleInAllConfigurations=True)


            # createHop the Routes.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Routes.updateEntity(
                    body=routeDetails,
                    id='route15'

                )
            )

