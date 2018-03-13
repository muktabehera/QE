# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audiences.

* TC-42284 - Audiences GET:

  Verify that Create button is not displayed on 'Proximities zones' page under Intelligent Content Routing menu for user with "Manage Configuration" permission, while "Config admin can create" flag is set to false within the token expiration time.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences"

Same, with test data:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Audiences')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Audiences test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42284')
    @pytest.mark.Audiences
    @pytest.mark.GET
    def test_TC_42284_GET_Audiences_Admin_Create_Flag_Set_To_False(self, context):
        """TC-42284 - Audiences-GET
           Verify that Create button is not displayed on 'Proximities zones' page under Intelligent Content Routing menu for user with "Manage Configuration" permission, while "Config admin can create" flag is set to false within the token expiration time."""
        # Define a test step
        with pytest.allure.step("""Verify that Create button is not displayed on 'Proximities zones' page under Intelligent Content Routing menu for user with "Manage Configuration" permission, while "Config admin can create" flag is set to false within the token expiration time."""):

            ### Positive test example

            # listEntities the Audiences.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Audiences.listEntities()
            )

        with pytest.allure.step("""Verify that Create button is not displayed on 'Proximities zones' page under Intelligent Content Routing menu for user with "Manage Configuration" permission, while "Config admin can create" flag is set to false within the token expiration time."""):

            ### Negative test example

            # listEntities the Audiences, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Audiences.listEntities(),
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
