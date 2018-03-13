# -*- coding: UTF-8 -*-

"""PFE Component Tests - Network_Locations.

* TC-43508 - Network_Locations POST:

  Verify that correct message is displayed in response with invalid value for parameter 'matchingRule' using request POST '/networkLocations'.


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
   'id': 'matchingRule',
   'matchingRule': {'groups': [{'groups': [],
                                'operator': 'ABCD',
                                'rules': [{'contextField': 'remoteAddress',
                                           'contextFieldKey': None,
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': '101.101.105.105/24',
                                           'operator': 'IPMATCH'}]}],
                    'operator': '1234',
                    'rules': [{'contextField': 'remoteAddress',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': '10.1.10.10/32',
                               'operator': 'IPMATCH'}]},
   'name': 'Network Matching Rule'}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Network_Locations')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Network_Locations test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43508')
    @pytest.mark.Network_Locations
    @pytest.mark.POST
    def test_TC_43508_POST_Network_Locations_Matching_Rule_Invalid(self, context):
        """TC-43508 - Network_Locations-POST
           Verify that correct message is displayed in response with invalid value for parameter 'matchingRule' using request POST '/networkLocations'."""
        # Define a test step
        with pytest.allure.step("""Verify that correct message is displayed in response with invalid value for parameter 'matchingRule' using request POST '/networkLocations'."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=0,
                bitrateCapVOD=0,
                id='matchingRule',
                matchingRule={
                    'operator':
                    '1234',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'IPMATCH',
                        'contextFieldType': 'String',
                        'matchValue': '10.1.10.10/32',
                        'contextFieldKey': None
                    }],
                    'groups': [{
                        'operator':
                        'ABCD',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'remoteAddress',
                            'operator': 'IPMATCH',
                            'contextFieldType': 'String',
                            'matchValue': '101.101.105.105/24',
                            'contextFieldKey': None
                        }],
                        'groups': []
                    }]
                },
                name='Network Matching Rule')


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
                    should.start_with('Invalid request. Can not construct instance of com.mpi.mp.expression.CompoundEvaluationCondition from String value'),
                    should.contain('value not one of declared Enum instance names: [ANY, ALL, NONE]')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
