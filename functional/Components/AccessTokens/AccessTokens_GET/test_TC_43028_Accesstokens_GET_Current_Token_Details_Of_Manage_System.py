# -*- coding: UTF-8 -*-

"""PFE Component Tests - Access_Tokens.

* TC-43028 - Access_Tokens GET:

  Verify that user is able to GET current token details of Manage System using  "/accessTokens/currentTokenDetails".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/accessTokens/currentTokenDetails"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/accessTokens/currentTokenDetails"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Access_Tokens')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Access_Tokens test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43028')
    @pytest.mark.Access_Tokens
    @pytest.mark.GET
    def test_TC_43028_GET_Access_Tokens_Current_Token_Details_Of_Manage_System(self, context):
        """TC-43028 - Access_Tokens-GET
           Verify that user is able to GET current token details of Manage System using  "/accessTokens/currentTokenDetails"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET current token details of Manage System using  "/accessTokens/currentTokenDetails"."""):

            # getEntity the Access_Tokens.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Access_Tokens.getEntity()
            )

