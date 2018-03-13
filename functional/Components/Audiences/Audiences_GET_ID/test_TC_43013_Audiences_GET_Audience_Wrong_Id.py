# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audiences.

* TC-43013 - Audiences GET:

  Verify that user is unable to GET the details of Audience using request /audiences/{id}  using wrong/deleted ID.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences/Invalid"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences/Invalid"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Audiences')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Audiences test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43013')
    @pytest.mark.Audiences
    @pytest.mark.GET
    def test_TC_43013_GET_Audiences_Audience_Wrong_Id(self, context):
        """TC-43013 - Audiences-GET
           Verify that user is unable to GET the details of Audience using request /audiences/{id}  using wrong/deleted ID."""
        # Define a test step

        with pytest.allure.step("""Verify that user is unable to GET the details of Audience using request /audiences/{id}  using wrong/deleted ID."""):



            # getEntity the Audiences, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Audiences.getEntity(id='wrongPOST_GETID'),
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden, HTTPNotFound) as e:        # 400, 403, 404 error
                get_error_message(e) | expect.any(
                    should.start_with('Delivery Service entity not found')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
