# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43957 - Clients GET:

  Verify that user is able to GET the details of Operating System using  GET /useragent/operatingsystems without providing any parameter. .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/useragent/operatingsystems"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/useragent/operatingsystems"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43957')
    @pytest.mark.Clients
    @pytest.mark.GET
    def test_TC_43957_GET_Clients_Operatingsystems(self, context):
        """TC-43957 - Clients-GET
           Verify that user is able to GET the details of Operating System using  GET /useragent/operatingsystems without providing any parameter. ."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of Operating System using  GET /useragent/operatingsystems without providing any parameter. ."""):

            ### Positive test example

            # getOperatingSystems_1 the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Clients.getOperatingSystems_1()
            )

        with pytest.allure.step("""Verify that user is able to GET the details of Operating System using  GET /useragent/operatingsystems without providing any parameter. ."""):

            ### Negative test example

            # getOperatingSystems_1 the Clients, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Clients.getOperatingSystems_1(),
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
