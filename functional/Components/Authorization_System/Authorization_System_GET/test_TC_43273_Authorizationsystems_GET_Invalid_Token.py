# -*- coding: UTF-8 -*-

"""PFE Component Tests - Authorization_Systems.

* TC-43273 - Authorization_Systems GET:

  Verify that user is unable to GET the details of Authorization system request /authorizationSystems  with invalid token.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer
       gqaiudoqwhwohasdfasfafsdfuqeoiqwojheohqwoie" -X GET -H "Content-
       Type: application/json"
       <PF_host>://<client_host>/authorizationSystems?prefix=de

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer
       gqaiudoqwhwohasdfasfafsdfuqeoiqwojheohqwoie" -X GET -H "Content-
       Type: application/json"
       <PF_host>://<client_host>/authorizationSystems?prefix=de

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Authorization_Systems')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Authorization_Systems test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43273')
    @pytest.mark.Authorization_Systems
    @pytest.mark.GET
    def test_TC_43273_GET_Authorization_Systems_Invalid_Token(self, context):
        """TC-43273 - Authorization_Systems-GET
           Verify that user is unable to GET the details of Authorization system request /authorizationSystems  with invalid token."""
        # Define a test step

        with pytest.allure.step("""Verify that user is unable to GET the details of Authorization system request /authorizationSystems  with invalid token."""):


            # listEntities the Authorization_Systems, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Authorization_Systems.listEntities(
                        prefix='d'),
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
