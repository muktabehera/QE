# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44107 - Routes POST:

  Verify that user is able to create route with single hop from root device using request POST "/routes".


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
             'member': {'id': 'autoO1dist1', 'name': 'autoO1dist1'},
             'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
             'memberType': 'EDGE_DEVICE'}],
   'id': 'hop4',
   'name': 'hop34',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44107')
    @pytest.mark.Routes
    @pytest.mark.POST
    def test_TC_44107_POST_Routes_Create_Route_With_Single_Hop_From_Root(self, context):
        """TC-44107 - Routes-POST
           Verify that user is able to create route with single hop from root device using request POST "/routes"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create route with single hop from root device using request POST "/routes"."""):

            # Test case configuration
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[
                    {
                        'hops': [],
                        'id': 4,
                        'member': {
                            'id': 'ZL-PFE-03',
                            'name': 'ZL-PFE-03'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'selected': True,
                        'used': True,
                        'memberRoles': ['EDGE']
                    }
                ],
                id='route5',
                name='Route5',
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

