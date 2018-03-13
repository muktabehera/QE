# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44207 - Routes POST:

  Verify that user correct message is displayed in response body if user provide invalid memberType in schema using request  DELETE "/routes/{id}/hops/{memberId}".


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
             'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
             'memberType': 'EDGE_DEVICE'}],
   'id': 'del',
   'name': 'del',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44207')
    @pytest.mark.Routes
    @pytest.mark.POST
    def test_TC_44207_POST_Routes_Singlehopfrom_Root(self, context):
        """TC-44207 - Routes-POST
           Verify that user correct message is displayed in response body if user provide invalid memberType in schema using request  DELETE "/routes/{id}/hops/{memberId}"."""

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
                id='route31',
                name='Route31',
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
        with pytest.allure.step("""Verify that user correct message is displayed in response body if user provide invalid memberType in schema using request  DELETE "/routes/{id}/hops/{memberId}"."""):

            # Test case configuration
            # prepare the request, so we can modify it
            request = context.cl.Routes.deleteHop(
                    id='route31',
                    memberId='POST_veDevices_AllConfigAdminMulticastTrue',
                    memberType='GROUP'

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
            except (HTTPBadRequest, HTTPForbidden, HTTPNotFound) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Route member with identifier'),
                    should.contain('type GROUP is not found')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
