# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43330 - Clients PATCH:

  Verify that correct message is displayed in response on modifying client child group by providing invalid value in parameter 'matchingRule' using request PATCH '/clients/'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/clientUpdate"

JSON data sent to PathFinder in this test:

  {'bitrateCapLive': 0,
   'bitrateCapVOD': 0,
   'description': None,
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
   'name': 'PATCH: Client updated with Group Rule Invalid',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43330')
    @pytest.mark.Clients
    @pytest.mark.PATCH
    def test_TC_43330_PATCH_Clients_Client_Group_Invalid_Matching_Rule(self, context):
        """TC-43330 - Clients-PATCH
           Verify that correct message is displayed in response on modifying client child group by providing invalid value in parameter 'matchingRule' using request PATCH '/clients/'."""
        # Define a test step


        with pytest.allure.step("""Test1: Verify that correct message is displayed in response on modifying client child group by providing invalid value in parameter 'matchingRule' using request PATCH '/clients/'."""):


            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
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
                name='PATCH: Client updated with Group Rule Invalid',
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
        with pytest.allure.step("""Test2: Verify that correct message is displayed in response on modifying client child group by providing invalid value in parameter 'matchingRule' using request PATCH '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
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
                name='PATCH: Client updated with Group Rule Invalid2',
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
        with pytest.allure.step("""Test3: Verify that correct message is displayed in response on modifying client child group by providing invalid value in parameter 'matchingRule' using request PATCH '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
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
                name='PATCH: Client updated with Group Rule Invalid3',
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
