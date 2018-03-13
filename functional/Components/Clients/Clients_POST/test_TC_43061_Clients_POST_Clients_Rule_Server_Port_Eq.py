# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43061 - Clients POST:

  Verify that user is able to add new rule with parameter 'Server Port>Equals' using request POST '/clients/'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

JSON data sent to PathFinder in this test:

  {'id': 'clientServerPort1',
   'matchingRule': {'groups': [],
                    'operator': 'ALL',
                    'rules': [{'contextField': 'serverPort',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 80,
                               'operator': 'EQ'}]},
   'name': 'POST: Client with Server Port EQ Rule1',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43061')
    @pytest.mark.Clients
    @pytest.mark.POST
    def test_TC_43061_POST_Clients_Clients_Rule_Server_Port_Eq(self, context):
        """TC-43061 - Clients-POST
           Verify that user is able to add new rule with parameter 'Server Port>Equals' using request POST '/clients/'."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is able to add new rule with parameter 'Server Port>Equals' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientServerPort1',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 80,
                        'contextFieldKey': None
                    }],
                    'groups': []
                },
                name='POST: Client with Server Port EQ Rule1',
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
        with pytest.allure.step("""Test2: Verify that user is able to add new rule with parameter 'Server Port>Equals' using request POST '/clients/'."""):


            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientServerPort2',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 8080,
                        'contextFieldKey': None
                    }],
                    'groups': []
                },
                name='POST: Client with Server Port EQ Rule2',
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
