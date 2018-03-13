# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audiences.

* TC-43159 - Audiences DELETE:

  Verify that error message is displayed on providing invalid value for 'id' parameter using request DELETE audiences/{id} .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences/123"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences/123"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Audiences')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Audiences test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43159')
    @pytest.mark.Audiences
    @pytest.mark.DELETE
    def test_TC_43159_DELETE_Audiences_Invalid_Id(self, context):
        """TC-43159 - Audiences-DELETE
           Verify that error message is displayed on providing invalid value for 'id' parameter using request DELETE audiences/{id} ."""
        # Define a test step


        with pytest.allure.step("""Verify that error message is displayed on providing invalid value for 'id' parameter using request DELETE audiences/{id} ."""):


            # deleteEntity the Audiences, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Audiences.deleteEntity(id='Delete_Audience123'),
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden, HTTPNotFound) as e:        # 400, 403, 404 error
                get_error_message(e) | expect.any(
                    should.start_with('Delivery Service entity not found'),
                    should.start_with('Invalid entity')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
