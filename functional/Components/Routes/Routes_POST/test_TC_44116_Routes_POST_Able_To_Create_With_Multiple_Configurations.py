# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44116 - Routes POST:

  Verify that user is able to create route with multiple system configurations using request POST "/routes".


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
   'creationDate': '2016-02-24T10:51:17Z',
   'hops': [{'hops': [],
             'member': {'id': '172.30.3.24', 'name': 'Windows Edge 172.30.3.24'},
             'memberRoles': ['EDGE'],
             'memberType': 'EDGE_DEVICE'}],
   'id': 'BSRoute1123',
   'modificationDate': '2016-02-24T10:51:17Z',
   'name': 'BSRoute11',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44116')
    @pytest.mark.Routes
    @pytest.mark.POST
    def test_TC_44116_POST_Routes_Able_To_Create_With_Multiple_Configurations(self, context):
        """TC-44116 - Routes-POST
           Verify that user is able to create route with multiple system configurations using request POST "/routes"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create route with multiple system configurations using request POST "/routes"."""):

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
                id='route12',
                name='Route12',
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

