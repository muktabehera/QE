# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audiences.

* TC-43015 - Audiences GET:

  Verify that user is unable to GET the details of Audience Request "/audiences/{id}  using incorrect token.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <invalid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <invalid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences/POST_GETID"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Audiences')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Audiences test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43015')
    @pytest.mark.Audiences
    @pytest.mark.GET
    def test_TC_43015_GET_Audiences_Audience_Incorrect_Token(self, context):
        """TC-43015 - Audiences-GET
           Verify that user is unable to GET the details of Audience Request "/audiences/{id}  using incorrect token."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to GET the details of Audience Request "/audiences/{id}  using incorrect token."""):

            # getEntity the Audiences, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Audiences.getEntity(
                        id='POST_GETID'),
                    token='invalid_token',
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Invalid Authorization Token')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
