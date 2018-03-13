# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43322 - Clients PATCH:

  Verify that user is able to modify client rule with parameter 'Browser>Matches' using request PATCH '/clients/'.


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
                    'rules': [{'contextField': 'browser',
                               'contextFieldKey': '',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 'IE',
                               'operator': 'BROWSERMATCH'}]},
   'name': 'PATCH: Client updated with Rule IE Browser',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43322')
    @pytest.mark.Clients
    @pytest.mark.PATCH
    def test_TC_43322_PATCH_Clients_Client_Rule_Ie_Browser(self, context):
        """TC-43322 - Clients-PATCH
           Verify that user is able to modify client rule with parameter 'Browser>Matches' using request PATCH '/clients/'."""
        # Define a test step
        with pytest.allure.step("""IE: Verify that user is able to modify client rule with parameter 'Browser>Matches' using request PATCH '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='PATCH: Client updated with Rule IE Browser',
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
        with pytest.allure.step("""IE6: Verify that user is able to modify client rule with parameter 'Browser>Matches' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE6',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='PATCH: Client updated with Rule IE6 Browser',
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
        with pytest.allure.step("""IE7: Verify that user is able to modify client rule with parameter 'Browser>Matches' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE7',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='PATCH: Client updated with Rule IE7 Browser',
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
        with pytest.allure.step("""IE8: Verify that user is able to modify client rule with parameter 'Browser>Matches' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE8',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='PATCH: Client updated with Rule IE8 Browser',
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
        with pytest.allure.step("""IE9: Verify that user is able to modify client rule with parameter 'Browser>Matches' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE9',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='PATCH: Client updated with Rule IE8 Browser',
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
        with pytest.allure.step("""IE10: Verify that user is able to modify client rule with parameter 'Browser>Matches' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE10',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='PATCH: Client updated with Rule IE10 Browser',
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
        with pytest.allure.step("""IE11: Verify that user is able to modify client rule with parameter 'Browser>Matches' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE11',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='PATCH: Client updated with Rule IE11 Browser',
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
        with pytest.allure.step("""FIREFOX : Verify that user is able to modify client rule with parameter 'Browser>Matches' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'FIREFOX',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='PATCH: Client updated with Rule Firefox Browser',
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
        with pytest.allure.step("""CHROME: Verify that user is able to modify client rule with parameter 'Browser>Matches' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'CHROME',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='PATCH: Client updated with Rule CHROME Browser',
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
        with pytest.allure.step("""SAFARI: Verify that user is able to modify client rule with parameter 'Browser>Matches' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'SAFARI',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='PATCH: Client updated with SAFARI Browser',
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
