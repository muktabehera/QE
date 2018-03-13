# -*- coding: UTF-8 -*-

"""PFE Component Tests - Distributions.

* TC-45021 - Distributions GET:

  Verify that error message is displayed on providing non existing 'Id' in 'Id' parameter using request GET /distributions{id}.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/distributions/nonExistingId"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/distributions/nonExistingId"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Distributions')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Distributions test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-45021')
    @pytest.mark.Distributions
    @pytest.mark.GET
    def test_TC_45021_GET_Distributions_Non_Existing_Id(self, context):
        """TC-45021 - Distributions-GET
           Verify that error message is displayed on providing non existing 'Id' in 'Id' parameter using request GET /distributions{id}."""
        # Define a test step
        with pytest.allure.step("""Verify that error message is displayed on providing non existing 'Id' in 'Id' parameter using request GET /distributions{id}."""):

            ### Positive test example

            # getEntity the Distributions.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Distributions.getEntity()
            )

        with pytest.allure.step("""Verify that error message is displayed on providing non existing 'Id' in 'Id' parameter using request GET /distributions{id}."""):

            ### Negative test example

            # getEntity the Distributions, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Distributions.getEntity(),
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
