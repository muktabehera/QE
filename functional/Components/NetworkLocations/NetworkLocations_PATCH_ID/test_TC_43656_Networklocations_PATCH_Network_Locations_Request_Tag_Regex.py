# -*- coding: UTF-8 -*-

"""PFE Component Tests - Network_Locations.

* TC-43656 - Network_Locations PATCH:

  Verify that user is able to modify network location with rule and group having parameter 'Tags>Matches Regex' using request PATCH '/networkLocations/'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations/networkUpdate"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations/networkUpdate"

JSON data sent to PathFinder in this test:

  {'bitrateCapLive': 1024,
   'bitrateCapVOD': 650,
   'id': 'networkUpdate',
   'matchingRule': {'groups': [{'groups': [],
                                'operator': 'ALL',
                                'rules': [{'contextField': 'remoteAddress',
                                           'contextFieldKey': None,
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': '101.101.105.105/24',
                                           'operator': 'IPMATCH'},
                                          {'contextField': 'remoteAddress',
                                           'contextFieldKey': None,
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 'metric',
                                           'operator': 'PROXIMITYMATCH'},
                                          {'contextField': 'remoteHost',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 'abc-sder_qumu.com',
                                           'operator': 'EQ'},
                                          {'contextField': 'remoteHost',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 'abc-sder_qumu.com',
                                           'operator': 'REGEX'},
                                          {'contextField': 'serverHost',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': '10.1.10.10',
                                           'operator': 'EQ'},
                                          {'contextField': 'serverHost',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': '10.10.10.10',
                                           'operator': 'REGEX'},
                                          {'contextField': 'serverPort',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 8080,
                                           'operator': 'EQ'},
                                          {'contextField': 'serverPort',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 8080,
                                           'operator': 'GTE'},
                                          {'contextField': 'serverPort',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 8080,
                                           'operator': 'GT'},
                                          {'contextField': 'serverPort',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 8080,
                                           'operator': 'LT'},
                                          {'contextField': 'serverPort',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 8080,
                                           'operator': 'LTE'},
                                          {'contextField': 'operatingSystem',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 'WINDOWS_MOBILE_8',
                                           'operator': 'OSMATCH'},
                                          {'contextField': 'browser',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 'SAFARI',
                                           'operator': 'BROWSERMATCH'},
                                          {'contextField': 'headerMap',
                                           'contextFieldKey': '101441',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Map',
                                           'matchValue': '101441',
                                           'operator': 'EQ'},
                                          {'contextField': 'headerMap',
                                           'contextFieldKey': '101441',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Map',
                                           'matchValue': '101441',
                                           'operator': 'REGEX'},
                                          {'contextField': 'query',
                                           'contextFieldKey': 'queryEQ',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Map',
                                           'matchValue': 'queryEQ',
                                           'operator': 'EQ'},
                                          {'contextField': 'query',
                                           'contextFieldKey': '101441',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Map',
                                           'matchValue': '101441',
                                           'operator': 'REGEX'},
                                          {'contextField': 'tags',
                                           'contextFieldKey': 'tegEQ',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Map',
                                           'matchValue': 'tagEQ',
                                           'operator': 'EQ'},
                                          {'contextField': 'tags',
                                           'contextFieldKey': '101441',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Map',
                                           'matchValue': '101441',
                                           'operator': 'REGEX'}]}],
                    'operator': 'ALL',
                    'rules': [{'contextField': 'remoteAddress',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': '101.101.105.105/24',
                               'operator': 'IPMATCH'},
                              {'contextField': 'remoteAddress',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 'metric',
                               'operator': 'PROXIMITYMATCH'},
                              {'contextField': 'remoteHost',
                               'contextFieldKey': '',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 'abc-sder_qumu.com',
                               'operator': 'EQ'},
                              {'contextField': 'remoteHost',
                               'contextFieldKey': '',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 'abc-sder_qumu.com',
                               'operator': 'REGEX'},
                              {'contextField': 'serverHost',
                               'contextFieldKey': '',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': '10.1.10.10',
                               'operator': 'EQ'},
                              {'contextField': 'serverHost',
                               'contextFieldKey': '',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': '10.10.10.10',
                               'operator': 'REGEX'},
                              {'contextField': 'serverPort',
                               'contextFieldKey': '',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 8080,
                               'operator': 'EQ'},
                              {'contextField': 'serverPort',
                               'contextFieldKey': '',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 8080,
                               'operator': 'GTE'},
                              {'contextField': 'serverPort',
                               'contextFieldKey': '',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 8080,
                               'operator': 'GT'},
                              {'contextField': 'serverPort',
                               'contextFieldKey': '',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 8080,
                               'operator': 'LT'},
                              {'contextField': 'serverPort',
                               'contextFieldKey': '',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 8080,
                               'operator': 'LTE'},
                              {'contextField': 'operatingSystem',
                               'contextFieldKey': '',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 'WINDOWS_MOBILE_8',
                               'operator': 'OSMATCH'},
                              {'contextField': 'browser',
                               'contextFieldKey': '',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 'SAFARI',
                               'operator': 'BROWSERMATCH'},
                              {'contextField': 'headerMap',
                               'contextFieldKey': '101441',
                               'contextFieldType': 'String',
                               'expressionType': 'Map',
                               'matchValue': '101441',
                               'operator': 'EQ'},
                              {'contextField': 'headerMap',
                               'contextFieldKey': '101441',
                               'contextFieldType': 'String',
                               'expressionType': 'Map',
                               'matchValue': '101441',
                               'operator': 'REGEX'},
                              {'contextField': 'query',
                               'contextFieldKey': 'queryEQ',
                               'contextFieldType': 'String',
                               'expressionType': 'Map',
                               'matchValue': 'queryEQ',
                               'operator': 'EQ'},
                              {'contextField': 'query',
                               'contextFieldKey': '101441',
                               'contextFieldType': 'String',
                               'expressionType': 'Map',
                               'matchValue': '101441',
                               'operator': 'REGEX'},
                              {'contextField': 'tags',
                               'contextFieldKey': 'tegEQ',
                               'contextFieldType': 'String',
                               'expressionType': 'Map',
                               'matchValue': 'tagEQ',
                               'operator': 'EQ'},
                              {'contextField': 'tags',
                               'contextFieldKey': '101441',
                               'contextFieldType': 'String',
                               'expressionType': 'Map',
                               'matchValue': '101441',
                               'operator': 'REGEX'}]},
   'name': 'Network Locations Updated'}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Network_Locations')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Network_Locations test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43656')
    @pytest.mark.Network_Locations
    @pytest.mark.PATCH
    def test_TC_43656_PATCH_Network_Locations_Network_Locations_Request_Tag_Regex(self, context):
        """TC-43656 - Network_Locations-PATCH
           Verify that user is able to modify network location with rule and group having parameter 'Tags>Matches Regex' using request PATCH '/networkLocations/'."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is able to modify network location with rule and group having parameter 'Tags>Matches Regex' using request PATCH '/networkLocations/'."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=1024,
                bitrateCapVOD=650,
                id=None,
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'IPMATCH',
                        'contextFieldType': 'String',
                        'matchValue': '101.101.105.105/24',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'PROXIMITYMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'metric',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'remoteHost',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'abc-sder_qumu.com',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'remoteHost',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': 'abc-sder_qumu.com',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverHost',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': '10.1.10.10',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverHost',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': '10.10.10.10',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 8080,
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'GTE',
                        'contextFieldType': 'String',
                        'matchValue': 8080,
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'GT',
                        'contextFieldType': 'String',
                        'matchValue': 8080,
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'LT',
                        'contextFieldType': 'String',
                        'matchValue': 8080,
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'LTE',
                        'contextFieldType': 'String',
                        'matchValue': 8080,
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'operatingSystem',
                        'operator': 'OSMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'WINDOWS_MOBILE_8',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'SAFARI',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': '101441',
                        'contextFieldKey': '101441'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': '101441',
                        'contextFieldKey': '101441'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'query',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'queryEQ',
                        'contextFieldKey': 'queryEQ'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'query',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': '101441',
                        'contextFieldKey': '101441'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'tags',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'tagEQ',
                        'contextFieldKey': 'tegEQ'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'tags',
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
                            'contextField': 'remoteAddress',
                            'operator': 'IPMATCH',
                            'contextFieldType': 'String',
                            'matchValue': '101.101.105.105/24',
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'remoteAddress',
                            'operator': 'PROXIMITYMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'metric',
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'remoteHost',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'abc-sder_qumu.com',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'remoteHost',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': 'abc-sder_qumu.com',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverHost',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': '10.1.10.10',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverHost',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': '10.10.10.10',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverPort',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 8080,
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverPort',
                            'operator': 'GTE',
                            'contextFieldType': 'String',
                            'matchValue': 8080,
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverPort',
                            'operator': 'GT',
                            'contextFieldType': 'String',
                            'matchValue': 8080,
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverPort',
                            'operator': 'LT',
                            'contextFieldType': 'String',
                            'matchValue': 8080,
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverPort',
                            'operator': 'LTE',
                            'contextFieldType': 'String',
                            'matchValue': 8080,
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'operatingSystem',
                            'operator': 'OSMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'WINDOWS_MOBILE_8',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'SAFARI',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': '101441',
                            'contextFieldKey': '101441'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': '101441',
                            'contextFieldKey': '101441'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'query',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'queryEQ',
                            'contextFieldKey': 'queryEQ'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'query',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': '101441',
                            'contextFieldKey': '101441'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'tags',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'tagEQ',
                            'contextFieldKey': 'tegEQ'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'tags',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': '101441',
                            'contextFieldKey': '101441'
                        }],
                        'groups': []
                    }]
                },
                name='Network Locations Updated')


            # updateEntity the Network_Locations.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Network_Locations.updateEntity(
                    id='networkpatchUpdate',
                    body=networkLocationDetails
                )
            )

        # Define a test step
        with pytest.allure.step("""Test2: Verify that user is able to modify network location with rule and group having parameter 'Tags>Matches Regex' using request PATCH '/networkLocations/'."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=1024,
                bitrateCapVOD=650,
                id=None,
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'IPMATCH',
                        'contextFieldType': 'String',
                        'matchValue': '101.101.105.105/24',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'PROXIMITYMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'metric',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'remoteHost',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'abc-sder_qumu.com',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'remoteHost',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': 'abc-sder_qumu.com',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverHost',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': '10.1.10.10',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverHost',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': '10.10.10.10',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 8080,
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'GTE',
                        'contextFieldType': 'String',
                        'matchValue': 8080,
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'GT',
                        'contextFieldType': 'String',
                        'matchValue': 8080,
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'LT',
                        'contextFieldType': 'String',
                        'matchValue': 8080,
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'LTE',
                        'contextFieldType': 'String',
                        'matchValue': 8080,
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'operatingSystem',
                        'operator': 'OSMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'WINDOWS_MOBILE_8',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'SAFARI',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': '101441',
                        'contextFieldKey': '101441'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': '101441',
                        'contextFieldKey': '101441'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'query',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'queryEQ',
                        'contextFieldKey': 'queryEQ'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'query',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': '101441',
                        'contextFieldKey': '101441'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'tags',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'tagEQ',
                        'contextFieldKey': 'tegEQ'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'tags',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': 'autovcc!234',
                        'contextFieldKey': 'autovcc!234'
                    }],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'remoteAddress',
                            'operator': 'IPMATCH',
                            'contextFieldType': 'String',
                            'matchValue': '101.101.105.105/24',
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'remoteAddress',
                            'operator': 'PROXIMITYMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'metric',
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'remoteHost',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'abc-sder_qumu.com',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'remoteHost',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': 'abc-sder_qumu.com',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverHost',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': '10.1.10.10',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverHost',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': '10.10.10.10',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverPort',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 8080,
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverPort',
                            'operator': 'GTE',
                            'contextFieldType': 'String',
                            'matchValue': 8080,
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverPort',
                            'operator': 'GT',
                            'contextFieldType': 'String',
                            'matchValue': 8080,
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverPort',
                            'operator': 'LT',
                            'contextFieldType': 'String',
                            'matchValue': 8080,
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverPort',
                            'operator': 'LTE',
                            'contextFieldType': 'String',
                            'matchValue': 8080,
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'operatingSystem',
                            'operator': 'OSMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'WINDOWS_MOBILE_8',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'SAFARI',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': '101441',
                            'contextFieldKey': '101441'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': '101441',
                            'contextFieldKey': '101441'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'query',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'queryEQ',
                            'contextFieldKey': 'queryEQ'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'query',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': '101441',
                            'contextFieldKey': '101441'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'tags',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'tagEQ',
                            'contextFieldKey': 'tegEQ'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'tags',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': 'autovcc!234',
                            'contextFieldKey': 'autovcc!234'
                        }],
                        'groups': []
                    }]
                },
                name='Network Locations Updated2')


            # updateEntity the Network_Locations.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Network_Locations.updateEntity(
                    id='networkpatchUpdate',
                    body=networkLocationDetails
                )
            )