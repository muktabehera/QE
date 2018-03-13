# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44103 - Routes DELETE:

  Verify that user is able to DELETE the route using request "/routes/{id}".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/del"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/del"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Routes')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Routes test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44103')
    @pytest.mark.Routes
    @pytest.mark.DELETE
    def test_TC_44103_DELETE_Routes_Id(self, context):
        """TC-44103 - Routes-DELETE
           Verify that user is able to DELETE the route using request "/routes/{id}"."""
        # Define a test step
        with pytest.allure.step("""First reate route using request POST "/routes"."""):
            # Test case configuration
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[],
                id='route27',
                name='Route27',
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
        with pytest.allure.step("""Now verify that user is able to DELETE the route using request "/routes/{id}"."""):

            # createHop the Routes.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Routes.deleteEntity(
                    id='route27'
                )
            )

