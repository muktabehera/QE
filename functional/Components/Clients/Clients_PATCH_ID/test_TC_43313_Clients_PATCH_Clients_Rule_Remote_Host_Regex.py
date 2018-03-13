# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43313 - Clients PATCH:

  Verify that user is able to modify client rule with parameter 'Remote Host>Matches Regex' using request PATCH '/clients/'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/clientUpdate"

JSON data sent to PathFinder in this test:

  {'matchingRule': {'groups': [],
                    'operator': 'ALL',
                    'rules': [{'contextField': 'remoteHost',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': '10.1.10.10',
                               'operator': 'REGEX'}]},
   'name': 'PATCh: Client with updated RemoteHost Regex Rule',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43313')
    @pytest.mark.Clients
    @pytest.mark.PATCH
    def test_TC_43313_PATCH_Clients_Clients_Rule_Remote_Host_Regex(self, context):
        """TC-43313 - Clients-PATCH
           Verify that user is able to modify client rule with parameter 'Remote Host>Matches Regex' using request PATCH '/clients/'."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is able to modify client rule with parameter 'Remote Host>Matches Regex' using request PATCH '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteHost',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': '10.1.10.10',
                        'contextFieldKey': None
                    }],
                    'groups': []
                },
                name='PATCh: Client with updated RemoteHost Regex Rule',
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
        with pytest.allure.step("""Test2: Verify that user is able to modify client rule with parameter 'Remote Host>Matches Regex' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteHost',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': 'acss_-1234.com',
                        'contextFieldKey': None
                    }],
                    'groups': []
                },
                name='PATCH: Client with updated Regex2 Rule',
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
        with pytest.allure.step("""Test3: Verify that user is able to modify client rule with parameter 'Remote Host>Matches Regex' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteHost',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': 'acss_1234',
                        'contextFieldKey': None
                    }],
                    'groups': []
                },
                name='PATCH: Client with updated RemoteHost Regex3 Rule',
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
