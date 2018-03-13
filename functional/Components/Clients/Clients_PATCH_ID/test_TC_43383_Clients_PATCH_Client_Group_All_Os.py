# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43383 - Clients PATCH:

  Verify that user is able to modify child group with parameter 'Operating System>Matches' using request PATCH '/clients/'.


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
   'matchingRule': {'groups': [{'groups': [],
                                'operator': 'ALL',
                                'rules': [{'contextField': 'operatingSystem',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 'ANDROID',
                                           'operator': 'OSMATCH'}]}],
                    'operator': 'ALL',
                    'rules': []},
   'name': 'PATCH: Client updated with Group Rule Android OS',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43383')
    @pytest.mark.Clients
    @pytest.mark.PATCH
    def test_TC_43383_PATCH_Clients_Client_Group_Android_Os(self, context):
        """TC-43383 - Clients-PATCH
           Verify that user is able to modify child group with parameter 'Operating System>Matches' using request PATCH '/clients/'."""
        # Define a test step
        with pytest.allure.step("""ANDROID: Verify that user is able to modify child group with parameter 'Operating System>Matches' using request PATCH '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [],
                    'groups': [{
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
                    }]
                },
                name='PATCH: Client updated with Group Rule Android OS',
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
        with pytest.allure.step("""BLACKBERRY: Verify that user is able to modify child group with parameter 'Operating System>Matches' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [],
                    'groups': [{
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
                    }]
                },
                name='PATCH: Client updated with Group Rule BLACKBERRY OS',
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
        with pytest.allure.step("""WINDOWS_7: Verify that user is able to modify child group with parameter 'Operating System>Matches' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [],
                    'groups': [{
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
                    }]
                },
                name='PATCH: Client updated with Group Rule WINDOWS_7 OS',
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
        with pytest.allure.step("""WINDOWS_8: Verify that user is able to modify child group with parameter 'Operating System>Matches' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [],
                    'groups': [{
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
                    }]
                },
                name='PATCH: Client updated with Group Rule WINDOWS_8 OS',
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
        with pytest.allure.step("""MAC_OS_X: Verify that user is able to modify child group with parameter 'Operating System>Matches' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [],
                    'groups': [{
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
                    }]
                },
                name='PATCH: Client updated with Group Rule MAC_OS_X OS',
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
        with pytest.allure.step("""LINUX: Verify that user is able to modify child group with parameter 'Operating System>Matches' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [],
                    'groups': [{
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
                    }]
                },
                name='PATCH: Client updated with Group Rule LINUX OS',
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
        with pytest.allure.step("""MAC_OS_X_IPHONE: Verify that user is able to modify child group with parameter 'Operating System>Matches' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [],
                    'groups': [{
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
                    }]
                },
                name='PATCH: Client updated with Group Rule MAC_OS_X_IPHONE OS',
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
        with pytest.allure.step("""MAC_OS_X_IPAD: Verify that user is able to modify child group with parameter 'Operating System>Matches' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [],
                    'groups': [{
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
                    }]
                },
                name='PATCH: Client updated with Group Rule MAC_OS_X_IPAD OS',
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
        with pytest.allure.step("""IOS: Verify that user is able to modify child group with parameter 'Operating System>Matches' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [],
                    'groups': [{
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
                    }]
                },
                name='PATCH: Client updated with Group Rule IOS OS',
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
        with pytest.allure.step("""WINDOWS_MOBILE: Verify that user is able to modify child group with parameter 'Operating System>Matches' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [],
                    'groups': [{
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
                    }]
                },
                name='PATCH: Client updated with Group Rule WINDOWS_MOBILE OS',
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
        with pytest.allure.step("""WINDOWS_MOBILE7: Verify that user is able to modify child group with parameter 'Operating System>Matches' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [],
                    'groups': [{
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
                    }]
                },
                name='PATCH: Client updated with Group Rule WINDOWS_MOBILE_7 OS',
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
        with pytest.allure.step("""WINDOWS_PHONE8: Verify that user is able to modify child group with parameter 'Operating System>Matches' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [],
                    'groups': [{
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
                    }]
                },
                name='PATCH: Client updated with Group Rule WINDOWS_MOBILE_8 OS',
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
        with pytest.allure.step("""WINDOWS_VISTA: Verify that user is able to modify child group with parameter 'Operating System>Matches' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [],
                    'groups': [{
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
                    }]
                },
                name='PATCH: Client updated with Group Rule WINDOWS_VISTA OS',
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
        with pytest.allure.step("""WINDOWS_XP: Verify that user is able to modify child group with parameter 'Operating System>Matches' using request PATCH '/clients/'."""):
            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [],
                    'groups': [{
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
                    }]
                },
                name='PATCH: Client updated with Group Rule WINDOWS_XP OS',
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
