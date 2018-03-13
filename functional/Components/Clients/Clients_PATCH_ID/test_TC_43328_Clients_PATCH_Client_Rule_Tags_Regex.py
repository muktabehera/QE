# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43328 - Clients PATCH:

  Verify that user is able to modify client rule with parameter 'Tags>Matches Regex' using request PATCH '/clients/'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/clientUpdate"

JSON data sent to PathFinder in this test:

  {'bitrateCapLive': 0,
   'bitrateCapVOD': 0,
   'description': None,
   'matchingRule': {'groups': [],
                    'operator': 'ALL',
                    'rules': [{'contextField': 'tags',
                               'contextFieldKey': '10144114',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': '1014441',
                               'operator': 'REGEX'}]},
   'name': 'PATCH: Client updated with Rule Tags Regex',
   'sourceSelectionRule': []}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43328')
    @pytest.mark.Clients
    @pytest.mark.PATCH
    def test_TC_43328_PATCH_Clients_Client_Rule_Tags_Regex(self, context):
        """TC-43328 - Clients-PATCH
           Verify that user is able to modify client rule with parameter 'Tags>Matches Regex' using request PATCH '/clients/'."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is able to modify client rule with parameter 'Tags>Matches Regex' using request PATCH '/clients/'."""):


            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'tags',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': '1014441',
                        'contextFieldKey': '10144114'
                    }],
                    'groups': []
                },
                name='PATCH: Client updated with Rule Tags Regex',
                sourceSelectionRule=[])


            # updateEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Clients.updateEntity(
                    body=clientDetails, 
                    id='clientUpdate'
                
                )
            )

        # Define a test step
        with pytest.allure.step("""Test2: Verify that user is able to modify client rule with parameter 'Tags>Matches Regex' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'tags',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': 'AutoVCC1234!@#$%^',
                        'contextFieldKey': 'AutoVCC1234!@#$%^'
                    }],
                    'groups': []
                },
                name='PATCH: Client updated with Rule Tags Regex',
                sourceSelectionRule=[])

            # updateEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Clients.updateEntity(
                    body=clientDetails,
                    id='clientUpdate'

                )
            )