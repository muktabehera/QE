# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43085 - Clients POST:

  Verify that correct message is displayed for child group in response with invalid value in parameter 'matchingRule' using request POST '/clients/'.


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
   'id': 'clientGroupInvalidMatchingRule',
   'matchingRule': {'groups': [{'groups': [],
                                'operator': '1234',
                                'rules': [{'contextField': 'remoteAddress',
                                           'contextFieldKey': None,
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': '10.10.0.0/16',
                                           'operator': 'IPMATCH'}]}],
                    'operator': 'ALL',
                    'rules': []},
   'name': 'POST: Client Group Matching Rule Invalid',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43085')
    @pytest.mark.Clients
    @pytest.mark.POST
    def test_TC_43085_POST_Clients_Client_Group_Invalid_Matching_Rule(self, context):
        """TC-43085 - Clients-POST
           Verify that correct message is displayed for child group in response with invalid value in parameter 'matchingRule' using request POST '/clients/'."""
        # Define a test step


        with pytest.allure.step("""Test1: Verify that correct message is displayed for child group in response with invalid value in parameter 'matchingRule' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientGroupInvalidMatchingRule',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [],
                    'groups': [{
                        'operator':
                        '1234',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'remoteAddress',
                            'operator': 'IPMATCH',
                            'contextFieldType': 'String',
                            'matchValue': '10.10.0.0/16',
                            'contextFieldKey': None
                        }],
                        'groups': []
                    }]
                },
                name='POST: Client Group Matching Rule Invalid',
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
                    should.start_with('Invalid request. Can not construct instance of com.mpi.mp.expression.CompoundEvaluationCondition from String value' ),
                    should.contain('value not one of declared Enum instance names: [ANY, ALL, NONE]'))

            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))



        # Define a test step
        with pytest.allure.step("""Test2: Verify that correct message is displayed for child group in response with invalid value in parameter 'matchingRule' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientGroupInvalidMatchingRule2',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [],
                    'groups': [{
                        'operator':
                        'abcd13',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'remoteAddress',
                            'operator': 'IPMATCH',
                            'contextFieldType': 'String',
                            'matchValue': '10.10.0.0/16',
                            'contextFieldKey': None
                        }],
                        'groups': []
                    }]
                },
                name='POST: Client Group Matching Rule Invalid2',
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
                    should.start_with('Invalid request. Can not construct instance of com.mpi.mp.expression.CompoundEvaluationCondition from String value'),
                    should.contain('value not one of declared Enum instance names: [ANY, ALL, NONE]'))

            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))



        # Define a test step
        with pytest.allure.step("""Test3: Verify that correct message is displayed for child group in response with invalid value in parameter 'matchingRule' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientGroupInvalidMatchingRule3',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [],
                    'groups': [{
                        'operator':
                        'none',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'remoteAddress',
                            'operator': 'IPMATCH',
                            'contextFieldType': 'String',
                            'matchValue': '10.10.0.0/16',
                            'contextFieldKey': None
                        }],
                        'groups': []
                    }]
                },
                name='POST: Client Group Matching Rule Invalid3',
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
                    should.start_with('Invalid request. Can not construct instance of com.mpi.mp.expression.CompoundEvaluationCondition from String value'),
                    should.contain('value not one of declared Enum instance names: [ANY, ALL, NONE]'))
                
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
