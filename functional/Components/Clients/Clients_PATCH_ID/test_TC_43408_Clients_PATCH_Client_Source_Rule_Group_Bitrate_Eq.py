# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43408 - Clients PATCH:

  Verify that user is able to modify source constraint rule with specific group and rule for parameter 'Bit Rate(kbps)Equals' using request PATCH '/clients/'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/clientUpdate"

JSON data sent to PathFinder in this test:

  {'matchingRule': {'groups': [], 'operator': 'ALL', 'rules': []},
   'name': 'PATCH: Client Updated with Source Rule and Group Bitrate EQ',
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
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43408')
    @pytest.mark.Clients
    @pytest.mark.PATCH
    def test_TC_43408_PATCH_Clients_Client_Source_Rule_Group_Bitrate_Eq(self, context):
        """TC-43408 - Clients-PATCH
           Verify that user is able to modify source constraint rule with specific group and rule for parameter 'Bit Rate(kbps)Equals' using request PATCH '/clients/'."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is able to modify source constraint rule with specific group and rule for parameter 'Bit Rate(kbps)Equals' using request PATCH '/clients/'."""):


            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={'operator': 'ALL',
                              'rules': [],
                              'groups': []},
                name='PATCH: Client Updated with Source Rule and Group Bitrate EQ',
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
        with pytest.allure.step("""Test2: Verify that user is able to modify source constraint rule with specific group and rule for parameter 'Bit Rate(kbps)Equals' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={'operator': 'ALL',
                              'rules': [],
                              'groups': []},
                name='PATCH: Client Updated with Source Rule and Group Bitrate EQ2',
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
