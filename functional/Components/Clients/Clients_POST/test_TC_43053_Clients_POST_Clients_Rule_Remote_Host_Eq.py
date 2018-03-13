# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43053 - Clients POST:

  Verify that user is able to add new rule with parameter 'Remote Host>Equals' using request POST '/clients/'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

JSON data sent to PathFinder in this test:

  {'id': 'clientRemoteHostEQ',
   'matchingRule': {'groups': [],
                    'operator': 'ALL',
                    'rules': [{'contextField': 'remoteHost',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': '10.1.10.10',
                               'operator': 'EQ'}]},
   'name': 'POST: Client with RemoteHost EQ Rule',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43053')
    @pytest.mark.Clients
    @pytest.mark.POST
    def test_TC_43053_POST_Clients_Clients_Rule_Remote_Host_Eq(self, context):
        """TC-43053 - Clients-POST
           Verify that user is able to add new rule with parameter 'Remote Host>Equals' using request POST '/clients/'."""
        # Define a test step
        with pytest.allure.step("""Example1: Verify that user is able to add new rule with parameter 'Remote Host>Equals' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientRemoteHostEQ',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteHost',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': '10.1.10.10',
                        'contextFieldKey': None
                    }],
                    'groups': []
                },
                name='POST: Client with RemoteHost EQ Rule',
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
        with pytest.allure.step("""Example2: Verify that user is able to add new rule with parameter 'Remote Host>Equals' using request POST '/clients/'."""):


            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientRemoteHostEQ2',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteHost',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'acss_1234',
                        'contextFieldKey': None
                    }],
                    'groups': []
                },
                name='POST: Client with RemoteHost EQ2 Rule',
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
        with pytest.allure.step("""Example3: Verify that user is able to add new rule with parameter 'Remote Host>Equals' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientRemoteHostEQ3',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteHost',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'acss_-1234.com',
                        'contextFieldKey': None
                    }],
                    'groups': []
                },
                name='POST: Client with RemoteHost EQ3 Rule',
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


