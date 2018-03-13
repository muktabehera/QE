# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43131 - Clients POST:

  Verify that user is able to add source constraint rule with specific group and rule for parameter 'Bit Rate(kbps)Equals' using request POST '/clients/'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

JSON data sent to PathFinder in this test:

  {'id': 'sourceRuleGroupBitrateEQ',
   'matchingRule': {'groups': [], 'operator': 'ALL', 'rules': []},
   'name': 'POST: Client with Source Rule and Group Bitrate EQ',
   'sourceSelectionRule': [{'groups': [{'groups': [],
                                        'operator': 'ALL',
                                        'rules': [{'contextField': 'bitrateKbps',
                                                   'contextFieldKey': None,
                                                   'contextFieldType': 'String',
                                                   'expressionType': 'Single',
                                                   'matchValue': 200,
                                                   'operator': 'EQ'}]}],
                            'operator': 'ALL',
                            'rules': [{'contextField': 'bitrateKbps',
                                       'contextFieldKey': None,
                                       'contextFieldType': 'String',
                                       'expressionType': 'Single',
                                       'matchValue': 200,
                                       'operator': 'EQ'}]}]}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43131')
    @pytest.mark.Clients
    @pytest.mark.POST
    def test_TC_43131_POST_Clients_Client_Source_Rule_Group_Bitrate_Eq(self, context):
        """TC-43131 - Clients-POST
           Verify that user is able to add source constraint rule with specific group and rule for parameter 'Bit Rate(kbps)Equals' using request POST '/clients/'."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is able to add source constraint rule with specific group and rule for parameter 'Bit Rate(kbps)Equals' using request POST '/clients/'."""):


            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='sourceRuleGroupBitrateEQ',
                matchingRule={'operator': 'ALL',
                              'rules': [],
                              'groups': []},
                name='POST: Client with Source Rule and Group Bitrate EQ',
                sourceSelectionRule=[{
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'bitrateKbps',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 200,
                        'contextFieldKey': None
                    }],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'bitrateKbps',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 200,
                            'contextFieldKey': None
                        }],
                        'groups': []
                    }]
                }])


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
        with pytest.allure.step("""Test2: Verify that user is able to add source constraint rule with specific group and rule for parameter 'Bit Rate(kbps)Equals' using request POST '/clients/'."""):


            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='sourceRuleGroupBitrateEQ2',
                matchingRule={'operator': 'ALL',
                              'rules': [],
                              'groups': []},
                name='POST: Client with Source Rule and Group Bitrate EQ2',
                sourceSelectionRule=[{
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'bitrateKbps',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 1024,
                        'contextFieldKey': None
                    }],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'bitrateKbps',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 1024,
                            'contextFieldKey': None
                        }],
                        'groups': []
                    }]
                }])


            # createEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Clients.createEntity(
                    body=clientDetails
                )
            )

