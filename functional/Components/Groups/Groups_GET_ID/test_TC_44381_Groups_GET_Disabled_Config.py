# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-44381 - Groups GET:

  Verify that user is unable to get the details of disabled 'Configurations' using request GET /groups{id}.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups/config_Empty"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups/config_Empty"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Groups')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Groups test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44381')
    @pytest.mark.Groups
    @pytest.mark.GET
    def test_TC_44381_GET_Groups_Disabled_Config(self, context):
        """TC-44381 - Groups-GET
           Verify that user is unable to get the details of disabled 'Configurations' using request GET /groups{id}."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to get the details of disabled 'Configurations' using request GET /groups{id}."""):

            ### Positive test example

            # getEntity the Groups.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Groups.getEntity()
            )

        with pytest.allure.step("""Verify that user is unable to get the details of disabled 'Configurations' using request GET /groups{id}."""):

            ### Negative test example

            # getEntity the Groups, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Groups.getEntity(),
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
