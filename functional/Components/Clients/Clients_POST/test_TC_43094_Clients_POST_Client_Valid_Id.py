# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43094 - Clients POST:

  Verify that user is able to create client with valid values for parameters 'id' using request POST /Clients.


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
   'id': '123456',
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
   'name': 'POST: Client Valid ID1',
   'sourceSelectionRule': []}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43094')
    @pytest.mark.Clients
    @pytest.mark.POST
    def test_TC_43094_POST_Clients_Client_Valid_Id(self, context):
        """TC-43094 - Clients-POST
           Verify that user is able to create client with valid values for parameters 'id' using request POST /Clients."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is able to create client with valid values for parameters 'id' using request POST /Clients."""):


            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='123456',
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
                name='POST: Client Valid ID1',
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
        with pytest.allure.step("""Test2: Verify that user is able to create client with valid values for parameters 'id' using request POST /Clients."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='POST_123:-.',
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
                name='POST: Client Valid ID2',
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
        with pytest.allure.step("""Test3: Verify that user is able to create client with valid values for parameters 'id' using request POST /Clients."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='A_:-.',
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
                name='POST: Client Valid ID3',
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
        with pytest.allure.step("""Test4: Verify that user is able to create Proximity Zone."""):

            # Test case configuration
            proximityZoneDetails = context.sc.ProximityZoneDetails(
                configAdminCanEdit=True,
                configurations=[],
                id='proximityAuto',
                name='ProximityAuto',
                proximityDetails=[{
                    'cidr': '0.0.0.0/0',
                    'metric': 1,
                    'notes': 'a'
                }],
                visibleInAllConfigurations=True)


            # createEntity the Proximity_Zones.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Proximity_Zones.createEntity(
                    body=proximityZoneDetails
                )
            )

