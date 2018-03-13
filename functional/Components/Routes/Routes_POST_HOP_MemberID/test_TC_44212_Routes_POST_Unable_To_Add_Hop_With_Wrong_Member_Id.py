# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44212 - Routes POST:

  Verify that user is unable to add single hop with wrong member ID using request POST "/routes/{id}/hops/{memberId}".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/BSR7/hops"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/BSR7/hops"

JSON data sent to PathFinder in this test:

  {'constraintViolations': ['HOP_MEMEBER_NO_PROXIMITY'],
   'hops': [],
   'member': {'id': 'GP1', 'name': 'GP1'},
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44212')
    @pytest.mark.Routes
    @pytest.mark.POST
    def test_TC_44212_POST_Routes_Unable_To_Add_Hop_With_Wrong_Member_Id(self, context):
        """TC-44212 - Routes-POST
           Verify that user is unable to add single hop with wrong member ID using request POST "/routes/{id}/hops/{memberId}"."""
        # Define a test step
        with pytest.allure.step("""First create route with Edge device using request POST "/routes"."""):
            # Test case configuration
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[
                    {
                        'hops': [],
                        'id': 1,
                        'member': {
                            'id': 'POST_veDevices_AllConfigAdminMulticastTrue',
                            'name': 'POST_veDevices_AllConfigAdminMulticastTrue'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'selected': True,
                        'used': True,
                        'memberRoles': ['ORIGIN']
                    }
                ],
                id='route29',
                name='Route29',
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
        with pytest.allure.step("""Verify that user is unable to add single hop with wrong member ID using request POST "/routes/{id}/hops/{memberId}"."""):


            # Test case configuration
            hopDetails = context.sc.HopDetails(
                member={'id': 'ZL-PFE-04',
                        'name': 'ZL-PFE-04'
                        },
                memberType='EDGE_DEVICE',
                memberRoles=['ORIGIN', 'DISTRIBUTION'],
            )

            # prepare the request, so we can modify it
            request = context.cl.Routes.addHop(
                id='route29',
                body=hopDetails,
                memberType='EDGE_DEVICE',
                memberId='wrong'

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
            except (HTTPBadRequest, HTTPForbidden, HTTPNotFound) as e:        # 400, 403, 404 error
                get_error_message(e) | expect.any(
                    should.start_with('Route member with identifier wrong and type EDGE_DEVICE is not found')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
