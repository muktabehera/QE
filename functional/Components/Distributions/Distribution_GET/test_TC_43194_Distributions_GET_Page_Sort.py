# -*- coding: UTF-8 -*-

"""PFE Component Tests - Distributions.

* TC-43194 - Distributions GET:

  Verify that user is able to GET the details of distributions with "page" and "Sort" parameters using request "/distributions".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/distributions?page=0;5 &sort=name;asc"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/distributions?page=0;5 &sort=name;asc"

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43194')
    @pytest.mark.Distributions
    @pytest.mark.GET
    def test_TC_43194_GET_Distributions_Page_Sort(self, context):
        """TC-43194 - Distributions-GET
           Verify that user is able to GET the details of distributions with "page" and "Sort" parameters using request "/distributions"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of distributions with "page" and "Sort" parameters using request "/distributions"."""):

            ### Positive test example

            # listEntities the Distributions.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Distributions.listEntities(
                    page='0;5', 
                    sort='name;asc'
                )
            )

        with pytest.allure.step("""Verify that user is able to GET the details of distributions with "page" and "Sort" parameters using request "/distributions"."""):

            ### Negative test example

            # listEntities the Distributions, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Distributions.listEntities(
                        page='0;5', 
                        sort='name;asc'
                    ),
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
