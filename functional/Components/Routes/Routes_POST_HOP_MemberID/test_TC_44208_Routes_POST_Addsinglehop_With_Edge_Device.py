# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44208 - Routes POST:

  Verify that user is able to add single hop with EDGE_DEVICE using request POST "/routes/{id}/hops/{memberId}".


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
   'member': {'id': 'auto2', 'name': 'auto2'},
   'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
   'memberType': 'EDGE_DEVICE'}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Routes')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Routes test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44208')
    @pytest.mark.Routes
    @pytest.mark.POST
    def test_TC_44208_POST_Routes_Addsinglehop_With_Edge_Device(self, context):
        """TC-44208 - Routes-POST
           Verify that user is able to add single hop with EDGE_DEVICE using request POST "/routes/{id}/hops/{memberId}"."""
        # Define a test step
        with pytest.allure.step("""First create route with a HOP using request POST "/routes"."""):
            # Test case configuration
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[
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
                    }
                ],
                id='route25',
                name='Route25',
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
        with pytest.allure.step("""Now verify that user is able to add single hop with EDGE_DEVICE using request POST "/routes/{id}/hops/{memberId}"."""):

            # Test case configuration
            hopDetails = context.sc.HopDetails(
                member={'id': 'ZL-PFE-04',
                        'name': 'ZL-PFE-04'
                        },
                memberType='EDGE_DEVICE',
                memberRoles=['ORIGIN','DISTRIBUTION'],
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
                    id='route25',
                    body=hopDetails,
                    memberType='EDGE_DEVICE',
                    memberId= 'ZL-PFE-05'

                )
            )

