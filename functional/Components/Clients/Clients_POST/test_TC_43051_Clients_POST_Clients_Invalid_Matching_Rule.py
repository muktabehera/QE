# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43051 - Clients POST:

  Verify that correct message is displayed in response with invalid value in parameter 'matchingRule' using request POST '/clients/'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

JSON data sent to PathFinder in this test:

  {'id': 'invalidMatchingRule1',
   'matchingRule': {'groups': [],
                    'operator': '1234',
                    'rules': [{'contextField': 'remoteAddress',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': '172.30.2.49/32',
                               'operator': 'IPMATCH'}]},
   'name': 'POST: Client with Invalid Matching Rule 1',
   'sourceSelectionRule': []}

"""

import pytest

from qe_common import *

logger = init_logger()

# Common framwork variables initialization
global env
env = load_config_file(get_config_file_cmdarg())
# Used for generating random test data
faker = Factory.create(env.Locale)


@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43051')
    @pytest.mark.Clients
    @pytest.mark.POST
    def test_TC_43051_POST_Clients_Clients_Invalid_Matching_Rule(self, context):
        """TC-43051 - Clients-POST
           Verify that correct message is displayed in response with invalid value in parameter 'matchingRule' using request POST '/clients/'."""
        # Define a test step
        with pytest.allure.step("""Verify that correct message is displayed in response with invalid value in parameter 'matchingRule' ex-1234 using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='invalidMatchingRule1',
                matchingRule={
                    'operator':
                    '1234',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'IPMATCH',
                        'contextFieldType': 'String',
                        'matchValue': '172.30.2.49/32',
                        'contextFieldKey': None
                    }],
                    'groups': []
                },
                name='POST: Client with Invalid Matching Rule 1',
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
                    should.start_with('Invalid request. Can not construct instance of com.mpi.mp.expression.')
                )

            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))

        # Define a test step
        with pytest.allure.step("""Verify that correct message is displayed in response with invalid value in parameter 'matchingRule' ex-avbcd using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='invalidMatchingRule2',
                matchingRule={
                    'operator':
                    'avbcd',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'IPMATCH',
                        'contextFieldType': 'String',
                        'matchValue': '172.30.2.49/32',
                        'contextFieldKey': None
                    }],
                    'groups': []
                },
                name='POST: Client with Invalid Matching Rule 2',
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
                    should.start_with('Invalid request. Can not construct instance of com.mpi.mp.expression.')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))


        # Define a test step
        with pytest.allure.step("""Verify that correct message is displayed in response with invalid value in parameter 'matchingRule' ex- none using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='invalidMatchingRule3',
                matchingRule={
                    'operator':
                    'none',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'IPMATCH',
                        'contextFieldType': 'String',
                        'matchValue': '172.30.2.49/32',
                        'contextFieldKey': None
                    }],
                    'groups': []
                },
                name='POST: Client with Invalid Matching Rule 3',
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
                    should.start_with('Invalid request. Can not construct instance of com.mpi.mp.expression.')
                    # Invalid request. Can not construct instance of com.mpi.mp.expression.CompoundEvaluationCondition from String value '1234': value not one of declared Enum instance names: [ANY, ALL, NONE]
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
