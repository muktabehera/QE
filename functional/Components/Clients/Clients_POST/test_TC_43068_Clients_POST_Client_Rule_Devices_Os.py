# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43068 - Clients POST:

  Verify that user is able to add new rule with parameter 'Operating System>Matches' using request POST '/clients/'.


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
   'id': 'clientandroidOS',
   'matchingRule': {'groups': [],
                    'operator': 'ALL',
                    'rules': [{'contextField': 'operatingSystem',
                               'contextFieldKey': '',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 'ANDROID',
                               'operator': 'OSMATCH'}]},
   'name': 'POST: Client Android OS',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43068')
    @pytest.mark.Clients
    @pytest.mark.POST
    def test_TC_43068_POST_Clients_Client_Rule_Android_Os(self, context):
        """TC-43068 - Clients-POST
           Verify that user is able to add new rule with parameter 'Operating System>Matches' using request POST '/clients/'."""
        # Define a test step
        with pytest.allure.step("""ANDROID: Verify that user is able to add new rule with parameter 'Operating System>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientandroidOS',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'operatingSystem',
                        'operator': 'OSMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'ANDROID',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='POST: Client Android OS',
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
        with pytest.allure.step("""BLACKBERRY : Verify that user is able to add new rule with parameter 'Operating System>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientBLACKBERRYOS',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'operatingSystem',
                        'operator': 'OSMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'BLACKBERRY',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='POST: Client BLACKBERRY OS',
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
        with pytest.allure.step("""WINDOWS_7: Verify that user is able to add new rule with parameter 'Operating System>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientWINDOWS_7OS',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'operatingSystem',
                        'operator': 'OSMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'WINDOWS_7',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='POST: Client WINDOWS_7 OS',
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
        with pytest.allure.step("""WINDOWS_8: Verify that user is able to add new rule with parameter 'Operating System>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientWINDOWS_8OS',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'operatingSystem',
                        'operator': 'OSMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'WINDOWS_8',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='POST: Client WINDOWS_8 OS',
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
        with pytest.allure.step("""MAC_OS_X: Verify that user is able to add new rule with parameter 'Operating System>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientMAC_OS_XOS',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'operatingSystem',
                        'operator': 'OSMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'MAC_OS_X',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='POST: Client MAC_OS_X OS',
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
        with pytest.allure.step("""LINUX: Verify that user is able to add new rule with parameter 'Operating System>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientLinuxOS',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'operatingSystem',
                        'operator': 'OSMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'LINUX',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='POST: Client LINUX OS',
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
        with pytest.allure.step("""MAC_OS_X_IPHONE: Verify that user is able to add new rule with parameter 'Operating System>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientMAC_OS_X_IPHONEOS',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'operatingSystem',
                        'operator': 'OSMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'MAC_OS_X_IPHONE',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='POST: Client MAC_OS_X_IPHONE OS',
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
        with pytest.allure.step("""MAC_OS_X_IPAD: Verify that user is able to add new rule with parameter 'Operating System>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientMAC_OS_X_IPADOS',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'operatingSystem',
                        'operator': 'OSMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'MAC_OS_X_IPAD',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='POST: Client MAC_OS_X_IPAD OS',
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
        with pytest.allure.step("""IOS: Verify that user is able to add new rule with parameter 'Operating System>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientIOSOS',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'operatingSystem',
                        'operator': 'OSMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IOS',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='POST: Client IOS OS',
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
        with pytest.allure.step("""WINDOWS_MOBILE: Verify that user is able to add new rule with parameter 'Operating System>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientWINDOWS_MOBILEOS',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'operatingSystem',
                        'operator': 'OSMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'WINDOWS_MOBILE',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='POST: Client WINDOWS_MOBILE OS',
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
        with pytest.allure.step("""WINDOWS_MOBILE7: Verify that user is able to add new rule with parameter 'Operating System>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientWINDOWS_MOBILE_7OS',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'operatingSystem',
                        'operator': 'OSMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'WINDOWS_MOBILE7',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='POST: Client WINDOWS_MOBILE_7 OS',
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
        with pytest.allure.step("""WINDOWS_PHONE8: Verify that user is able to add new rule with parameter 'Operating System>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientWINDOWS_MOBILE_8OS',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'operatingSystem',
                        'operator': 'OSMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'WINDOWS_PHONE8',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='POST: Client WINDOWS_MOBILE_8 OS',
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
        with pytest.allure.step("""WINDOWS_VISTA: Verify that user is able to add new rule with parameter 'Operating System>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientWINDOWS_VISTAOS',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'operatingSystem',
                        'operator': 'OSMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'WINDOWS_VISTA',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='POST: Client WINDOWS_VISTA OS',
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
        with pytest.allure.step("""WINDOWS_XP: Verify that user is able to add new rule with parameter 'Operating System>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientWINDOWS_XPOS',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'operatingSystem',
                        'operator': 'OSMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'WINDOWS_XP',
                        'contextFieldKey': ''
                    }],
                    'groups': []
                },
                name='POST: Client WINDOWS_XP OS',
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
