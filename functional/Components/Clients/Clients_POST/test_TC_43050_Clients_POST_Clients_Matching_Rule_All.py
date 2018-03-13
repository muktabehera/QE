# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43050 - Clients POST:

  Verify that user is able to add new rule with parameter 'matchingRule'(ALL, ANY, NONE) using request POST '/clients/'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

JSON data sent to PathFinder in this test:

  {'id': 'clientMatchingRuleALL',
   'matchingRule': {'groups': [],
                    'operator': 'ALL',
                    'rules': [{'contextField': 'remoteAddress',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': '172.30.2.49/32',
                               'operator': 'IPMATCH'}]},
   'name': 'POST: Client with Matching Rule ALL',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43050')
    @pytest.mark.Clients
    @pytest.mark.POST
    def test_TC_43050_POST_Clients_Clients_Matching_Rule_All(self, context):
        """TC-43050 - Clients-POST
           Verify that user is able to add new rule with parameter 'matchingRule'(ALL, ANY, NONE) using request POST '/clients/'."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to add new rule with parameter 'matchingRule'(ALL) using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientMatchingRuleALL',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'IPMATCH',
                        'contextFieldType': 'String',
                        'matchValue': '172.30.2.49/32',
                        'contextFieldKey': None
                    }],
                    'groups': []
                },
                name='POST: Client with Matching Rule ALL',
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
        with pytest.allure.step("""Verify that user is able to add new rule with parameter 'matchingRule'(ANY) using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientMatchingRuleANY',
                matchingRule={
                    'operator':
                    'ANY',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'IPMATCH',
                        'contextFieldType': 'String',
                        'matchValue': '172.30.2.49/32',
                        'contextFieldKey': None
                    }],
                    'groups': []
                },
                name='POST: Client with Matching Rule ANY',
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
        with pytest.allure.step("""Verify that user is able to add new rule with parameter 'matchingRule'(NONE) using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientMatchingRuleNONE',
                matchingRule={
                    'operator':
                    'NONE',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'IPMATCH',
                        'contextFieldType': 'String',
                        'matchValue': '172.30.2.49/32',
                        'contextFieldKey': None
                    }],
                    'groups': []
                },
                name='POST: Client with Matching Rule NONE',
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