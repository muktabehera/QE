# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44206 - Routes DELETE:

  Verify that user is unable to DELETE a single hop from root with incorrect member ID using request "/routes/{id}/hops/{memberId}".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/deletegroup/hops/GP12323?memberType=GROUP"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/deletegroup/hops/GP12323?memberType=GROUP"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Routes')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Routes test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44206')
    @pytest.mark.Routes
    @pytest.mark.DELETE
    def test_TC_44206_DELETE_Routes_Root(self, context):
        """TC-44206 - Routes-DELETE
           Verify that user is unable to DELETE a single hop from root with incorrect member ID using request "/routes/{id}/hops/{memberId}"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to DELETE a single hop from root with incorrect member ID using request "/routes/{id}/hops/{memberId}"."""):

            # deleteHop the Routes, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Routes.deleteHop(
                        id = 'route2',
                        memberId = 'incorrectGroupforHOP',
                        memberType = 'GROUP'
                    ),
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden, HTTPNotFound) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Route member with identifier incorrectGroupforHOP and type GROUP is not found')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
