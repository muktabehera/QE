# -*- coding: UTF-8 -*-

"""PFE Component Tests - Pathfinder_Edge_Device_Upgrades.

* TC-44409 - Pathfinder_Edge_Device_Upgrades GET:

  Verify that user is able to GET the details of Video Edge Device Upgrade with upgradeID parameter using request "/devices/upgrades/{upgradeId}".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/upgrades/1233eda3-767d-4482-8948-9a412fef864e"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/upgrades/1233eda3-767d-4482-8948-9a412fef864e"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Pathfinder_Edge_Device_Upgrades')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Pathfinder_Edge_Device_Upgrades test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44409')
    @pytest.mark.Pathfinder_Edge_Device_Upgrades
    @pytest.mark.GET
    def test_TC_44409_GET_Pathfinder_Edge_Device_Upgrades_Get_Details_With_Upgrade_Id(self, context):
        """TC-44409 - Pathfinder_Edge_Device_Upgrades-GET
           Verify that user is able to GET the details of Video Edge Device Upgrade with upgradeID parameter using request "/devices/upgrades/{upgradeId}"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of Video Edge Device Upgrade with upgradeID parameter using request "/devices/upgrades/{upgradeId}"."""):

            ### Positive test example

            # viewUpdate the Pathfinder_Edge_Device_Upgrades.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Pathfinder_Edge_Device_Upgrades.viewUpdate(
                    id='1233eda3-767d-4482-8948-9a412fef864e')
            )

        with pytest.allure.step("""Verify that user is able to GET the details of Video Edge Device Upgrade with upgradeID parameter using request "/devices/upgrades/{upgradeId}"."""):

            ### Negative test example

            # viewUpdate the Pathfinder_Edge_Device_Upgrades, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Pathfinder_Edge_Device_Upgrades.viewUpdate(
                        id='1233eda3-767d-4482-8948-9a412fef864e'),
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
