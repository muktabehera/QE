# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44115 - Routes POST:

  Verify that user is unable to create route with duplicate name and ID using POST "/routes".


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
   'id': 'BSRoute1',
   'modificationDate': '2016-02-24T10:51:17Z',
   'name': 'BSRoute11',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44115')
    @pytest.mark.Routes
    @pytest.mark.POST
    def test_TC_44115_POST_Routes_Un_Able_To_Create_With_Duplicate_Id(self, context):
        """TC-44115 - Routes-POST
           Verify that user is unable to create route with duplicate name and ID using POST "/routes"."""
        # Define a test step
        with pytest.allure.step("""First create route with a name and ID using POST "/routes"."""):

            # Test case configuration
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[],
                id='route10',
                name='Route10',
                visibleInAllConfigurations=True)


            # deleteHop the Routes.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Routes.createRoute(
                    body=routeDetails
                )
            )



        # Define a test step
        with pytest.allure.step("""Now verify that user is unable to create route with duplicate name and ID using POST "/routes"."""):

            # Test case configuration
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[],
                id='route10',
                name='Route10',
                visibleInAllConfigurations=True)


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
            except (HTTPBadRequest, HTTPForbidden, HTTPConflict) as e:        # 400, 403, 409 error
                get_error_message(e) | expect.any(
                    should.start_with('The ID value you have specified is in use or is invalid.')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
