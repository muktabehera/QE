# -*- coding: UTF-8 -*-

"""PFE Component Tests - Pathfinder_Edge_Device.

* TC-45313 - Pathfinder_Edge_Device GET:

  Verify User is able to GET the alerts by passing page parameter using request GET /devices/veDevices/{id}/alerts .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veDevices/<data_ID1_under_test>/alerts?page=0;1"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veDevices/Linux_172.30.3.131/alerts?page=0;1"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Pathfinder_Edge_Device')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Pathfinder_Edge_Device test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-45313')
    @pytest.mark.Pathfinder_Edge_Device
    @pytest.mark.GET
    def test_TC_45313_GET_Pathfinder_Edge_Device_Able_To_Get_Alerts_With_Valid_Page_Parameter(self, context):
        """TC-45313 - Pathfinder_Edge_Device-GET
           Verify User is able to GET the alerts by passing page parameter using request GET /devices/veDevices/{id}/alerts ."""
        # Define a test step
        with pytest.allure.step("""Verify User is able to GET the alerts by passing page parameter using request GET /devices/veDevices/{id}/alerts ."""):

            ### Positive test example

            # getEntitis the Pathfinder_Edge_Device.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Pathfinder_Edge_Device.getEntitis(
                    id='Linux_172.30.3.131', 
                    page='0;1'
                )
            )

        with pytest.allure.step("""Verify User is able to GET the alerts by passing page parameter using request GET /devices/veDevices/{id}/alerts ."""):

            ### Negative test example

            # getEntitis the Pathfinder_Edge_Device, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Pathfinder_Edge_Device.getEntitis(
                        id='Linux_172.30.3.131', 
                        page='0;1'
                    ),
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
