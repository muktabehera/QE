# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audience_Match.

* TC-44452 - Audience_Match GET:

  Verify user is able to fetch the details of audience match without passing parameters using GET /audienceMatch.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audienceMatch"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audienceMatch"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Audience_Match')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Audience_Match test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44452')
    @pytest.mark.Audience_Match
    @pytest.mark.GET
    def test_TC_44452_GET_Audience_Match_Get_Details_Without_Passing_Parameters(self, context):
        """TC-44452 - Audience_Match-GET
           Verify user is able to fetch the details of audience match without passing parameters using GET /audienceMatch."""
        # Define a test step
        with pytest.allure.step("""Verify user is able to fetch the details of audience match without passing parameters using GET /audienceMatch."""):

            # audienceMatchGet the Audience_Match.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Audience_Match.audienceMatchGet()
            )

