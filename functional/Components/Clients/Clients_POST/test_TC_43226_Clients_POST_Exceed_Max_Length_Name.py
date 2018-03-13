# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43226 - Clients POST:

  Verify that user is unable to create client on providing length greater than 100 character in parameter 'Name' using request POST '/clients/'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

JSON data sent to PathFinder in this test:

  {'bitrateCapLive': 0,
   'bitrateCapVOD': 0,
   'description': None,
   'id': 'clientNameMaxLengthExceed',
   'matchingRule': {'groups': [{'groups': [],
                                'operator': 'ALL',
                                'rules': [{'contextField': 'operatingSystem',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 'WINDOWS_MOBILE_8',
                                           'operator': 'OSMATCH'}]}],
                    'operator': 'ALL',
                    'rules': []},
   'name': 'clientAPI1234!@# clientAPI1234!@# clientAPI1234!@# clientAPI1234!@# '
           'clientAPI1234!@#clientAPI1234!@# ',
   'sourceSelectionRule': []}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43226')
    @pytest.mark.Clients
    @pytest.mark.POST
    def test_TC_43226_POST_Clients_Exceed_Max_Length_Name(self, context):
        """TC-43226 - Clients-POST
           Verify that user is unable to create client on providing length greater than 100 character in parameter 'Name' using request POST '/clients/'."""
        # Define a test step

        with pytest.allure.step("""Verify that user is unable to create client on providing length greater than 100 character in parameter 'Name' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientNameMaxLengthExceed',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'operatingSystem',
                            'operator': 'OSMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'WINDOWS_MOBILE_8',
                            'contextFieldKey': ''
                        }],
                        'groups': []
                    }]
                },
                name=
                'clientAPI1234!@# clientAPI1234!@# clientAPI1234!@# clientAPI1234!@# clientAPI1234!@#clientAPI1234!@# ',
                sourceSelectionRule=[])


            # prepare the request, so we can modify it
            request = context.cl.Clients.createEntity(
                    body=clientDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # createEntity the Clients, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('length must be between 1 and 100')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
