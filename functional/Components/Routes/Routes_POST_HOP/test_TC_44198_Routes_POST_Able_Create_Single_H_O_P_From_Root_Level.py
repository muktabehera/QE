# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44198 - Routes POST:

  Verify that user is able to create a single hop from root level using request "/routes/{id}/hops".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/Test123/hops"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/Test123/hops"

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44198')
    @pytest.mark.Routes
    @pytest.mark.POST
    def test_TC_44198_POST_Routes_Able_Create_Single_H_O_P_From_Root_Level(self, context):
        """TC-44198 - Routes-POST
           Verify that user is able to create a single hop from root level using request "/routes/{id}/hops"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create a single hop from root level using request "/routes/{id}/hops"."""):

            # Test case configuration
            # To add hops, you can create a route with hops.
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[{
                    'hops': [],
                    'id':3,
                    'member': {
                        'id': 'ZL-PFE-03',
                        'name': 'ZL-PFE-03'
                    },
                    'memberType': 'EDGE_DEVICE',
                    'selected': True,
                    'used': True,
                    'memberRoles': ['EDGE']
                }],
                id='route2',
                name='Route2',
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
