# -*- coding: UTF-8 -*-

"""PFE Component Tests - Authorization_Systems.

* TC-43365 - Authorization_Systems GET:

  Verify that error message is displayed on providing 'page-size' value as 0 for 'page' parameter using request GET /authorizationSystems.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       <PF_host>://<client_host>/authorizationSystems?page=0

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       <PF_host>://<client_host>/authorizationSystems?page=0

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Authorization_Systems')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Authorization_Systems test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43365')
    @pytest.mark.Authorization_Systems
    @pytest.mark.GET
    def test_TC_43365_GET_Authorization_Systems_Page_Size_0(self, context):
        """TC-43365 - Authorization_Systems-GET
           Verify that error message is displayed on providing 'page-size' value as 0 for 'page' parameter using request GET /authorizationSystems."""
        # Define a test step
        with pytest.allure.step("""Verify that error message is not displayed on providing 'page-size' value as 0 for 'page' parameter using request GET /authorizationSystems. Instead max 20 records is displayed on providing 'page-size' value as 0 for 'page' parameter """):

            # listEntities the Authorization_Systems.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Authorization_Systems.listEntities(page='1;0')
            )
