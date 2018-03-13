# -*- coding: UTF-8 -*-

"""PFE Component Tests - Pathfinder_Edge_Device.

* TC-42625 - Pathfinder_Edge_Device DELETE:

  Verify that user is able to DELETE the VideoNetEdge device using request DELETE /devices/veDevices/{id}  .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veDevices/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veDevices/DELETE_device_POST"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Pathfinder_Edge_Device')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Pathfinder_Edge_Device test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42625')
    @pytest.mark.Pathfinder_Edge_Device
    @pytest.mark.DELETE
    def test_TC_42625_DELETE_Pathfinder_Edge_Device_Able_To_Delete_With_Valid_Id(self, context):
        """TC-42625 - Pathfinder_Edge_Device-DELETE
           Verify that user is able to DELETE the VideoNetEdge device using request DELETE /devices/veDevices/{id}  ."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to DELETE the VideoNetEdge device using request DELETE /devices/veDevices/{id}  ."""):

            ### Positive test example

            # deleteEntity the Pathfinder_Edge_Device.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Pathfinder_Edge_Device.deleteEntity(
                    id='DELETE_device_POST')
            )

        with pytest.allure.step("""Verify that user is able to DELETE the VideoNetEdge device using request DELETE /devices/veDevices/{id}  ."""):

            ### Negative test example

            # deleteEntity the Pathfinder_Edge_Device, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Pathfinder_Edge_Device.deleteEntity(
                        id='DELETE_device_POST'),
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
