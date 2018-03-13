# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audiences.

* TC-43011 - Audiences GET:

  Verify that user is unable to GET the details of Audience request /audiences  with invalid Token.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer
       <data_ID1_under_test>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer
       eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJkZWZhdWx0Iiwic3ViIjoiYWRtaW5AMTcyLjMwLjIuMTQ5OjgwODAuY29tIiwiYXVkIjoicWVkOmRlZmF1bHQiLCJxZWRwIjpbInMiLCJjIiwiZyIsInAiLCJkIiwibSIsImEiXX0.uh1W0Hs2nemsjiRFRSiyiZgo4io5bUmmCSJqrjfjfehff"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Audiences')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Audiences test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43011')
    @pytest.mark.Audiences
    @pytest.mark.GET
    def test_TC_43011_GET_Audiences_Invalid_Token(self, context):
        """TC-43011 - Audiences-GET
           Verify that user is unable to GET the details of Audience request /audiences  with invalid Token."""
        # Define a test step

        with pytest.allure.step("""Verify that user is unable to GET the details of Audience request /audiences  with invalid Token."""):

            # listEntities the Audiences, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Audiences.listEntities(),
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
