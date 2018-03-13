# -*- coding: UTF-8 -*-

"""PFE Component Tests - Network_Locations.

* TC-43649 - Network_Locations PATCH:

  Verify that user is able to modify network location with rule and group having parameter 'Operating System>Matches' using request PATCH '/networkLocations/'.


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
                                           'matchValue': 'ANDROID',
                                           'operator': 'OSMATCH'},
                                          {'contextField': 'browser',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 'IE',
                                           'operator': 'BROWSERMATCH'},
                                          {'contextField': 'headerMap',
                                           'contextFieldKey': 'key',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Map',
                                           'matchValue': 'key',
                                           'operator': 'EQ'},
                                          {'contextField': 'headerMap',
                                           'contextFieldKey': 'regex',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Map',
                                           'matchValue': 'regex',
                                           'operator': 'REGEX'},
                                          {'contextField': 'query',
                                           'contextFieldKey': 'queryEQ',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Map',
                                           'matchValue': 'queryEQ',
                                           'operator': 'EQ'},
                                          {'contextField': 'query',
                                           'contextFieldKey': 'regex',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Map',
                                           'matchValue': 'regex',
                                           'operator': 'REGEX'},
                                          {'contextField': 'tags',
                                           'contextFieldKey': 'tegEQ',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Map',
                                           'matchValue': 'tagEQ',
                                           'operator': 'EQ'},
                                          {'contextField': 'tags',
                                           'contextFieldKey': 'regex',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Map',
                                           'matchValue': 'regex',
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
                               'matchValue': 'ANDROID',
                               'operator': 'OSMATCH'},
                              {'contextField': 'browser',
                               'contextFieldKey': '',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 'IE',
                               'operator': 'BROWSERMATCH'},
                              {'contextField': 'headerMap',
                               'contextFieldKey': 'key',
                               'contextFieldType': 'String',
                               'expressionType': 'Map',
                               'matchValue': 'key',
                               'operator': 'EQ'},
                              {'contextField': 'headerMap',
                               'contextFieldKey': 'regex',
                               'contextFieldType': 'String',
                               'expressionType': 'Map',
                               'matchValue': 'regex',
                               'operator': 'REGEX'},
                              {'contextField': 'query',
                               'contextFieldKey': 'queryEQ',
                               'contextFieldType': 'String',
                               'expressionType': 'Map',
                               'matchValue': 'queryEQ',
                               'operator': 'EQ'},
                              {'contextField': 'query',
                               'contextFieldKey': 'regex',
                               'contextFieldType': 'String',
                               'expressionType': 'Map',
                               'matchValue': 'regex',
                               'operator': 'REGEX'},
                              {'contextField': 'tags',
                               'contextFieldKey': 'tegEQ',
                               'contextFieldType': 'String',
                               'expressionType': 'Map',
                               'matchValue': 'tagEQ',
                               'operator': 'EQ'},
                              {'contextField': 'tags',
                               'contextFieldKey': 'regex',
                               'contextFieldType': 'String',
                               'expressionType': 'Map',
                               'matchValue': 'regex',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43649')
    @pytest.mark.Network_Locations
    @pytest.mark.PATCH
    def test_TC_43649_PATCH_Network_Locations_Network_Locations_Android_Os(self, context):
        """TC-43649 - Network_Locations-PATCH
           Verify that user is able to modify network location with rule and group having parameter 'Operating System>Matches' using request PATCH '/networkLocations/'."""
        # Define a test step
        with pytest.allure.step("""ANDROID: Verify that user is able to modify network location with rule and group having parameter 'Operating System>Matches' using request PATCH '/networkLocations/'."""):

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
                        'matchValue': 'ANDROID',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'key',
                        'contextFieldKey': 'key'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                            'matchValue': 'ANDROID',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'IE',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'key',
                            'contextFieldKey': 'key'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
                        }],
                        'groups': []
                    }]
                },
                name='Network Locations Updated1')


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
        with pytest.allure.step("""BLACKBERRY: Verify that user is able to modify network location with rule and group having parameter 'Operating System>Matches' using request PATCH '/networkLocations/'."""):

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
                        'matchValue': 'BLACKBERRY',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'key',
                        'contextFieldKey': 'key'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                            'matchValue': 'BLACKBERRY',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'IE',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'key',
                            'contextFieldKey': 'key'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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

# Define a test step
        with pytest.allure.step("""WINDOWS_7: Verify that user is able to modify network location with rule and group having parameter 'Operating System>Matches' using request PATCH '/networkLocations/'."""):

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
                        'matchValue': 'WINDOWS_7',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'key',
                        'contextFieldKey': 'key'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                            'matchValue': 'WINDOWS_7',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'IE',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'key',
                            'contextFieldKey': 'key'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
        with pytest.allure.step("""WINDOWS_8: Verify that user is able to modify network location with rule and group having parameter 'Operating System>Matches' using request PATCH '/networkLocations/'."""):


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
                        'matchValue': 'WINDOWS_8',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'key',
                        'contextFieldKey': 'key'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                            'matchValue': 'WINDOWS_8',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'IE',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'key',
                            'contextFieldKey': 'key'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
                        }],
                        'groups': []
                    }]
                },
                name='Network Locations Updated4')


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
        with pytest.allure.step("""MAC_OS_X: Verify that user is able to modify network location with rule and group having parameter 'Operating System>Matches' using request PATCH '/networkLocations/'."""):

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
                        'matchValue': 'MAC_OS_X',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'key',
                        'contextFieldKey': 'key'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                            'matchValue': 'MAC_OS_X',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'IE',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'key',
                            'contextFieldKey': 'key'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
                        }],
                        'groups': []
                    }]
                },
                name='Network Locations Updated5')


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
        with pytest.allure.step("""LINUX: Verify that user is able to modify network location with rule and group having parameter 'Operating System>Matches' using request PATCH '/networkLocations/'."""):

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
                        'matchValue': 'LINUX',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'key',
                        'contextFieldKey': 'key'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                            'matchValue': 'LINUX',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'IE',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'key',
                            'contextFieldKey': 'key'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
                        }],
                        'groups': []
                    }]
                },
                name='Network Locations Updated6')


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
        with pytest.allure.step("""MAC_OS_X_IPHONE: Verify that user is able to modify network location with rule and group having parameter 'Operating System>Matches' using request PATCH '/networkLocations/'."""):

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
                        'matchValue': 'MAC_OS_X_IPHONE',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'key',
                        'contextFieldKey': 'key'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                            'matchValue': 'MAC_OS_X_IPHONE',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'IE',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'key',
                            'contextFieldKey': 'key'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
                        }],
                        'groups': []
                    }]
                },
                name='Network Locations Updated7')


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
        with pytest.allure.step("""MAC_OS_X_IPAD: Verify that user is able to modify network location with rule and group having parameter 'Operating System>Matches' using request PATCH '/networkLocations/'."""):

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
                        'matchValue': 'MAC_OS_X_IPAD',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'key',
                        'contextFieldKey': 'key'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                            'matchValue': 'MAC_OS_X_IPAD',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'IE',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'key',
                            'contextFieldKey': 'key'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
                        }],
                        'groups': []
                    }]
                },
                name='Network Locations Updated8')


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
        with pytest.allure.step("""IOS: Verify that user is able to modify network location with rule and group having parameter 'Operating System>Matches' using request PATCH '/networkLocations/'."""):

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
                        'matchValue': 'IOS',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'key',
                        'contextFieldKey': 'key'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                            'matchValue': 'IOS',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'IE',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'key',
                            'contextFieldKey': 'key'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
                        }],
                        'groups': []
                    }]
                },
                name='Network Locations Updated9')


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
        with pytest.allure.step("""WINDOWS_MOBILE: Verify that user is able to modify network location with rule and group having parameter 'Operating System>Matches' using request PATCH '/networkLocations/'."""):

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
                        'matchValue': 'WINDOWS_MOBILE',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'key',
                        'contextFieldKey': 'key'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                            'matchValue': 'WINDOWS_MOBILE',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'IE',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'key',
                            'contextFieldKey': 'key'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
                        }],
                        'groups': []
                    }]
                },
                name='Network Locations Updated12')


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
        with pytest.allure.step("""WINDOWS_MOBILE7: Verify that user is able to modify network location with rule and group having parameter 'Operating System>Matches' using request PATCH '/networkLocations/'."""):


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
                        'matchValue': 'WINDOWS_MOBILE7',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'key',
                        'contextFieldKey': 'key'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                            'matchValue': 'WINDOWS_MOBILE7',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'IE',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'key',
                            'contextFieldKey': 'key'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
                        }],
                        'groups': []
                    }]
                },
                name='Network Locations Updated win7mobile')


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
        with pytest.allure.step("""WINDOWS_PHONE8: Verify that user is able to modify network location with rule and group having parameter 'Operating System>Matches' using request PATCH '/networkLocations/'."""):

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
                        'matchValue': 'WINDOWS_PHONE8',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'key',
                        'contextFieldKey': 'key'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                            'matchValue': 'WINDOWS_PHONE8',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'IE',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'key',
                            'contextFieldKey': 'key'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'queryParamM',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'queryEQ',
                            'contextFieldKey': 'queryEQ'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'query',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
                        }],
                        'groups': []
                    }]
                },
                name='Network Locations Updated win8mobile')


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
        with pytest.allure.step("""WINDOWS_VISTA: Verify that user is able to modify network location with rule and group having parameter 'Operating System>Matches' using request PATCH '/networkLocations/'."""):

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
                        'matchValue': 'WINDOWS_VISTA',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'key',
                        'contextFieldKey': 'key'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                            'matchValue': 'WINDOWS_VISTA',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'IE',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'key',
                            'contextFieldKey': 'key'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
                        }],
                        'groups': []
                    }]
                },
                name='Network Locations Updated vista')


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
        with pytest.allure.step("""WINDOWS_XP: Verify that user is able to modify network location with rule and group having parameter 'Operating System>Matches' using request PATCH '/networkLocations/'."""):

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
                        'matchValue': 'WINDOWS_XP',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'key',
                        'contextFieldKey': 'key'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                        'matchValue': 'regex',
                        'contextFieldKey': 'regex'
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
                            'matchValue': 'WINDOWS_XP',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'IE',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'key',
                            'contextFieldKey': 'key'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
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
                            'matchValue': 'regex',
                            'contextFieldKey': 'regex'
                        }],
                        'groups': []
                    }]
                },
                name='Network Locations Updated Xp')


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