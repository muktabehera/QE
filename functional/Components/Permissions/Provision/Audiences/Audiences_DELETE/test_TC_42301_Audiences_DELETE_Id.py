# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audiences.

* TC-42301 - Audiences DELETE:

  Verify that User is unable to Create/Edit/View/Delete, any entity on any page of the QED, using token with "Provision" permission within the token expiration time.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences/Delete_Audience"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Audiences')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Audiences test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42301')
    @pytest.mark.Audiences
    @pytest.mark.DELETE
    def test_TC_42301_DELETE_Audiences_Id(self, context):
        """TC-42301 - Audiences-DELETE
           Verify that User is unable to Create/Edit/View/Delete, any entity on any page of the QED, using token with "Provision" permission within the token expiration time."""
        # Define a test step
        with pytest.allure.step("""Verify that User is unable to Create/Edit/View/Delete, any entity on any page of the QED, using token with "Provision" permission within the token expiration time."""):

            ### Positive test example

            # deleteEntity the Audiences.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Audiences.deleteEntity(
                    id='Delete_Audience')
            )

        with pytest.allure.step("""Verify that User is unable to Create/Edit/View/Delete, any entity on any page of the QED, using token with "Provision" permission within the token expiration time."""):

            ### Negative test example

            # deleteEntity the Audiences, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Audiences.deleteEntity(
                        id='Delete_Audience'),
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
