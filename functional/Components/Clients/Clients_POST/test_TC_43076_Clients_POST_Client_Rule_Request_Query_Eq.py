# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43076 - Clients POST:

  Verify that user is able to add new rule with parameter 'Request Query Parameter>Equals' using request POST '/clients/'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

JSON data sent to PathFinder in this test:

  {'bitrateCapLive': 0,
   'bitrateCapVOD': 0,
   'description': None,
   'id': 'clientRuleRequestQueryEQ',
   'matchingRule': {'groups': [],
                    'operator': 'ALL',
                    'rules': [{'contextField': 'queryParamMap',
                               'contextFieldKey': '10144114',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': '1014441',
                               'operator': 'EQ'}]},
   'name': 'POST: Client Rule Request Query EQ',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43076')
    @pytest.mark.Clients
    @pytest.mark.POST
    def test_TC_43076_POST_Clients_Client_Rule_Request_Query_Eq(self, context):
        """TC-43076 - Clients-POST
           Verify that user is able to add new rule with parameter 'Request Query Parameter>Equals' using request POST '/clients/'."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is able to add new rule with parameter 'Request Query Parameter>Equals' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientRuleRequestQueryEQ',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'queryParamMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': '1014441',
                        'contextFieldKey': '10144114'
                    }],
                    'groups': []
                },
                name='POST: Client Rule Request Query EQ',
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
        with pytest.allure.step("""Test2: Verify that user is able to add new rule with parameter 'Request Query Parameter>Equals' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientRuleRequestQueryEQ2',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'queryParamMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'AutoVCC1234!@#$%^',
                        'contextFieldKey': 'AutoVCC1234!@#$%^'
                    }],
                    'groups': []
                },
                name='POST: Client Rule Request Query EQ2',
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
