# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44110 - Routes POST:

  Verify that user is unable to create route without any configurations using request POST "/routes".


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
   'creationDate': '2016-02-29T10:51:27Z',
   'hops': [{'hops': [],
             'member': {'id': 'auto1', 'name': 'auto1'},
             'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
             'memberType': 'EDGE_DEVICE'},
            {'hops': [],
             'member': {'id': 'auto2', 'name': 'auto2'},
             'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
             'memberType': 'EDGE_DEVICE'},
            {'hops': [],
             'member': {'id': 'auto3', 'name': 'auto3'},
             'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
             'memberType': 'EDGE_DEVICE'},
            {'hops': [],
             'member': {'id': 'autoEdge1', 'name': 'autoEdge1'},
             'memberRoles': ['EDGE'],
             'memberType': 'EDGE_DEVICE'},
            {'hops': [],
             'member': {'id': 'autoEdge2', 'name': 'autoEdge2'},
             'memberRoles': ['EDGE'],
             'memberType': 'EDGE_DEVICE'},
            {'hops': [],
             'member': {'id': 'autoO1dist1', 'name': 'autoO1dist1'},
             'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
             'memberType': 'EDGE_DEVICE'},
            {'hops': [],
             'member': {'id': 'autoO2dist2', 'name': 'autoO2dist2'},
             'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
             'memberType': 'EDGE_DEVICE'},
            {'hops': [],
             'member': {'id': 'Device1', 'name': 'Device1'},
             'memberRoles': ['DISTRIBUTION', 'EDGE'],
             'memberType': 'EDGE_DEVICE'},
            {'hops': [],
             'member': {'id': 'GP1', 'name': 'GP1'},
             'memberRoles': ['DISTRIBUTION', 'EDGE'],
             'memberType': 'GROUP'},
            {'hops': [],
             'member': {'id': '172.30.3.24', 'name': 'Windows Edge 172.30.3.24'},
             'memberRoles': ['EDGE'],
             'memberType': 'EDGE_DEVICE'}],
   'id': 'hop12_1',
   'modificationDate': '2016-02-29T10:51:27Z',
   'name': 'hop12_1',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44110')
    @pytest.mark.Routes
    @pytest.mark.POST
    def test_TC_44110_POST_Routes_Unable_To_Create_Route_Without_Configurations(self, context):
        """TC-44110 - Routes-POST
           Verify that user is unable to create route without any configurations using request POST "/routes"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to create route without any configurations using request POST "/routes"."""):

            # Test case configuration
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
                id='route8',
                name='Route8',
                visibleInAllConfigurations=False
            )
            # createHop the Routes.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
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
            except (HTTPBadRequest, HTTPForbidden, HTTPBadRequest, HTTPNotFound) as e:        # 400, 403, 404 error
                get_error_message(e) | expect.any(
                    should.start_with('Either provide the configurations where the system resource is visible or mark it visible in all configurations'),
                    should.start_with('Either provide the configurations where the system resource is visible or mark it visible in all configurations'))
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
