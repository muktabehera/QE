# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43057 - Clients POST:

  Verify that user is able to add new rule with parameter 'Server Host>Equals' using request POST '/clients/'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

JSON data sent to PathFinder in this test:

  {'id': 'clientServerHost',
   'matchingRule': {'groups': [],
                    'operator': 'ALL',
                    'rules': [{'contextField': 'serverHost',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': '10.1.10.10',
                               'operator': 'EQ'}]},
   'name': 'POST: Client with Server Host EQ Rule 1',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43057')
    @pytest.mark.Clients
    @pytest.mark.POST
    def test_TC_43057_POST_Clients_Clients_Rule_Server_Host_Eq(self, context):
        """TC-43057 - Clients-POST
           Verify that user is able to add new rule with parameter 'Server Host>Equals' using request POST '/clients/'."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is able to add new rule with parameter 'Server Host>Equals' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientServerHost',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'serverHost',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': '10.1.10.10',
                        'contextFieldKey': None
                    }],
                    'groups': []
                },
                name='POST: Client with Server Host EQ Rule 1',
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

        # Define a test step
        with pytest.allure.step("""Test2: Verify that user is able to add new rule with parameter 'Server Host>Equals' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientServerHost2',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'serverHost',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'autovcc_24.com',
                        'contextFieldKey': None
                    }],
                    'groups': []
                },
                name='POST: Client with Server Host EQ Rule2',
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
