# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44101 - Routes GET:

  Verify that user is able to GET the details of route with id" parameter using request "/routes/{id}".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/BSRoute1"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/BSRoute1"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Routes')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Routes test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44101')
    @pytest.mark.Routes
    @pytest.mark.GET
    def test_TC_44101_GET_Routes_Details_With_Id(self, context):
        """TC-44101 - Routes-GET
           Verify that user is able to GET the details of route with id" parameter using request "/routes/{id}"."""
        # Define a test step
        with pytest.allure.step("""First Create route using request POST "/routes"."""):
            # Test case configuration
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[],
                id='route22',
                name='Route22',
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
        with pytest.allure.step("""Verify that user is able to GET the details of route with id" parameter using request "/routes/{id}"."""):

            # listEntities the Routes.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Routes.getEntity(
                    id='route22'
                )
            )
