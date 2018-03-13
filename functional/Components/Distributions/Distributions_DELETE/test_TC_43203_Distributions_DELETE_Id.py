# -*- coding: UTF-8 -*-

"""PFE Component Tests - Distributions.

* TC-43203 - Distributions DELETE:

  Verify that user is able to DELETE distributions using request "/distributions/{id}".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       <PF_host>://<client_host>/distributions/deleteDistribution

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       <PF_host>://<client_host>/distributions/deleteDistribution

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Distributions')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Distributions test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43203')
    @pytest.mark.Distributions
    @pytest.mark.DELETE
    def test_TC_43203_DELETE_Distributions_Id(self, context):
        """TC-43203 - Distributions-DELETE
           Verify that user is able to DELETE distributions using request "/distributions/{id}"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to DELETE distributions using request "/distributions/{id}"."""):

            ### Positive test example

            # deleteEntity the Distributions.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Distributions.deleteEntity()
            )

        with pytest.allure.step("""Verify that user is able to DELETE distributions using request "/distributions/{id}"."""):

            ### Negative test example

            # deleteEntity the Distributions, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Distributions.deleteEntity(),
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
