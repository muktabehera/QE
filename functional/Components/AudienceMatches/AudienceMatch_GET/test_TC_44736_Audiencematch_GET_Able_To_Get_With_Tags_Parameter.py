# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audience_Match.

* TC-44736 - Audience_Match GET:

  Verify the user is able to get the results for audience match by passing tags parameter using request GET /audienceMatch.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audienceMatch?tags=abc:abc"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audienceMatch?tags=abc:abc"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Audience_Match')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Audience_Match test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44736')
    @pytest.mark.Audience_Match
    @pytest.mark.GET
    def test_TC_44736_GET_Audience_Match_Able_To_Get_With_Tags_Parameter(self, context):
        """TC-44736 - Audience_Match-GET
           Verify the user is able to get the results for audience match by passing tags parameter using request GET /audienceMatch."""
        # Define a test step
        with pytest.allure.step("""Verify the user is able to get the results for audience match by passing tags parameter using request GET /audienceMatch."""):

            ### Positive test example

            # audienceMatchGet the Audience_Match.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Audience_Match.audienceMatchGet(
                    tags='abc:abc')
            )

        with pytest.allure.step("""Verify the user is able to get the results for audience match by passing tags parameter using request GET /audienceMatch."""):

            ### Negative test example

            # audienceMatchGet the Audience_Match, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Audience_Match.audienceMatchGet(
                        tags='abc:abc'),
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
