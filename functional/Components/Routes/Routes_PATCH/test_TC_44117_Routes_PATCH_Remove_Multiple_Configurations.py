# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44117 - Routes PATCH:

  Verify that user is able to remove multiple system configurations from route using request PATCH "/routes".


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
   'configurations': [],
   'creationDate': '2016-02-24T10:51:17Z',
   'hops': [{'hops': [],
             'member': {'id': '172.30.3.24', 'name': 'Windows Edge 172.30.3.24'},
             'memberRoles': ['EDGE'],
             'memberType': 'EDGE_DEVICE'}],
   'modificationDate': '2016-02-24T10:51:17Z',
   'name': 'BSRoute11New',
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Routes')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Routes test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44117')
    @pytest.mark.Routes
    @pytest.mark.PATCH
    def test_TC_44117_PATCH_Routes_Remove_Multiple_Configurations(self, context):
        """TC-44117 - Routes-PATCH
           Verify that user is able to remove multiple system configurations from route using request PATCH "/routes"."""
        # Define a test step
        with pytest.allure.step("""First create route with multiple system configurations using request POST "/routes"."""):

            # Test case configuration
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[
                    {
                        'id': 'default',
                        'host': 'automation-pf03.qumu.media'
                    }, {
                        'id': 'QA_Test',
                        'host': 'automation-pf03b.qumu.media'
                    }
                ],
                hops=[],
                id='route17',
                name='Route17',
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


        # Define a test step
        with pytest.allure.step("""Then verify that user is able to remove multiple system configurations from route using request PATCH "/routes"."""):

            # Test case configuration
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[],
                name='Route17',
                visibleInAllConfigurations=True)


            # createHop the Routes.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Routes.updateEntity(
                    body=routeDetails,
                    id='route17'

                )
            )

