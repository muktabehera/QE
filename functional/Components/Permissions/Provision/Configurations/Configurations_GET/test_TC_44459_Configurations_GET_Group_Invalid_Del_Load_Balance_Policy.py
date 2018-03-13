# -*- coding: UTF-8 -*-

"""PFE Component Tests - Configurations.

* TC-44459 - Configurations GET:

  Verify that user is unable to create group on providing invalid values in parameter 'deliveryLoadBalancePolicy' using request POST '/groups'.


Equivalent test CURL command:

  curl -k -H "Host: <client_host>" -H "Authorization: Bearer
       <valid_token>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/configurations"

Same, with test data:

  curl -k -H "Host: <client_host>" -H "Authorization: Bearer
       <valid_token>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/configurations"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Configurations')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Configurations test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44459')
    @pytest.mark.Configurations
    @pytest.mark.GET
    def test_TC_44459_GET_Configurations_Group_Invalid_Del_Load_Balance_Policy(self, context):
        """TC-44459 - Configurations-GET
           Verify that user is unable to create group on providing invalid values in parameter 'deliveryLoadBalancePolicy' using request POST '/groups'."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to create group on providing invalid values in parameter 'deliveryLoadBalancePolicy' using request POST '/groups'."""):

            ### Positive test example

            # listEntities the Configurations.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Configurations.listEntities()
            )

        with pytest.allure.step("""Verify that user is unable to create group on providing invalid values in parameter 'deliveryLoadBalancePolicy' using request POST '/groups'."""):

            ### Negative test example

            # listEntities the Configurations, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Configurations.listEntities(),
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
