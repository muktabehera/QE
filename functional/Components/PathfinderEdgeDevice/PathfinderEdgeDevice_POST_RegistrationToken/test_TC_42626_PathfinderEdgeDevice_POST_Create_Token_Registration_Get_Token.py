# -*- coding: UTF-8 -*-

"""PFE Component Tests - Pathfinder_Edge_Device.

* TC-42626 - Pathfinder_Edge_Device POST:

  Verify that user is able to GET the VideoNetEdge device Registration token using POST /devices/veDevices/{id}/createRegistrationToken  .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veDevices/<data_ID1_under_test>/createRegistrationToken"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veDevices/VNE_172.30.4.168/createRegistrationToken"

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42626')
    @pytest.mark.Pathfinder_Edge_Device
    @pytest.mark.POST
    def test_TC_42626_POST_Pathfinder_Edge_Device_Create_Token_Registration_Get_Token(self, context):
        """TC-42626 - Pathfinder_Edge_Device-POST
           Verify that user is able to GET the VideoNetEdge device Registration token using POST /devices/veDevices/{id}/createRegistrationToken  ."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the VideoNetEdge device Registration token using POST /devices/veDevices/{id}/createRegistrationToken  ."""):

            ### Positive test example

            # getRegistrationToken the Pathfinder_Edge_Device.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Pathfinder_Edge_Device.getRegistrationToken(
                    id='VNE_172.30.4.168')
            )

        with pytest.allure.step("""Verify that user is able to GET the VideoNetEdge device Registration token using POST /devices/veDevices/{id}/createRegistrationToken  ."""):

            ### Negative test example

            # getRegistrationToken the Pathfinder_Edge_Device, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Pathfinder_Edge_Device.getRegistrationToken(
                        id='VNE_172.30.4.168'),
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
