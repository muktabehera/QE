# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43385 - Clients PATCH:

  Verify that user is able to modify client with valid values for parameters 'name' using request PATCH /Clients.


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
                                           'matchValue': 'WINDOWS_MOBILE_8',
                                           'operator': 'OSMATCH'}]}],
                    'operator': 'ALL',
                    'rules': []},
   'name': 'PATCH client Name',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43385')
    @pytest.mark.Clients
    @pytest.mark.PATCH
    def test_TC_43385_PATCH_Clients_Client_Valid_Name(self, context):
        """TC-43385 - Clients-PATCH
           Verify that user is able to modify client with valid values for parameters 'name' using request PATCH /Clients."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is able to modify client with valid values for parameters 'name' using request PATCH /Clients."""):

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
                            'matchValue': 'WINDOWS_MOBILE_8',
                            'contextFieldKey': ''
                        }],
                        'groups': []
                    }]
                },
                name='PATCH client Name',
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
        with pytest.allure.step("""Test2: Verify that user is able to modify client with valid values for parameters 'name' using request PATCH /Clients."""):
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
                            'matchValue': 'WINDOWS_MOBILE_8',
                            'contextFieldKey': ''
                        }],
                        'groups': []
                    }]
                },
                name='PATCH1234',
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
        with pytest.allure.step("""Test3: Verify that user is able to modify client with valid values for parameters 'name' using request PATCH /Clients."""):
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
                            'matchValue': 'WINDOWS_MOBILE_8',
                            'contextFieldKey': ''
                        }],
                        'groups': []
                    }]
                },
                name='PATCH!@#',
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
        with pytest.allure.step("""Test4: Verify that user is able to modify client with valid values for parameters 'name' using request PATCH /Clients."""):
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
                            'matchValue': 'WINDOWS_MOBILE_8',
                            'contextFieldKey': ''
                        }],
                        'groups': []
                    }]
                },
                name='a123!@#$%&*()_-+=,.?;:{}[]`~',
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
