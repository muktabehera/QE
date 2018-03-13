# -*- coding: UTF-8 -*-

"""PFE Component Tests - Broadcasts.

* TC-42299 - Broadcasts GET:

  Verify that User is unable to View the Broadcast corresponding to the other Configuration, using token with "Provision" permission within the token expiration time.


Equivalent test CURL command:

  curl -k -H "Host: <client_host>" -H "Authorization: Bearer
       <valid_token>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/broadcasts/configbroad1"

Same, with test data:

  curl -k -H "Host: <client_host>" -H "Authorization: Bearer
       <valid_token>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/broadcasts/configbroad1"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Broadcasts')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Broadcasts test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42299')
    @pytest.mark.Broadcasts
    @pytest.mark.GET
    def test_TC_42299_GET_Broadcasts_Diff_Config(self, context):
        """TC-42299 - Broadcasts-GET
           Verify that User is unable to View the Broadcast corresponding to the other Configuration, using token with "Provision" permission within the token expiration time."""
        # Define a test step
        with pytest.allure.step("""Verify that User is unable to View the Broadcast corresponding to the other Configuration, using token with "Provision" permission within the token expiration time."""):

            ### Positive test example

            # listEntities the Broadcasts.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Broadcasts.listEntities()
            )

        with pytest.allure.step("""Verify that User is unable to View the Broadcast corresponding to the other Configuration, using token with "Provision" permission within the token expiration time."""):

            ### Negative test example

            # listEntities the Broadcasts, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Broadcasts.listEntities(),
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
