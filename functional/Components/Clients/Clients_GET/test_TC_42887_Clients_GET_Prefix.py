# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-42887 - Clients GET:

  Verify that user is able to GET the details of clients using request GET /clients with parameter prefix.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients?prefix=c"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients?prefix=c"

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42887')
    @pytest.mark.Clients
    @pytest.mark.GET
    def test_TC_42887_GET_Clients_Prefix(self, context):
        """TC-42887 - Clients-GET
           Verify that user is able to GET the details of clients using request GET /clients with parameter prefix."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of clients using request GET /clients with parameter prefix."""):

            # listEntities the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Clients.listEntities(
                    prefix='p')
            )

