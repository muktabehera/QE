# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43310 - Clients PATCH:

  Verify that correct message is displayed in response on modifying client by providing invalid value in parameter 'matchingRule' using request PATCH '/clients/'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/clientUpdate"

JSON data sent to PathFinder in this test:

  {'matchingRule': {'groups': [],
                    'operator': '1234',
                    'rules': [{'contextField': 'remoteAddress',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': '172.30.2.49/32',
                               'operator': 'IPMATCH'}]},
   'name': 'PATCH: Client with Updated Invalid Matching Rule 1',
   'sourceSelectionRule': []}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43310')
    @pytest.mark.Clients
    @pytest.mark.PATCH
    def test_TC_43310_PATCH_Clients_Clients_Rule_Invalid_Matching_Rule(self, context):
        """TC-43310 - Clients-PATCH
           Verify that correct message is displayed in response on modifying client by providing invalid value in parameter 'matchingRule' using request PATCH '/clients/'."""

        # Define a test step
        with pytest.allure.step("""Test1: Verify that correct message is displayed in response on modifying client by providing invalid value "1234" in parameter 'matchingRule' using request PATCH '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
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
                name='PATCH: Client with Updated Invalid Matching Rule 1',
                sourceSelectionRule=[])


            # prepare the request, so we can modify it
            request = context.cl.Clients.updateEntity(
                    body=clientDetails, 
                    id='clientUpdate'
                
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateEntity the Clients, and check we got the error we expect
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
        with pytest.allure.step("""Test2: Verify that correct message is displayed in response on modifying client by providing invalid value "avbcd" in parameter 'matchingRule' using request PATCH '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
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
                name='PATCH: Client with Updated  Invalid Matching Rule 2',
                sourceSelectionRule=[])

            # prepare the request, so we can modify it
            request = context.cl.Clients.updateEntity(
                body=clientDetails,
                id='clientUpdate'

            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateEntity the Clients, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:  # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with(
                        'Invalid request. Can not construct instance of com.mpi.mp.expression.CompoundEvaluationCondition from String value'),
                    should.contain('value not one of declared Enum instance names: [ANY, ALL, NONE]')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))




        # Define a test step
        with pytest.allure.step("""Test3: Verify that correct message is displayed in response on modifying client by providing no value in parameter 'matchingRule' using request PATCH '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
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
                name='PATCH: Client with Updated Invalid Matching Rule 3',
                sourceSelectionRule=[])

            # prepare the request, so we can modify it
            request = context.cl.Clients.updateEntity(
                body=clientDetails,
                id='clientUpdate'

            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateEntity the Clients, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:  # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with(
                        'Invalid request. Can not construct instance of com.mpi.mp.expression.CompoundEvaluationCondition from String value'),
                    should.contain('value not one of declared Enum instance names: [ANY, ALL, NONE]')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
