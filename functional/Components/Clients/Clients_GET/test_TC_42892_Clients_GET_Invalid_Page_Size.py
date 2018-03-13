# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-42892 - Clients GET:

  Verify that 20 records is displayed on providing 'page-size' value as 0 for 'page' parameter using request GET /clients.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients?page=1;0"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients?page=1;0"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42892')
    @pytest.mark.Clients
    @pytest.mark.GET
    def test_TC_42892_GET_Clients_Invalid_Page_Size(self, context):
        """TC-42892 - Clients-GET
           Verify that 20 records is displayed on providing 'page-size' value as 0 for 'page' parameter using request GET /clients."""
        # Define a test step
        with pytest.allure.step("""Verify that 20 records is displayed on providing 'page-size' value as 0 for 'page' parameter using request GET /clients."""):


            # listEntities the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Clients.listEntities(
                    page='1;0')
            )
