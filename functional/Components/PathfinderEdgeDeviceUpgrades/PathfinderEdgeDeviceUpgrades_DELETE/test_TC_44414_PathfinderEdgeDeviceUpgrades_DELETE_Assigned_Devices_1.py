# -*- coding: UTF-8 -*-

"""PFE Component Tests - Pathfinder_Edge_Device_Upgrades.

* TC-44414 - Pathfinder_Edge_Device_Upgrades DELETE:

  Verify that user is unable to get the details of Video Edge Device Upgrade assigned devices with invalid effectiveDate using request  POST "/devices/upgrades/{upgradeId}/assignedDevice".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/upgrades/64528488-400a-4066-af6a-a3cde7b1ed49"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/upgrades/64528488-400a-4066-af6a-a3cde7b1ed49"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Pathfinder_Edge_Device_Upgrades')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Pathfinder_Edge_Device_Upgrades test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44414')
    @pytest.mark.Pathfinder_Edge_Device_Upgrades
    @pytest.mark.DELETE
    def test_TC_44414_DELETE_Pathfinder_Edge_Device_Upgrades_Assigned_Devices(self, context):
        """TC-44414 - Pathfinder_Edge_Device_Upgrades-DELETE
           Verify that user is unable to get the details of Video Edge Device Upgrade assigned devices with invalid effectiveDate using request  POST "/devices/upgrades/{upgradeId}/assignedDevice"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to get the details of Video Edge Device Upgrade assigned devices with invalid effectiveDate using request  POST "/devices/upgrades/{upgradeId}/assignedDevice"."""):

            ### Positive test example

            # deleteUpdate the Pathfinder_Edge_Device_Upgrades.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Pathfinder_Edge_Device_Upgrades.deleteUpdate(
                    id='64528488-400a-4066-af6a-a3cde7b1ed49')
            )

        with pytest.allure.step("""Verify that user is unable to get the details of Video Edge Device Upgrade assigned devices with invalid effectiveDate using request  POST "/devices/upgrades/{upgradeId}/assignedDevice"."""):

            ### Negative test example

            # deleteUpdate the Pathfinder_Edge_Device_Upgrades, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Pathfinder_Edge_Device_Upgrades.deleteUpdate(
                        id='64528488-400a-4066-af6a-a3cde7b1ed49'),
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
