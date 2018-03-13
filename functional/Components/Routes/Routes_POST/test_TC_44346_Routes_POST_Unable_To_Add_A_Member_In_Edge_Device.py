# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44346 - Routes POST:

  Verify that user is unable to add member in Edge device inside the route using request POST "/routes".


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
   'hops': [{'hops': [{'hops': [],
                       'member': {'id': 'auto2', 'name': 'auto2'},
                       'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'EDGE_DEVICE'}],
             'member': {'id': 'auto1', 'name': 'auto1'},
             'memberRoles': ['EDGE'],
             'memberType': 'EDGE_DEVICE'}],
   'id': 'wrong',
   'name': 'wrong',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44346')
    @pytest.mark.Routes
    @pytest.mark.POST
    def test_TC_44346_POST_Routes_Unable_To_Add_A_Member_In_Edge_Device(self, context):
        """TC-44346 - Routes-POST
           Verify that user is unable to add member in Edge device inside the route using request POST "/routes"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to add member in Edge device inside the route using request POST "/routes"."""):
            # Test case configuration
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[{
                    'id': 3,
                    'member': {
                        'id': 'POST_veDevices_AllConfigAdminMulticastTrueThree',
                        'name': 'POST_veDevices_AllConfigAdminMulticastTrueThree'
                    },
                    'memberType':'EDGE_DEVICE',
                    'selected': True,
                    'used': True,
                    'memberRoles': ['EDGE'],
                    'hops': [{
                        'id': 2,
                        'member': {
                            'id': 'POST_veDevices_AllConfigAdminMulticastTrue',
                            'name': 'POST_veDevices_AllConfigAdminMulticastTrue'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'selected': True,
                        'used': True,
                        'memberRoles': ['ORIGIN', 'DISTRIBUTION', 'EDGE'],
                        'hops': []
                    }]
                }],
                id='route13',
                name='Route13',
                visibleInAllConfigurations=True
            )


            # prepare the request, so we can modify it
            request = context.cl.Routes.createRoute(
                    body=routeDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # createHop the Routes, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden, HTTPConflict, HTTPNotFound) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Route member with identifier'),
                    should.contain(' does not have DISTRIBUTION role, but has children')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
