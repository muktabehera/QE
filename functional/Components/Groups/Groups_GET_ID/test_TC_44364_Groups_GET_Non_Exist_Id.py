# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-44364 - Groups GET:

  Verify that error message is displayed on providing non existing 'Id' in 'Id' parameter using request GET /groups{id}.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups/groupNonExist"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups/groupNonExist"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Groups')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Groups test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44364')
    @pytest.mark.Groups
    @pytest.mark.GET
    def test_TC_44364_GET_Groups_Non_Exist_Id(self, context):
        """TC-44364 - Groups-GET
           Verify that error message is displayed on providing non existing 'Id' in 'Id' parameter using request GET /groups{id}."""
        # Define a test step
        with pytest.allure.step("""Verify that error message is displayed on providing non existing 'Id' in 'Id' parameter using request GET /groups{id}."""):

            # getEntity the Groups, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Groups.getEntity(
                        id='wrong'
                    ),
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden, HTTPNotFound) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Delivery Service entity not found')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
