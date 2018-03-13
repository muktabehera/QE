# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44112 - Routes POST:

  Verify that user is unable to create route on providing more than 100 characters in the id and name parameter using POST/PATCH "/routes".


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
   'creationDate': '2016-02-24T10:51:17Z',
   'hops': [{'hops': [],
             'member': {'id': '172.30.3.24', 'name': 'Windows Edge 172.30.3.24'},
             'memberRoles': ['EDGE'],
             'memberType': 'EDGE_DEVICE'}],
   'id': 'aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaaabbbsa',
   'modificationDate': '2016-02-24T10:51:17Z',
   'name': 'ABC',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44112')
    @pytest.mark.Routes
    @pytest.mark.POST
    def test_TC_44112_POST_Routes_Unable_To_Create_With_More_Than_100_Characters_In_Id_Field(self, context):
        """TC-44112 - Routes-POST
           Verify that user is unable to create route on providing more than 100 characters in the id and name parameter using POST/PATCH "/routes"."""
        
        # Define a test step
        with pytest.allure.step("""Test ID: Verify that user is unable to create route on providing more than 100 characters in the id parameter using POST/PATCH "/routes"."""):

            # Test case configuration
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[{
                    'hops': [],
                    'id': 9,
                    'member': {
                        'id': 'POST_veDevices_AllConfigAdminMulticastTrue',
                        'name': 'POST_veDevices_AllConfigAdminMulticastTrue'
                    },
                    'memberType': 'EDGE_DEVICE',
                    'selected': True,
                    'used': True,
                    'memberRoles': ['EDGE']
                }],
                id='qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiop123',
                name='Route2',
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

            # deleteHop the Routes, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('length must be between 1 and 100')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))


        # Define a test step
        with pytest.allure.step("""Test Name: Verify that user is unable to create route on providing more than 100 characters in the name parameter using POST/PATCH "/routes"."""):

            # Test case configuration
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[{
                    'hops': [],
                    'id': 9,
                    'member': {
                        'id': 'POST_veDevices_AllConfigAdminMulticastTrue',
                        'name': 'POST_veDevices_AllConfigAdminMulticastTrue'
                    },
                    'memberType': 'EDGE_DEVICE',
                    'selected': True,
                    'used': True,
                    'memberRoles': ['EDGE']
                }],
                id='Route',
                name='qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiop123',
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

            # deleteHop the Routes, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('length must be between 1 and 100')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
