# -*- coding: UTF-8 -*-

"""PFE Component Tests - Network_Locations.

* TC-43572 - Network_Locations POST:

  Verify that correct error message is displayed in response on providing invalid values in parameters 'id' using request POST /networkLocations.


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
   'id': 'POST <>!@#$%^&*;/?',
   'matchingRule': {'groups': [{'groups': [],
                                'operator': 'ANY',
                                'rules': [{'contextField': 'remoteAddress',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': '10.0.0.0/32',
                                           'operator': 'IPMATCH'}]}],
                    'operator': 'ALL',
                    'rules': []},
   'name': 'Network ID Invalid Values'}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Network_Locations')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Network_Locations test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43572')
    @pytest.mark.Network_Locations
    @pytest.mark.POST
    def test_TC_43572_POST_Network_Locations_Id_Invalid_Values(self, context):
        """TC-43572 - Network_Locations-POST
           Verify that correct error message is displayed in response on providing invalid values in parameters 'id' using request POST /networkLocations."""
        # Define a test step
        with pytest.allure.step("""Verify that correct error message is displayed in response on providing invalid values in parameters 'id' using request POST /networkLocations."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=0,
                bitrateCapVOD=0,
                id='POST <>!@#$%^&*;/?',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [],
                    'groups': [{
                        'operator':
                        'ANY',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'remoteAddress',
                            'operator': 'IPMATCH',
                            'contextFieldType': 'String',
                            'matchValue': '10.0.0.0/32',
                            'contextFieldKey': ''
                        }],
                        'groups': []
                    }]
                },
                name='Network ID Invalid Values')


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
                    should.start_with('Invalid identifier, the pattern must match \"^\\p{Alnum}+[\\w\\-\\:\\.]*$\"')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
