# -*- coding: UTF-8 -*-

"""PFE Component Tests - Pathfinder_Edge_Device.

* TC-42628 - Pathfinder_Edge_Device POST:

  Verify that user is unable to GET the VideoEdge device registration token using request  /devices/veDevices/{id}/createRegistrationToken  with wrong device ID.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veDevices/dnsknd/createRegistrationToken"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veDevices/dnsknd/createRegistrationToken"

JSON data sent to PathFinder in this test:

  {}

  ### ==>> Please double-check test plan for required test data.

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Pathfinder_Edge_Device')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Pathfinder_Edge_Device test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42628')
    @pytest.mark.Pathfinder_Edge_Device
    @pytest.mark.POST
    def test_TC_42628_POST_Pathfinder_Edge_Device_Unable_To_Get_With_Wrong_Device_Id(self, context):
        """TC-42628 - Pathfinder_Edge_Device-POST
           Verify that user is unable to GET the VideoEdge device registration token using request  /devices/veDevices/{id}/createRegistrationToken  with wrong device ID."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to GET the VideoEdge device registration token using request  /devices/veDevices/{id}/createRegistrationToken  with wrong device ID."""):

            ### Positive test example

            # Test case configuration
            emptyDetails = context.sc.EmptyDetails()


            # getRegistrationToken the Pathfinder_Edge_Device.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Pathfinder_Edge_Device.getRegistrationToken(
                    body=emptyDetails, 
                    id='dnsknd'
                
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is unable to GET the VideoEdge device registration token using request  /devices/veDevices/{id}/createRegistrationToken  with wrong device ID."""):

            ### Negative test example

            # Test case configuration
            emptyDetails = context.sc.EmptyDetails()


            # prepare the request, so we can modify it
            request = context.cl.Pathfinder_Edge_Device.getRegistrationToken(
                    body=emptyDetails, 
                    id='dnsknd'
                
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # getRegistrationToken the Pathfinder_Edge_Device, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('may not be empty'),
                    should.start_with('Invalid page parameter specified'),
                    should.contain('Invalid Authorization Token')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
