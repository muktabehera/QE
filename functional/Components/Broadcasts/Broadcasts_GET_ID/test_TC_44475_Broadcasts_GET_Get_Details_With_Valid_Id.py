# -*- coding: UTF-8 -*-

"""PFE Component Tests - Broadcasts.

* TC-44475 - Broadcasts GET:

  Verify that user is able to GET the details of broadcasts with valid id using request "/broadcasts/{id}".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/broadcasts/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/broadcasts/Broadcast_GetByID"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Broadcasts')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Broadcasts test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44475')
    @pytest.mark.Broadcasts
    @pytest.mark.GET
    def test_TC_44475_GET_Broadcasts_Get_Details_With_Valid_Id(self, context):
        """TC-44475 - Broadcasts-GET
           Verify that user is able to GET the details of broadcasts with valid id using request "/broadcasts/{id}"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of broadcasts with valid id using request "/broadcasts/{id}"."""):

            ### Positive test example

            # getEntity the Broadcasts.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Broadcasts.getEntity(
                    id='Broadcast_GetByID')
            )

        with pytest.allure.step("""Verify that user is able to GET the details of broadcasts with valid id using request "/broadcasts/{id}"."""):

            ### Negative test example

            # getEntity the Broadcasts, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Broadcasts.getEntity(
                        id='Broadcast_GetByID'),
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
