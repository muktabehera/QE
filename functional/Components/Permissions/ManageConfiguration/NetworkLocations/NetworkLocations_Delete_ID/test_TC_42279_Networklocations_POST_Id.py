# -*- coding: UTF-8 -*-

"""PFE Component Tests - Network_Locations.

* TC-42279 - Network_Locations POST:

  Verify that User is able to View, all the entities under Intelligent Content Routing menu, using token with "Manage Configuration" permission within the token expiration time.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X POST -d @<JSON_data_file> -H "Content-Type:
       application/json" "<PF_host>://<client_host>/networkLocations"

Same, with test data:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X POST -d @<JSON_data_file> -H "Content-Type:
       application/json" "<PF_host>://<client_host>/networkLocations"

JSON data sent to PathFinder in this test:

  {'bitrateCapLive': 146,
   'bitrateCapVOD': 285,
   'description': None,
   'id': 'deleteNetworkLocationPermission',
   'matchingRule': {'groups': [{'groups': [],
                                'operator': 'ALL',
                                'rules': [{'contextField': 'remoteAddress',
                                           'contextFieldKey': None,
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': '10.0.0.0/32',
                                           'operator': 'IPMATCH'},
                                          {'contextField': 'remoteHost',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 'autoQEd',
                                           'operator': 'EQ'},
                                          {'contextField': 'serverHost',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': '101.101.101.101',
                                           'operator': 'EQ'},
                                          {'contextField': 'serverPort',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 80,
                                           'operator': 'EQ'},
                                          {'contextField': 'operatingSystem',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 'BLACKBERRY',
                                           'operator': 'OSMATCH'},
                                          {'contextField': 'browser',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 'CHROME',
                                           'operator': 'BROWSERMATCH'},
                                          {'contextField': 'headerMap',
                                           'contextFieldKey': 'header',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Map',
                                           'matchValue': 'header',
                                           'operator': 'EQ'},
                                          {'contextField': 'queryParamMap',
                                           'contextFieldKey': 'query',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Map',
                                           'matchValue': 'query',
                                           'operator': 'EQ'},
                                          {'contextField': 'tags',
                                           'contextFieldKey': 'tags',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Map',
                                           'matchValue': 'tags',
                                           'operator': 'EQ'}]}],
                    'operator': 'ALL',
                    'rules': []},
   'name': 'Post: Network Location Delete'}

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42279')
    @pytest.mark.Network_Locations
    @pytest.mark.POST
    def test_TC_42279_POST_Network_Locations_Id(self, context):
        """TC-42279 - Network_Locations-POST
           Verify that User is able to View, all the entities under Intelligent Content Routing menu, using token with "Manage Configuration" permission within the token expiration time."""
        # Define a test step
        with pytest.allure.step("""Verify that User is able to View, all the entities under Intelligent Content Routing menu, using token with "Manage Configuration" permission within the token expiration time."""):

            ### Positive test example

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=146,
                bitrateCapVOD=285,
                id='deleteNetworkLocationPermission',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'remoteAddress',
                            'operator': 'IPMATCH',
                            'contextFieldType': 'String',
                            'matchValue': '10.0.0.0/32',
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'remoteHost',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'autoQEd',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverHost',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': '101.101.101.101',
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
                            'matchValue': 'CHROME',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'header',
                            'contextFieldKey': 'header'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'queryParamMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'query',
                            'contextFieldKey': 'query'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'tags',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'tags',
                            'contextFieldKey': 'tags'
                        }],
                        'groups': []
                    }]
                },
                name='Post: Network Location Delete')


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

        with pytest.allure.step("""Verify that User is able to View, all the entities under Intelligent Content Routing menu, using token with "Manage Configuration" permission within the token expiration time."""):

            ### Negative test example

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=146,
                bitrateCapVOD=285,
                id='deleteNetworkLocationPermission',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'remoteAddress',
                            'operator': 'IPMATCH',
                            'contextFieldType': 'String',
                            'matchValue': '10.0.0.0/32',
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'remoteHost',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'autoQEd',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverHost',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': '101.101.101.101',
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
                            'matchValue': 'CHROME',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'header',
                            'contextFieldKey': 'header'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'queryParamMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'query',
                            'contextFieldKey': 'query'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'tags',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'tags',
                            'contextFieldKey': 'tags'
                        }],
                        'groups': []
                    }]
                },
                name='Post: Network Location Delete')


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
