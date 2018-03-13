# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-42552 - Routes GET:

  Verify that user with Manage Configuration permission is able to create "Authorization System" and "Origin", if "Config admin can create" is set to True in Configuration. .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes"

Same, with test data:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Routes')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Routes test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42552')
    @pytest.mark.Routes
    @pytest.mark.GET
    def test_TC_42552_GET_Routes_Admin_Create_Config_True(self, context):
        """TC-42552 - Routes-GET
           Verify that user with Manage Configuration permission is able to create "Authorization System" and "Origin", if "Config admin can create" is set to True in Configuration. ."""
        # Define a test step
        with pytest.allure.step("""Verify that user with Manage Configuration permission is able to create "Authorization System" and "Origin", if "Config admin can create" is set to True in Configuration. ."""):

            ### Positive test example

            # createEntity the Routes.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Routes.createEntity()
            )

        with pytest.allure.step("""Verify that user with Manage Configuration permission is able to create "Authorization System" and "Origin", if "Config admin can create" is set to True in Configuration. ."""):

            ### Negative test example

            # createEntity the Routes, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Routes.createEntity(),
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
