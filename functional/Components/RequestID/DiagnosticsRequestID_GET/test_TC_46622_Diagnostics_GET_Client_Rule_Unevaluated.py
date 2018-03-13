# -*- coding: UTF-8 -*-

"""PFE Component Tests - Diagnosis.

* TC-46622 - Diagnosis GET:

  Verify that all the subsequent client rules are  displayed as 'Unevaluated' after any client rule is 'Failed' as per the client machine using request GET /diagnostices/requestId.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/diagnostics/requestId"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/diagnostics/requestId"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Diagnosis')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Diagnosis test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-46622')
    @pytest.mark.Diagnosis
    @pytest.mark.GET
    def test_TC_46622_GET_Diagnosis_Client_Rule_Unevaluated(self, context):
        """TC-46622 - Diagnosis-GET
           Verify that all the subsequent client rules are  displayed as 'Unevaluated' after any client rule is 'Failed' as per the client machine using request GET /diagnostices/requestId."""
        # Define a test step
        with pytest.allure.step("""Verify that all the subsequent client rules are  displayed as 'Unevaluated' after any client rule is 'Failed' as per the client machine using request GET /diagnostices/requestId."""):

            ### Positive test example

            # getEntity the Diagnosis.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Diagnosis.getEntity()
            )

        with pytest.allure.step("""Verify that all the subsequent client rules are  displayed as 'Unevaluated' after any client rule is 'Failed' as per the client machine using request GET /diagnostices/requestId."""):

            ### Negative test example

            # getEntity the Diagnosis, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Diagnosis.getEntity(),
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
