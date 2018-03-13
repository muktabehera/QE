# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43306 - Clients PATCH:

  Verify that validation message is displayed in response class on modifying client with non-existing 'Id' parameter using request PATCH /clients.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/NonExistID"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/NonExistID"

JSON data sent to PathFinder in this test:

  {'matchingRule': {'groups': [{'groups': [],
                                'operator': 'ALL',
                                'rules': [{'contextField': 'remoteAddress',
                                           'contextFieldKey': None,
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': '101.121.101.101/32',
                                           'operator': 'IPMATCH'}]}],
                    'operator': 'ALL',
                    'rules': [{'contextField': 'remoteAddress',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': '10.12.1.1/32',
                               'operator': 'IPMATCH'}]},
   'name': 'POST: Client Updated with name_Rule_Group_SourceRule',
   'sourceSelectionRule': [{'groups': [],
                            'operator': 'ALL',
                            'rules': [{'contextField': 'bitrateKbps',
                                       'contextFieldKey': None,
                                       'contextFieldType': 'String',
                                       'expressionType': 'Single',
                                       'matchValue': 200,
                                       'operator': 'EQ'}]}]}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43306')
    @pytest.mark.Clients
    @pytest.mark.PATCH
    def test_TC_43306_PATCH_Clients_Non_Exist_Id(self, context):
        """TC-43306 - Clients-PATCH
           Verify that validation message is displayed in response class on modifying client with non-existing 'Id' parameter using request PATCH /clients."""
        # Define a test step


        with pytest.allure.step("""Verify that validation message is displayed in response class on modifying client with non-existing 'Id' parameter using request PATCH /clients."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'IPMATCH',
                        'contextFieldType': 'String',
                        'matchValue': '10.12.1.1/32',
                        'contextFieldKey': None
                    }],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'remoteAddress',
                            'operator': 'IPMATCH',
                            'contextFieldType': 'String',
                            'matchValue': '101.121.101.101/32',
                            'contextFieldKey': None
                        }],
                        'groups': []
                    }]
                },
                name='POST: Client Updated with name_Rule_Group_SourceRule',
                sourceSelectionRule=[{
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'bitrateKbps',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 200,
                        'contextFieldKey': None
                    }],
                    'groups': []
                }])


            # prepare the request, so we can modify it
            request = context.cl.Clients.updateEntity(
                    body=clientDetails,
                    id='non existing'
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
            except (HTTPBadRequest, HTTPForbidden, HTTPNotFound) as e:        # 400, 403, 404 error
                get_error_message(e) | expect.any(
                    should.start_with('Delivery Service entity not found')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
