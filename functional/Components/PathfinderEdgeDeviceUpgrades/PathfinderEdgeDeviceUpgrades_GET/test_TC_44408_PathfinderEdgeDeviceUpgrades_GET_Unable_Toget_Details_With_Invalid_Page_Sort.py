# -*- coding: UTF-8 -*-

"""PFE Component Tests - Pathfinder_Edge_Device_Upgrades.

* TC-44408 - Pathfinder_Edge_Device_Upgrades GET:

  Verify that user is unable to GET the details of Video Edge Device Upgrade with invalid value of  "sort" & "page"  parameter using request "/devices/upgrades".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/upgrades?sort=asdsdsd
       &page=asdasdsa"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/upgrades?sort=asdsdsd
       &page=asdasdsa"

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44408')
    @pytest.mark.Pathfinder_Edge_Device_Upgrades
    @pytest.mark.GET
    def test_TC_44408_GET_Pathfinder_Edge_Device_Upgrades_Unable_Toget_Details_With_Invalid_Page_Sort(self, context):
        """TC-44408 - Pathfinder_Edge_Device_Upgrades-GET
           Verify that user is unable to GET the details of Video Edge Device Upgrade with invalid value of  "sort" & "page"  parameter using request "/devices/upgrades"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to GET the details of Video Edge Device Upgrade with invalid value of  "sort" & "page"  parameter using request "/devices/upgrades"."""):

            ### Positive test example

            # listAll the Pathfinder_Edge_Device_Upgrades.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Pathfinder_Edge_Device_Upgrades.listAll(
                    sort='asdsdsd', 
                    page='asdasdsa'
                )
            )

        with pytest.allure.step("""Verify that user is unable to GET the details of Video Edge Device Upgrade with invalid value of  "sort" & "page"  parameter using request "/devices/upgrades"."""):

            ### Negative test example

            # listAll the Pathfinder_Edge_Device_Upgrades, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Pathfinder_Edge_Device_Upgrades.listAll(
                        sort='asdsdsd', 
                        page='asdasdsa'
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
