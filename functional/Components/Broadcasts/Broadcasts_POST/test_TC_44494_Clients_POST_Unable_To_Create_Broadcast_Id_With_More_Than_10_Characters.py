# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-44494 - Clients POST:

  Verify that user is unable to create broadcast ID with more than 100 characters using request POST "/broadcasts".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

JSON data sent to PathFinder in this test:

  {'id': 'broadcastClient',
   'matchingRule': {'groups': [],
                    'operator': 'ALL',
                    'rules': [{'contextField': 'remoteAddress',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': '0.0.0.0/0',
                               'operator': 'IPMATCH'}]},
   'name': 'broadcastClient',
   'sourceSelectionRule': [{'groups': [],
                            'operator': 'ANY',
                            'rules': [{'contextField': 'mimetype',
                                       'contextFieldKey': None,
                                       'contextFieldType': 'String',
                                       'expressionType': 'Single',
                                       'matchValue': 'video/mp4',
                                       'operator': 'MIMEMATCH'},
                                      {'contextField': 'mimetype',
                                       'contextFieldKey': None,
                                       'contextFieldType': 'String',
                                       'expressionType': 'Single',
                                       'matchValue': 'application/vnd.apple.mpegurl',
                                       'operator': 'MIMEMATCH'},
                                      {'contextField': 'mimetype',
                                       'contextFieldKey': None,
                                       'contextFieldType': 'String',
                                       'expressionType': 'Single',
                                       'matchValue': 'application/x-mpegURL',
                                       'operator': 'MIMEMATCH'}]}]}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44494')
    @pytest.mark.Clients
    @pytest.mark.POST
    def test_TC_44494_POST_Clients_Unable_To_Create_Broadcast_Id_With_More_Than_10_Characters(self, context):
        """TC-44494 - Clients-POST
           Verify that user is unable to create broadcast ID with more than 100 characters using request POST "/broadcasts"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to create broadcast ID with more than 100 characters using request POST "/broadcasts"."""):

            ### Positive test example

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='broadcastClient',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'IPMATCH',
                        'contextFieldType': 'String',
                        'matchValue': '0.0.0.0/0',
                        'contextFieldKey': None
                    }],
                    'groups': []
                },
                name='broadcastClient',
                sourceSelectionRule=[{
                    'operator':
                    'ANY',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'mimetype',
                        'operator': 'MIMEMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'video/mp4',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'mimetype',
                        'operator': 'MIMEMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'application/vnd.apple.mpegurl',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'mimetype',
                        'operator': 'MIMEMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'application/x-mpegURL',
                        'contextFieldKey': None
                    }],
                    'groups': []
                }])


            # createEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Clients.createEntity(
                    body=clientDetails
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is unable to create broadcast ID with more than 100 characters using request POST "/broadcasts"."""):

            ### Negative test example

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='broadcastClient',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'IPMATCH',
                        'contextFieldType': 'String',
                        'matchValue': '0.0.0.0/0',
                        'contextFieldKey': None
                    }],
                    'groups': []
                },
                name='broadcastClient',
                sourceSelectionRule=[{
                    'operator':
                    'ANY',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'mimetype',
                        'operator': 'MIMEMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'video/mp4',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'mimetype',
                        'operator': 'MIMEMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'application/vnd.apple.mpegurl',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'mimetype',
                        'operator': 'MIMEMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'application/x-mpegURL',
                        'contextFieldKey': None
                    }],
                    'groups': []
                }])


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
                    should.start_with('may not be empty'),
                    should.start_with('Invalid page parameter specified'),
                    should.contain('Invalid Authorization Token')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
