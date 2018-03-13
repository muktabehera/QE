# -*- coding: UTF-8 -*-

"""PFE Component Tests - Network_Locations.

* TC-43677 - Network_Locations POST:

  Verify that user is able to send slides(PPT, PPTx) for distribution using request POST "/distributions" with VideoNet  as public delivery system.


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
   'id': 'broadcastNetworkLocation',
   'matchingRule': {'groups': [{'groups': [],
                                'operator': 'ANY',
                                'rules': [{'contextField': 'remoteAddress',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': '0.0.0.0/0',
                                           'operator': 'IPMATCH'}]}],
                    'operator': 'ALL',
                    'rules': []},
   'name': 'broadcastNetworkLocation'}

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43677')
    @pytest.mark.Network_Locations
    @pytest.mark.POST
    def test_TC_43677_POST_Network_Locations_Distributions_Vnet_Pptx_Slide(self, context):
        """TC-43677 - Network_Locations-POST
           Verify that user is able to send slides(PPT, PPTx) for distribution using request POST "/distributions" with VideoNet  as public delivery system."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to send slides(PPT, PPTx) for distribution using request POST "/distributions" with VideoNet  as public delivery system."""):

            ### Positive test example

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=0,
                bitrateCapVOD=0,
                id='broadcastNetworkLocation',
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
                            'matchValue': '0.0.0.0/0',
                            'contextFieldKey': ''
                        }],
                        'groups': []
                    }]
                },
                name='broadcastNetworkLocation')


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

        with pytest.allure.step("""Verify that user is able to send slides(PPT, PPTx) for distribution using request POST "/distributions" with VideoNet  as public delivery system."""):

            ### Negative test example

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=0,
                bitrateCapVOD=0,
                id='broadcastNetworkLocation',
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
                            'matchValue': '0.0.0.0/0',
                            'contextFieldKey': ''
                        }],
                        'groups': []
                    }]
                },
                name='broadcastNetworkLocation')


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
