# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44122 - Routes PATCH:

  Verify that validation message is displayed if user try to update with wrong ID using request PATCH "/routes".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/BSRoute1BS"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/BSRoute1BS"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': True,
   'configurations': [{'host': '172.30.2.149', 'id': 'default'},
                      {'host': 'qa_test', 'id': 'Qa_test'}],
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44122')
    @pytest.mark.Routes
    @pytest.mark.PATCH
    def test_TC_44122_PATCH_Routes_Verify_Correct_Message_Displayed_If_Wrong_Id_Entered(self, context):
        """TC-44122 - Routes-PATCH
           Verify that validation message is displayed if user try to update with wrong ID using request PATCH "/routes"."""
        # Define a test step
        with pytest.allure.step("""First create route using request POST "/routes"."""):

            # Test case configuration
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[],
                id='route20',
                name='Route20',
                visibleInAllConfigurations=True)

            # createHop the Routes.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.

            response1 = check(
                context.cl.Routes.createRoute(
                    body=routeDetails
                )
            )

        # Define a test step
        with pytest.allure.step("""Then verify that validation message is displayed if user try to update with wrong ID using request PATCH "/routes"."""):

            # Test case configuration
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[],
                name='Route20 updated',
                visibleInAllConfigurations=True)

            # prepare the request, so we can modify it
            request = context.cl.Routes.updateEntity(
                    body=routeDetails,
                    id='route20Wrong'
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
            except (HTTPBadRequest, HTTPForbidden, HTTPNotFound, HTTPConflict) as e:        # 400, 403, 404 error
                get_error_message(e) | expect.any(
                    should.start_with('Delivery Service entity not found'),
                    should.start_with('The ID value you have specified is in use or is invalid.')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
