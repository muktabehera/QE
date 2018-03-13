# -*- coding: UTF-8 -*-

"""PFE Component Tests - Broadcasts.

* TC-44483 - Broadcasts PATCH:

  Verify that appropriate message is displayed if broadcasts failed for live program using request POST  "/broadcasts/{id}".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/broadcasts/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/broadcasts/Broadcast_StandaloneVNE"

JSON data sent to PathFinder in this test:

  {'status': 'Start'}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Broadcasts')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Broadcasts test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44483')
    @pytest.mark.Broadcasts
    @pytest.mark.PATCH
    def test_TC_44483_PATCH_Broadcasts_Verify_Correct_Message_Displayed_When_Broadcast_Failed_To_Start(self, context):
        """TC-44483 - Broadcasts-PATCH
           Verify that appropriate message is displayed if broadcasts failed for live program using request POST  "/broadcasts/{id}"."""
        # Define a test step
        with pytest.allure.step("""Verify that appropriate message is displayed if broadcasts failed for live program using request POST  "/broadcasts/{id}"."""):

            ### Positive test example

            # Test case configuration
            broadcastStatusUpdate = context.sc.BroadcastStatusUpdate(status='Start')


            # updateEntity the Broadcasts.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Broadcasts.updateEntity(
                    body=broadcastStatusUpdate, 
                    id='Broadcast_StandaloneVNE'
                
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that appropriate message is displayed if broadcasts failed for live program using request POST  "/broadcasts/{id}"."""):

            ### Negative test example

            # Test case configuration
            broadcastStatusUpdate = context.sc.BroadcastStatusUpdate(status='Start')


            # prepare the request, so we can modify it
            request = context.cl.Broadcasts.updateEntity(
                    body=broadcastStatusUpdate, 
                    id='Broadcast_StandaloneVNE'
                
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateEntity the Broadcasts, and check we got the error we expect
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
