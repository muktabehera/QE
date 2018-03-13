# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-42565 - Groups GET:

  Verify that User is able to View, all the entities under "VideoNet Configuration" menu, using token with "Manage Configuration" permission within the token expiration time.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups"

Same, with test data:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups"

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42565')
    @pytest.mark.Groups
    @pytest.mark.GET
    def test_TC_42565_GET_Groups_Id(self, context):
        """TC-42565 - Groups-GET
           Verify that User is able to View, all the entities under "VideoNet Configuration" menu, using token with "Manage Configuration" permission within the token expiration time."""
        # Define a test step
        with pytest.allure.step("""Verify that User is able to View, all the entities under "VideoNet Configuration" menu, using token with "Manage Configuration" permission within the token expiration time."""):

            ### Positive test example

            # getEntity the Groups.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Groups.getEntity()
            )

        with pytest.allure.step("""Verify that User is able to View, all the entities under "VideoNet Configuration" menu, using token with "Manage Configuration" permission within the token expiration time."""):

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
