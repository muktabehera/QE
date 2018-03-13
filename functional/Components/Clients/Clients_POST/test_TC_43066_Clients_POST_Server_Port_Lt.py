# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43066 - Clients POST:

  Verify that user is able to add new rule with parameter 'Server Port>LT(Less Than)' using request POST '/clients/'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

JSON data sent to PathFinder in this test:

  {'id': 'clientServerPortLT',
   'matchingRule': {'groups': [],
                    'operator': 'ALL',
                    'rules': [{'contextField': 'serverPort',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 8080,
                               'operator': 'LT'}]},
   'name': 'POST: Client with Server Port LT Rule',
   'sourceSelectionRule': []}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43066')
    @pytest.mark.Clients
    @pytest.mark.POST
    def test_TC_43066_POST_Clients_Server_Port_Lt(self, context):
        """TC-43066 - Clients-POST
           Verify that user is able to add new rule with parameter 'Server Port>LT(Less Than)' using request POST '/clients/'."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to add new rule with parameter 'Server Port>LT(Less Than)' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientServerPortLT',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'LT',
                        'contextFieldType': 'String',
                        'matchValue': 8080,
                        'contextFieldKey': None
                    }],
                    'groups': []
                },
                name='POST: Client with Server Port LT Rule',
                sourceSelectionRule=[])


            # createEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Clients.createEntity(
                    body=clientDetails
                )
            )
