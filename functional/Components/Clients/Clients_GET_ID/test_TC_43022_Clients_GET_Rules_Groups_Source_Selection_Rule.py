# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43022 - Clients GET:

  Verify that user is able to get all the details(rules, groups, sourceSelectionRule) of client using request GET /client{id}.


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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43022')
    @pytest.mark.Clients
    @pytest.mark.GET
    def test_TC_43022_GET_Clients_Rules_Groups_Source_Selection_Rule(self, context):
        """TC-43022 - Clients-GET
           Verify that user is able to get all the details(rules, groups, sourceSelectionRule) of client using request GET /client{id}."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to get all the details(rules, groups, sourceSelectionRule) of client using request GET /client{id}."""):

            # getEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
         ClientDetails = check(
                context.cl.Clients.getEntity(
                    id='clientsWithAllDetails')
            )

         print (ClientDetails)