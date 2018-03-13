# -*- coding: UTF-8 -*-

"""PFE Component Tests - Network_Locations.

* TC-42284 - Network_Locations POST:

  Verify that Create button is not displayed on 'Proximities zones' page under Intelligent Content Routing menu for user with "Manage Configuration" permission, while "Config admin can create" flag is set to false within the token expiration time.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X POST -d @<JSON_data_file> -H "Content-Type:
       application/json" "<PF_host>://<client_host>/networkLocations"

Same, with test data:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X POST -d @<JSON_data_file> -H "Content-Type:
       application/json" "<PF_host>://<client_host>/networkLocations"

JSON data sent to PathFinder in this test:

  {'bitrateCapLive': 1024,
   'bitrateCapVOD': 650,
   'id': 'adminFlagSetToFalse',
   'matchingRule': {'groups': [{'groups': [],
                                'operator': 'ALL',
                                'rules': [{'contextField': 'remoteAddress',
                                           'contextFieldKey': None,
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': '102.102.0.0/32',
                                           'operator': 'IPMATCH'},
                                          {'contextField': 'remoteAddress',
                                           'contextFieldKey': None,
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': '1238w90',
                                           'operator': 'PROXIMITYMATCH'},
                                          {'contextField': 'remoteHost',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 'autovcc',
                                           'operator': 'EQ'},
                                          {'contextField': 'remoteHost',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': '10.10.10.10',
                                           'operator': 'REGEX'},
                                          {'contextField': 'serverHost',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 'autovcc',
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
                                           'matchValue': 80,
                                           'operator': 'EQ'},
                                          {'contextField': 'serverPort',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 80,
                                           'operator': 'GTE'},
                                          {'contextField': 'serverPort',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 80,
                                           'operator': 'GT'},
                                          {'contextField': 'serverPort',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 80,
                                           'operator': 'LT'},
                                          {'contextField': 'serverPort',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 80,
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
                               'matchValue': '101.101.0.0/32',
                               'operator': 'IPMATCH'},
                              {'contextField': 'remoteAddress',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': '1238w90',
                               'operator': 'PROXIMITYMATCH'},
                              {'contextField': 'remoteHost',
                               'contextFieldKey': '',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 'autovcc',
                               'operator': 'EQ'},
                              {'contextField': 'remoteHost',
                               'contextFieldKey': '',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': '10.10.10.10',
                               'operator': 'REGEX'},
                              {'contextField': 'serverHost',
                               'contextFieldKey': '',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 'autovcc',
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
                               'matchValue': 80,
                               'operator': 'EQ'},
                              {'contextField': 'serverPort',
                               'contextFieldKey': '',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 80,
                               'operator': 'GTE'},
                              {'contextField': 'serverPort',
                               'contextFieldKey': '',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 80,
                               'operator': 'GT'},
                              {'contextField': 'serverPort',
                               'contextFieldKey': '',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 80,
                               'operator': 'LT'},
                              {'contextField': 'serverPort',
                               'contextFieldKey': '',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 80,
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
   'name': 'Post: Unable To Create Network Location'}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Network_Locations')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Network_Locations test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42284')
    @pytest.mark.Network_Locations
    @pytest.mark.POST
    def test_TC_42284_POST_Network_Locations_Admin_Create_Flag_Set_To_False(self, context):
        """TC-42284 - Network_Locations-POST
           Verify that Create button is not displayed on 'Proximities zones' page under Intelligent Content Routing menu for user with "Manage Configuration" permission, while "Config admin can create" flag is set to false within the token expiration time."""
        # Define a test step
        with pytest.allure.step("""Verify that Create button is not displayed on 'Proximities zones' page under Intelligent Content Routing menu for user with "Manage Configuration" permission, while "Config admin can create" flag is set to false within the token expiration time."""):

            ### Positive test example

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=1024,
                bitrateCapVOD=650,
                id='adminFlagSetToFalse',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'IPMATCH',
                        'contextFieldType': 'String',
                        'matchValue': '101.101.0.0/32',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'PROXIMITYMATCH',
                        'contextFieldType': 'String',
                        'matchValue': '1238w90',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'remoteHost',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'autovcc',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'remoteHost',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': '10.10.10.10',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverHost',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'autovcc',
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
                        'matchValue': 80,
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'GTE',
                        'contextFieldType': 'String',
                        'matchValue': 80,
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'GT',
                        'contextFieldType': 'String',
                        'matchValue': 80,
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'LT',
                        'contextFieldType': 'String',
                        'matchValue': 80,
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'LTE',
                        'contextFieldType': 'String',
                        'matchValue': 80,
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
                            'matchValue': '102.102.0.0/32',
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'remoteAddress',
                            'operator': 'PROXIMITYMATCH',
                            'contextFieldType': 'String',
                            'matchValue': '1238w90',
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'remoteHost',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'autovcc',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'remoteHost',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': '10.10.10.10',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverHost',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'autovcc',
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
                            'matchValue': 80,
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverPort',
                            'operator': 'GTE',
                            'contextFieldType': 'String',
                            'matchValue': 80,
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverPort',
                            'operator': 'GT',
                            'contextFieldType': 'String',
                            'matchValue': 80,
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverPort',
                            'operator': 'LT',
                            'contextFieldType': 'String',
                            'matchValue': 80,
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverPort',
                            'operator': 'LTE',
                            'contextFieldType': 'String',
                            'matchValue': 80,
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
                name='Post: Unable To Create Network Location')


            # createEntity the Network_Locations.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Network_Locations.createEntity(
                    body=networkLocationDetails
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that Create button is not displayed on 'Proximities zones' page under Intelligent Content Routing menu for user with "Manage Configuration" permission, while "Config admin can create" flag is set to false within the token expiration time."""):

            ### Negative test example

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=1024,
                bitrateCapVOD=650,
                id='adminFlagSetToFalse',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'IPMATCH',
                        'contextFieldType': 'String',
                        'matchValue': '101.101.0.0/32',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'PROXIMITYMATCH',
                        'contextFieldType': 'String',
                        'matchValue': '1238w90',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'remoteHost',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'autovcc',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'remoteHost',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': '10.10.10.10',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverHost',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'autovcc',
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
                        'matchValue': 80,
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'GTE',
                        'contextFieldType': 'String',
                        'matchValue': 80,
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'GT',
                        'contextFieldType': 'String',
                        'matchValue': 80,
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'LT',
                        'contextFieldType': 'String',
                        'matchValue': 80,
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'LTE',
                        'contextFieldType': 'String',
                        'matchValue': 80,
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
                            'matchValue': '102.102.0.0/32',
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'remoteAddress',
                            'operator': 'PROXIMITYMATCH',
                            'contextFieldType': 'String',
                            'matchValue': '1238w90',
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'remoteHost',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'autovcc',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'remoteHost',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': '10.10.10.10',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverHost',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'autovcc',
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
                            'matchValue': 80,
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverPort',
                            'operator': 'GTE',
                            'contextFieldType': 'String',
                            'matchValue': 80,
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverPort',
                            'operator': 'GT',
                            'contextFieldType': 'String',
                            'matchValue': 80,
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverPort',
                            'operator': 'LT',
                            'contextFieldType': 'String',
                            'matchValue': 80,
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverPort',
                            'operator': 'LTE',
                            'contextFieldType': 'String',
                            'matchValue': 80,
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
                name='Post: Unable To Create Network Location')


            # prepare the request, so we can modify it
            request = context.cl.Network_Locations.createEntity(
                    body=networkLocationDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # createEntity the Network_Locations, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('may not be empty'),
                    should.start_with('Invalid page parameter specified'),
                    should.contain('Invalid Authorization Token')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
