# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44200 - Routes POST:

  Verify that validation message is displayed on providing invalid member id using request "/routes/{id}/hops".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/hopetest3/hops"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/hopetest3/hops"

JSON data sent to PathFinder in this test:

  {'constraintViolations': ['HOP_MEMEBER_NO_PROXIMITY'],
   'hops': [],
   'member': {'id': 'GP112345', 'name': 'GP112345'},
   'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
   'memberType': 'GROUP'}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Routes')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Routes test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44200')
    @pytest.mark.Routes
    @pytest.mark.POST
    def test_TC_44200_POST_Routes_Validation_Message_On_Entering_Ivalid_Member_Id(self, context):
        """TC-44200 - Routes-POST
           Verify that validation message is displayed on providing invalid member id using request "/routes/{id}/hops"."""
        # Define a test step
        with pytest.allure.step("""Verify that validation message is displayed on providing invalid member id using request "/routes/{id}/hops"."""):

            # Test case configuration
            # To add hops, you can create a route with hops.
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[{
                    'hops': [],
                    'id': 3,
                    'member': {
                        'id': 'GP112345',
                        'name': 'GP112345'
                    },
                    'memberType': 'EDGE_DEVICE',
                    'selected': True,
                    'used': True,
                    'memberRoles': ['EDGE']
                }],
                id='route2',
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

            # createHop the Routes, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Invalid hop details. Provided route member does not exist.'),
                    should.start_with('Invalid hop details.')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
