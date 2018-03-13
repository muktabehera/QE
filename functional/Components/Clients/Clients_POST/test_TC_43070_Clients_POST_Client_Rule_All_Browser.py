# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43070 - Clients POST:

  Verify that user is able to add new rule with parameter 'Browser>Matches' using request POST '/clients/'.


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
   'id': 'clientRulebrowserIE',
   'matchingRule': {'groups': [],
                    'operator': 'ALL',
                    'rules': [{'contextField': 'browser',
                               'contextFieldKey': '',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 'IE',
                               'operator': 'BROWSERMATCH'}]},
   'name': 'POST: Client Rule IE Browser',
   'sourceSelectionRule': []}

"""

import pytest

from qe_common import *

logger = init_logger()

# Common framwork variables initialization
global env
env = load_config_file(get_config_file_cmdarg())
# Used for generating random test data
faker = Factory.create(env.Locale)


@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43070')
    @pytest.mark.Clients
    @pytest.mark.POST
    def test_TC_43070_POST_Clients_Client_Rule_Ie_Browser(self, context):
        """TC-43070 - Clients-POST
           Verify that user is able to add new rule with parameter 'Browser>Matches' using request POST '/clients/'."""
        # Define a test step
        with pytest.allure.step("""IE: Verify that user is able to add new rule with parameter 'Browser>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientRulebrowserIE',
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
                name='POST: Client Rule IE Browser',
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
        with pytest.allure.step("""IE6: Verify that user is able to add new rule with parameter 'Browser>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientRulebrowserIE6',
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
                name='POST: Client Rule IE6 Browser',
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
        with pytest.allure.step("""IE7: Verify that user is able to add new rule with parameter 'Browser>Matches' using request POST '/clients/'."""):


            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientRulebrowserIE7',
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
                name='POST: Client Rule IE7 Browser',
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
        with pytest.allure.step("""IE8: Verify that user is able to add new rule with parameter 'Browser>Matches' using request POST '/clients/'."""):


            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientRulebrowserIE8',
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
                name='POST: Client Rule IE8 Browser',
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
        with pytest.allure.step("""IE9: Verify that user is able to add new rule with parameter 'Browser>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientRulebrowserIE9',
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
                name='POST: Client Rule IE9 Browser',
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
        with pytest.allure.step("""IE10: Verify that user is able to add new rule with parameter 'Browser>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientRulebrowserIE10',
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
                name='POST: Client Rule IE10 Browser',
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
        with pytest.allure.step("""IE11: Verify that user is able to add new rule with parameter 'Browser>Matches' using request POST '/clients/'."""):


            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientRulebrowserIE11',
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
                name='POST: Client Rule IE11 Browser',
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
        with pytest.allure.step("""FIREFOX: Verify that user is able to add new rule with parameter 'Browser>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientRulebrowserFirefox',
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
                name='POST: Client Rule Firefox Browser',
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
        with pytest.allure.step("""CHROME: Verify that user is able to add new rule with parameter 'Browser>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientRulebrowserCHROME',
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
                name='POST: Client Rule CHROME Browser',
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
        with pytest.allure.step("""SAFARI: Verify that user is able to add new rule with parameter 'Browser>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientRulebrowserSAFARI',
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
                name='POST: Client Rule SAFARI Browser',
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



