# -*- coding: UTF-8 -*-

"""PFE Component Tests - Broadcasts.

* TC-44769 - Broadcasts GET:

  Verify that User is unable to get the details of another broadcast "Broad" while Token is generated for the corresponding URL with Provision permission.


Equivalent test CURL command:

  curl -k -H "Host: <client_host>" -H "Authorization: Bearer
       <valid_token>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/broadcasts"

Same, with test data:

  curl -k -H "Host: <client_host>" -H "Authorization: Bearer
       <valid_token>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/broadcasts"

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44769')
    @pytest.mark.Broadcasts
    @pytest.mark.GET
    def test_TC_44769_GET_Broadcasts_Unableto_Get_Broadcast_Details(self, context):
        """TC-44769 - Broadcasts-GET
           Verify that User is unable to get the details of another broadcast "Broad" while Token is generated for the corresponding URL with Provision permission."""
        # Define a test step
        with pytest.allure.step("""Verify that User is unable to get the details of another broadcast "Broad" while Token is generated for the corresponding URL with Provision permission."""):

            ### Positive test example

            # listEntities the Broadcasts.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Broadcasts.listEntities()
            )

        with pytest.allure.step("""Verify that User is unable to get the details of another broadcast "Broad" while Token is generated for the corresponding URL with Provision permission."""):

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
