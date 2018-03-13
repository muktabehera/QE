# -*- coding: UTF-8 -*-

"""PFE Component Tests - Authorization_Systems.

* TC-43345 - Authorization_Systems DELETE:

  Verify that user is unable to delete the Authorization system using request DELETE authorizationSystems/{id}  with 'id' parameter having invalid token.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer
       2903871290389012890wjhdijhIJSHxdijhgeyaHDKJHIASGHDIUAWDSIUY98YQW89EY9QWDJASBDG"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/authorizationSystems/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer
       2903871290389012890wjhdijhIJSHxdijhgeyaHDKJHIASGHDIUAWDSIUY98YQW89EY9QWDJASBDG"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/authorizationSystems/Delete_authorizationSystem_testdata"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Authorization_Systems')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Authorization_Systems test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43345')
    @pytest.mark.Authorization_Systems
    @pytest.mark.DELETE
    def test_TC_43345_DELETE_Authorization_Systems_Invalid_Token(self, context):
        """TC-43345 - Authorization_Systems-DELETE
           Verify that user is unable to delete the Authorization system using request DELETE authorizationSystems/{id}  with 'id' parameter having invalid token."""
        # Define a test step

        with pytest.allure.step("""Verify that user is unable to delete the Authorization system using request DELETE authorizationSystems/{id}  with 'id' parameter having invalid token."""):

            # deleteEntity the Authorization_Systems, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Authorization_Systems.deleteEntity(
                        id='Delete_authorizationSystem_testdata'),
                    token='invalid_token',
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Invalid Authorization Token')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
