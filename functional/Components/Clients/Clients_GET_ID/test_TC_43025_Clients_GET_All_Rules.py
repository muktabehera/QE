# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43025 - Clients GET:

  Verify that user is able to get 'rules' details associated with client using request GET /client{id}.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/clientsAllRules"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43025')
    @pytest.mark.Clients
    @pytest.mark.GET
    def test_TC_43025_GET_Clients_All_Rules(self, context):
        """TC-43025 - Clients-GET
           Verify that user is able to get 'rules' details associated with client using request GET /client{id}."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to get 'rules' details associated with client using request GET /client{id}."""):

            # getEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Clients.getEntity(
                    id='clientsWithAllDetails')
            )

