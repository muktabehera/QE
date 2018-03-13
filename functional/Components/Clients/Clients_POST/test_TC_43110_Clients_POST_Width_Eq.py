# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43110 - Clients POST:

  Verify that user is able to add source constraint rule with specific rule for parameter 'Width>Equals  using request POST '/clients/'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

JSON data sent to PathFinder in this test:

  {'id': 'sourceRuleWidthEQ',
   'matchingRule': {'groups': [], 'operator': 'ALL', 'rules': []},
   'name': 'POST: Client with Source Rule Width EQ',
   'sourceSelectionRule': [{'groups': [],
                            'operator': 'ALL',
                            'rules': [{'contextField': 'widthPx',
                                       'contextFieldKey': None,
                                       'contextFieldType': 'String',
                                       'expressionType': 'Single',
                                       'matchValue': 250,
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43110')
    @pytest.mark.Clients
    @pytest.mark.POST
    def test_TC_43110_POST_Clients_Width_Eq(self, context):
        """TC-43110 - Clients-POST
           Verify that user is able to add source constraint rule with specific rule for parameter 'Width>Equals  using request POST '/clients/'."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to add source constraint rule with specific rule for parameter 'Width>Equals  using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='sourceRuleWidthEQ',
                matchingRule={'operator': 'ALL',
                              'rules': [],
                              'groups': []},
                name='POST: Client with Source Rule Width EQ',
                sourceSelectionRule=[{
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'widthPx',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 250,
                        'contextFieldKey': None
                    }],
                    'groups': []
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

