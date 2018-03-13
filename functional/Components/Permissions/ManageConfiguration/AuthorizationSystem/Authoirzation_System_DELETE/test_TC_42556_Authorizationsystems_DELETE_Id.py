# -*- coding: UTF-8 -*-

"""PFE Component Tests - Authorization_Systems.

* TC-42556 - Authorization_Systems DELETE:

  Verify that user with Manage Configuration permission is able to delete entities on "System Configuration" pages  if "Config admin can create" is True in Configuration and "Configuration admin can edit" is true in the entity. .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/authorizationSystems/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/authorizationSystems/Delete_authorizationSystem"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Authorization_Systems')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Authorization_Systems test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42556')
    @pytest.mark.Authorization_Systems
    @pytest.mark.DELETE
    def test_TC_42556_DELETE_Authorization_Systems_Id(self, context):
        """TC-42556 - Authorization_Systems-DELETE
           Verify that user with Manage Configuration permission is able to delete entities on "System Configuration" pages  if "Config admin can create" is True in Configuration and "Configuration admin can edit" is true in the entity. ."""
        # Define a test step
        with pytest.allure.step("""Verify that user with Manage Configuration permission is able to delete entities on "System Configuration" pages  if "Config admin can create" is True in Configuration and "Configuration admin can edit" is true in the entity. ."""):

            ### Positive test example

            # deleteEntity the Authorization_Systems.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Authorization_Systems.deleteEntity(
                    id='Delete_authorizationSystem')
            )

        with pytest.allure.step("""Verify that user with Manage Configuration permission is able to delete entities on "System Configuration" pages  if "Config admin can create" is True in Configuration and "Configuration admin can edit" is true in the entity. ."""):

            ### Negative test example

            # deleteEntity the Authorization_Systems, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Authorization_Systems.deleteEntity(
                        id='Delete_authorizationSystem'),
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
