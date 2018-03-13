# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44052 - Routes GET:

  Verify that user is able to GET the details of route devices without any parameters using request "/routes/possibleMembers".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/possibleMembers"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/possibleMembers"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Routes')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Routes test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44052')
    @pytest.mark.Routes
    @pytest.mark.GET
    def test_TC_44052_GET_Routes_Without_Parameters(self, context):
        """TC-44052 - Routes-GET
           Verify that user is able to GET the details of route devices without any parameters using request "/routes/possibleMembers"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of route devices without any parameters using request "/routes/possibleMembers"."""):

            # possibleMembers the Routes.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Routes.possibleMembers()
            )
