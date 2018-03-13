# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44203 - Routes POST:

  Verify that user is able to DELETE a single hop from root with EDGE_DEVICE using request "/routes/{id}/hops/{memberId}".


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
             'member': {'id': 'auto1', 'name': 'auto1'},
             'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
             'memberType': 'EDGE_DEVICE'}],
   'id': 'deletedevicefromroot',
   'name': 'deletedevicefromroot',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44203')
    @pytest.mark.Routes
    @pytest.mark.POST
    def test_TC_44203_POST_Routes_Singlehopfrom_Root(self, context):
        """TC-44203 - Routes-POST
           Verify that user is able to DELETE a single hop from root with EDGE_DEVICE using request "/routes/{id}/hops/{memberId}"."""
        # Define a test step
        with pytest.allure.step("""First create a single hop from root level using request "/routes/{id}/hops"."""):
            # Test case configuration
            # To add hops, you can create a route with hops.
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[{
                    'hops': [],
                    'id': 3,
                    'member': {
                        'id': 'POST_veDevices_AllConfigAdminMulticastTrue',
                        'name': 'POST_veDevices_AllConfigAdminMulticastTrue'
                    },
                    'memberType': 'EDGE_DEVICE',
                    'selected': True,
                    'used': True,
                    'memberRoles': ['EDGE']
                }],
                id='route23',
                name='Route23',
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
        with pytest.allure.step("""Now verify that user is able to DELETE a single hop from root with EDGE_DEVICE using request "/routes/{id}/hops/{memberId}"."""):

            # Test case configuration
            # deleteHop the Routes.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            # response1 = check(
            #     context.cl.Routes.deleteHop(
            #         id= 'route23',
            #         memberId='3'
            #     )
            # )
            check(
                context.cl.Routes.deleteHop(
                    id='route23',
                    memberId='POST_veDevices_AllConfigAdminMulticastTrue',
                    memberType='EDGE_DEVICE'

                )
            )

