# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43074 - Clients POST:

  Verify that user is able to add new rule with parameter 'Request Header>Matches Regex' using request POST '/clients/'.


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
   'id': 'clientRuleRequestHeaderRegex',
   'matchingRule': {'groups': [],
                    'operator': 'ALL',
                    'rules': [{'contextField': 'headerMap',
                               'contextFieldKey': '10144114',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': '1014441',
                               'operator': 'REGEX'}]},
   'name': 'POST: Client Rule Request Header REGEX',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43074')
    @pytest.mark.Clients
    @pytest.mark.POST
    def test_TC_43074_POST_Clients_Client_Rule_Request_Header_Regex(self, context):
        """TC-43074 - Clients-POST
           Verify that user is able to add new rule with parameter 'Request Header>Matches Regex' using request POST '/clients/'."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is able to add new rule with parameter 'Request Header>Matches Regex' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientRuleRequestHeaderRegex',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'headerMap',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': '1014441',
                        'contextFieldKey': '10144114'
                    }],
                    'groups': []
                },
                name='POST: Client Rule Request Header REGEX',
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
        with pytest.allure.step("""Test2: Verify that user is able to add new rule with parameter 'Request Header>Matches Regex' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientRuleRequestHeaderRegex2',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'headerMap',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': 'AutoVCC1234!@#$%^',
                        'contextFieldKey': 'AutoVCC1234!@#$%^'
                    }],
                    'groups': []
                },
                name='POST: Client Rule Request Header REGEX2',
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
