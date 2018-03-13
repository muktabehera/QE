# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-42569 - Groups DELETE:

  Verify that user is able to Edit/Delete all the entities under "VideoNet Configuration" with "Manage Configuration" permission while "Configuration admin can edit" and "Configuration admin can create" flags are set to true within token expiration time.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups/autoDeleteGroup"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Groups')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Groups test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42569')
    @pytest.mark.Groups
    @pytest.mark.DELETE
    def test_TC_42569_DELETE_Groups_Id(self, context):
        """TC-42569 - Groups-DELETE
           Verify that user is able to Edit/Delete all the entities under "VideoNet Configuration" with "Manage Configuration" permission while "Configuration admin can edit" and "Configuration admin can create" flags are set to true within token expiration time."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to Edit/Delete all the entities under "VideoNet Configuration" with "Manage Configuration" permission while "Configuration admin can edit" and "Configuration admin can create" flags are set to true within token expiration time."""):

            ### Positive test example

            # deleteEntity the Groups.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Groups.deleteEntity(
                    id='autoDeleteGroup')
            )

        with pytest.allure.step("""Verify that user is able to Edit/Delete all the entities under "VideoNet Configuration" with "Manage Configuration" permission while "Configuration admin can edit" and "Configuration admin can create" flags are set to true within token expiration time."""):

            ### Negative test example

            # deleteEntity the Groups, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Groups.deleteEntity(
                        id='autoDeleteGroup'),
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
