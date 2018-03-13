# -*- coding: UTF-8 -*-

"""PFE Component Tests - Authorization_Systems.

* TC-43270 - Authorization_Systems GET:

  Verify that user is able to GET the details of Authorization system request /authorizationSystems  with showAll=False value.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       <PF_host>://<client_host>/authorizationSystems?showAll=false

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       <PF_host>://<client_host>/authorizationSystems?showAll=false

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Authorization_Systems')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Authorization_Systems test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43270')
    @pytest.mark.Authorization_Systems
    @pytest.mark.GET
    def test_TC_43270_GET_Authorization_Systems_Show_All_False_Value(self, context):
        """TC-43270 - Authorization_Systems-GET
           Verify that user is able to GET the details of Authorization system request /authorizationSystems  with showAll=False value."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of Authorization system request /authorizationSystems  with showAll=False value."""):

            ### Positive test example

            # listEntities the Authorization_Systems.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Authorization_Systems.listEntities(
                    showAll='false')
            )
