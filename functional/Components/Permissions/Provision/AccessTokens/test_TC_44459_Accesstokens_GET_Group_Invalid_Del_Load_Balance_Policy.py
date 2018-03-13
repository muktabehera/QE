# -*- coding: UTF-8 -*-

"""PFE Component Tests - Access_Tokens.

* TC-44459 - Access_Tokens GET:

  Verify that user is unable to create group on providing invalid values in parameter 'deliveryLoadBalancePolicy' using request POST '/groups'.


Equivalent test CURL command:

  curl -k -H "Host: <client_host>" -H "Authorization: Bearer
       <valid_token>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/accessTokens/currentTokenDetails"

Same, with test data:

  curl -k -H "Host: <client_host>" -H "Authorization: Bearer
       <valid_token>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/accessTokens/currentTokenDetails"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Access_Tokens')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Access_Tokens test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44459')
    @pytest.mark.Access_Tokens
    @pytest.mark.GET
    def test_TC_44459_GET_Access_Tokens_Group_Invalid_Del_Load_Balance_Policy(self, context):
        """TC-44459 - Access_Tokens-GET
           Verify that user is unable to create group on providing invalid values in parameter 'deliveryLoadBalancePolicy' using request POST '/groups'."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to create group on providing invalid values in parameter 'deliveryLoadBalancePolicy' using request POST '/groups'."""):

            ### Positive test example

            # getEntity the Access_Tokens.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Access_Tokens.getEntity()
            )

        with pytest.allure.step("""Verify that user is unable to create group on providing invalid values in parameter 'deliveryLoadBalancePolicy' using request POST '/groups'."""):

            ### Negative test example

            # getEntity the Access_Tokens, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Access_Tokens.getEntity(),
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
