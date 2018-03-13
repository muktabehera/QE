# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44056 - Routes GET:

  Verify that user is able to GET the details of route devices with "routeId" parameter using request  "/routes/possibleMembers".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/possibleMembers?routeId=Alpha1_test_Route"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/possibleMembers?routeId=Alpha1_test_Route"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Routes')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Routes test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44056')
    @pytest.mark.Routes
    @pytest.mark.GET
    def test_TC_44056_GET_Routes_Route_Id(self, context):
        """TC-44056 - Routes-GET
           Verify that user is able to GET the details of route devices with "routeId" parameter using request  "/routes/possibleMembers"."""
        # Define a test step
        with pytest.allure.step("""Create route using request POST "/routes"."""):
            # Test case configuration
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[],
                id='route21',
                name='Route21',
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
        with pytest.allure.step("""Now verify that user is able to GET the details of route devices with "routeId" parameter using request  "/routes/possibleMembers"."""):

            # possibleMembers the Routes.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Routes.possibleMembers(
                    routeId='route21')
            )

