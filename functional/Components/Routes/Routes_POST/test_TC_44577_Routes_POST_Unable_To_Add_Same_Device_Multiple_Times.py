# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44577 - Routes POST:

  Verify that user is unable to add same device multiple times using post "/routes".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/BSR8/hops"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/BSR8/hops"

JSON data sent to PathFinder in this test:

  {
        "member": {
          "id": "GP1",
          "name": "GP1"
        },
        "memberType": "GROUP",
        "memberRoles": [
          "ORIGIN",
          "EDGE",
          "DISTRIBUTION"
        ],
        "hops": []
      
      }
    ]
  }

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Routes')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Routes test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44577')
    @pytest.mark.Routes
    @pytest.mark.POST
    def test_TC_44577_POST_Routes_Unable_To_Add_Same_Device_Multiple_Times(self, context):
        """TC-44577 - Routes-POST
           Verify that user is unable to add same device multiple times using post "/routes"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to add same device multiple times using post "/routes"."""):

            # Test case configuration
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[{
                    'hops': [],
                    'id': 3,
                    'member': {
                        'id': 'ZL-PFE-03',
                        'name': 'ZL-PFE-03'
                    },
                    'memberType': 'EDGE_DEVICE',
                    'selected': True,
                    'used': True,
                    'memberRoles': ['EDGE']
                },
                    {
                        'hops': [],
                        'id': 4,
                        'member': {
                            'id': 'ZL-PFE-03',
                            'name': 'ZL-PFE-03'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'selected': True,
                        'used': True,
                        'memberRoles': ['EDGE']
                    }
                ],
                id='route14',
                name='Route14',
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
            except (HTTPBadRequest, HTTPForbidden, HTTPConflict) as e:        # 400, 403, 409 error
                get_error_message(e) | expect.any(
                    should.start_with('Member ve_device:ZL-PFE-03 is in use, MemberType = EDGE_DEVICE')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
