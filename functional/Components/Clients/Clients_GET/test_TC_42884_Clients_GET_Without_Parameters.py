# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-42884 - Clients GET:

  Verify that user is able to GET the details of clients using request GET /clients without providing any parameter.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42884')
    @pytest.mark.Clients
    @pytest.mark.GET
    def test_TC_42884_GET_Clients_Without_Parameters(self, context):
        """TC-42884 - Clients-GET
           Verify that user is able to GET the details of clients using request GET /clients without providing any parameter."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of clients using request GET /clients without providing any parameter."""):


            # listEntities the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Clients.listEntities()
            )

