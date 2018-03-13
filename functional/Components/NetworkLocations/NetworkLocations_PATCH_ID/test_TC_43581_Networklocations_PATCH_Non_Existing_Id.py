# -*- coding: UTF-8 -*-

"""PFE Component Tests - Network_Locations.

* TC-43581 - Network_Locations PATCH:

  Verify that validation message is displayed in response class on modifying network location with non-existing 'Id' parameter using request PATCH /networkLocations.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations/networkUpdate1"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations/networkUpdate1"

JSON data sent to PathFinder in this test:

  {'bitrateCapLive': 1024,
   'bitrateCapVOD': 650,
   'id': 'NetworkIdNotExist',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43581')
    @pytest.mark.Network_Locations
    @pytest.mark.PATCH
    def test_TC_43581_PATCH_Network_Locations_Non_Existing_Id(self, context):
        """TC-43581 - Network_Locations-PATCH
           Verify that validation message is displayed in response class on modifying network location with non-existing 'Id' parameter using request PATCH /networkLocations."""

        # Define a test step
        with pytest.allure.step("""First create network location using request POST /networkLocations."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=1024,
                bitrateCapVOD=650,
                id='networkpatchUpdate',
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
                        }],
                        'groups': []
                    }]
                },
                name='networkpatchUpdate')

            # createEntity the Network_Locations.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Network_Locations.createEntity(
                    body=networkLocationDetails
                )
            )


        # Define a test step
        with pytest.allure.step("""Now verify that validation message is displayed in response class on modifying network location with non-existing 'Id' parameter using request PATCH /networkLocations."""):

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
                        'matchValue': '101.101.0.0/32',
                        'contextFieldKey': None
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
                        }],
                        'groups': []
                    }]
                },
                name='Network Locations Update')


            # prepare the request, so we can modify it
            request = context.cl.Network_Locations.updateEntity(
                     id='invalid',
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
            except (HTTPBadRequest, HTTPForbidden, HTTPNotFound) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Delivery Service entity not found')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
