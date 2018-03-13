# -*- coding: UTF-8 -*-

"""PFE Component Tests - Network_Locations.

* TC-43584 - Network_Locations PATCH:

  Verify that correct message is displayed in response on modifying network location by providing invalid value in parameter 'matchingRule' using request PATCH '/networkLocations'.


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
                                'operator': 'ABC',
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
                    'operator': 'ABC',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43584')
    @pytest.mark.Network_Locations
    @pytest.mark.PATCH
    def test_TC_43584_PATCH_Network_Locations_Network_Locations_Invalid_Matching_Rule(self, context):
        """TC-43584 - Network_Locations-PATCH
           Verify that correct message is displayed in response on modifying network location by providing invalid value in parameter 'matchingRule' using request PATCH '/networkLocations'."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that correct message is displayed in response on modifying network location by providing invalid value in parameter 'matchingRule' using request PATCH '/networkLocations'."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=1024,
                bitrateCapVOD=650,
                id=None,
                matchingRule={
                    'operator':
                    'ABC',
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
                        'ABC',
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
                name='Network Locations Updated')


            # prepare the request, so we can modify it
            request = context.cl.Network_Locations.updateEntity(
                    id='networkpatchUpdate',
                    body=networkLocationDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateEntity the Network_Locations, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Invalid request. Can not construct instance of com.mpi.mp.expression.CompoundEvaluationCondition from String value'),
                    should.contain('value not one of declared Enum instance names: [ANY, ALL, NONE]')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))


        # Define a test step
        with pytest.allure.step("""Test2: Verify that correct message is displayed in response on modifying network location by providing invalid value in parameter 'matchingRule' using request PATCH '/networkLocations'."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=1024,
                bitrateCapVOD=650,
                id=None,
                matchingRule={
                    'operator':
                    '123!@#',
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
                        '123',
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
                name='Network Locations Updated')


            # prepare the request, so we can modify it
            request = context.cl.Network_Locations.updateEntity(
                    id='networkpatchUpdate',
                    body=networkLocationDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateEntity the Network_Locations, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with(
                        'Invalid request. Can not construct instance of com.mpi.mp.expression.CompoundEvaluationCondition from String value'),
                    should.contain('value not one of declared Enum instance names: [ANY, ALL, NONE]')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
