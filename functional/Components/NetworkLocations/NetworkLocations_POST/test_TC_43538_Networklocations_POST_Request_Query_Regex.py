# -*- coding: UTF-8 -*-

"""PFE Component Tests - Network_Locations.

* TC-43538 - Network_Locations POST:

  Verify that user is able to create network location with rule and group having parameter 'Request Query Parameter>Matches Regex' using request POST '/networkLocations/'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations"

JSON data sent to PathFinder in this test:

  {'bitrateCapLive': 0,
   'bitrateCapVOD': 0,
   'description': None,
   'id': 'requestQueryREGEX',
   'matchingRule': {'groups': [{'groups': [],
                                'operator': 'ALL',
                                'rules': [{'contextField': 'queryParamMap',
                                           'contextFieldKey': 'autovcc!234',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 'autovcc!234',
                                           'operator': 'REGEX'}]}],
                    'operator': 'ALL',
                    'rules': [{'contextField': 'queryParamMap',
                               'contextFieldKey': '101441',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': '101441',
                               'operator': 'REGEX'}]},
   'name': 'Network Request Query REGEX'}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Network_Locations')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Network_Locations test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43538')
    @pytest.mark.Network_Locations
    @pytest.mark.POST
    def test_TC_43538_POST_Network_Locations_Request_Query_Regex(self, context):
        """TC-43538 - Network_Locations-POST
           Verify that user is able to create network location with rule and group having parameter 'Request Query Parameter>Matches Regex' using request POST '/networkLocations/'."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create network location with rule and group having parameter 'Request Query Parameter>Matches Regex' using request POST '/networkLocations/'."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=0,
                bitrateCapVOD=0,
                id='requestQueryREGEX',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'queryParamMap',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': '101441',
                        'contextFieldKey': '101441'
                    }],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'queryParamMap',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': 'autovcc!234',
                            'contextFieldKey': 'autovcc!234'
                        }],
                        'groups': []
                    }]
                },
                name='Network Request Query REGEX')


            # createEntity the Network_Locations.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Network_Locations.createEntity(
                    body=networkLocationDetails
                )
            )

