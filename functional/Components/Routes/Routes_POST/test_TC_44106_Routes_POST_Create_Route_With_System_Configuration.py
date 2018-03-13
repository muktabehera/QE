# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44106 - Routes POST:

  Verify that user is able to create route with system configurations using request POST "/routes".


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
   'configurations': [{'host': '172.30.5.204', 'id': 'default'},
                      {'host': '172.30.5.205', 'id': 'QA_Test'}],
   'creationDate': '2016-02-29T09:41:59Z',
   'hops': [{'hops': [],
             'member': {'id': 'autoO1dist1', 'name': 'autoO1dist1'},
             'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
             'memberType': 'EDGE_DEVICE'},
            {'hops': [],
             'member': {'id': 'autoO2dist2', 'name': 'autoO2dist2'},
             'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
             'memberType': 'EDGE_DEVICE'},
            {'hops': [],
             'member': {'id': 'autoEdge1', 'name': 'autoEdge1'},
             'memberRoles': ['DISTRIBUTION', 'EDGE'],
             'memberType': 'EDGE_DEVICE'}],
   'id': 'system1',
   'modificationDate': '2016-02-29T09:42:22Z',
   'name': 'system1',
   'visibleInAllConfigurations': False}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Routes')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Routes test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44106')
    @pytest.mark.Routes
    @pytest.mark.POST
    def test_TC_44106_POST_Routes_Create_Route_With_System_Configuration(self, context):
        """TC-44106 - Routes-POST
           Verify that user is able to create route with system configurations using request POST "/routes"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create route with system configurations using request POST "/routes"."""):

            # Test case configuration
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[
                    {
                        'id': 'default',
                        'host': 'automation-pf03.qumu.media'
                    }
                ],
                hops=[],
                id='route4',
                name='Route4',
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
