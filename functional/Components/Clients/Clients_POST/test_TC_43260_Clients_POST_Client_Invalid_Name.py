# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43260 - Clients POST:

  Verify that correct error message is displayed in response on providing invalid values in parameters 'Name' using request POST /Clients.


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
   'id': 'clientInvalidName1',
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
   'name': '12POST@ID',
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


@pytest.allure.issue('https://jira.qumu.com/browse/QED-1917')
@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43260')
    @pytest.mark.Clients
    @pytest.mark.POST
    def test_TC_43260_POST_Clients_Client_Invalid_Name(self, context):
        """TC-43260 - Clients-POST
           Verify that correct error message is displayed in response on providing invalid values in parameters 'Name' using request POST /Clients."""
        # Define a test step

        with pytest.allure.step("""Verify that correct error message is displayed in response on providing invalid values in parameters 'Name' ex- 12POST@ID using request POST /Clients."""):


            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientInvalidName1',
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
                name='12POST@ID',
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
                    should.start_with('may not be empty'),
                    should.start_with('Invalid page parameter specified'),
                    should.contain('Invalid Authorization Token')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))

        # Define a test step

        with pytest.allure.step("""Verify that correct error message is displayed in response on providing invalid values in parameters 'Name' ex- Ab12/<>|\^ using request POST /Clients."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientInvalidName2',
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
                name='Ab12<>|\^',
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
                    should.start_with('may not be empty'),
                    should.start_with('Invalid page parameter specified'),
                    should.contain('Invalid Authorization Token')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))

        # Define a test step
        with pytest.allure.step("""Verify that correct error message is displayed in response on providing invalid values in parameters 'Name' ex- !@ABCD using request POST /Clients."""):

                    # Test case configuration
                    clientDetails = context.sc.ClientDetails(
                        id='clientInvalidName3',
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
                        name='!@ABCD',
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
                    except (HTTPBadRequest, HTTPForbidden) as e:  # 400, 403 error
                        get_error_message(e) | expect.any(
                            should.start_with('may not be empty'),
                            should.start_with('Invalid page parameter specified'),
                            should.contain('Invalid Authorization Token')
                        )
                    else:
                        raise Exception(
                            "Expected error message, got {} status code instead.".format(
                                response.status_code))

        # Define a test step
        with pytest.allure.step("""Verify that correct error message is displayed in response on providing invalid values in parameters 'Name' with space(ex- ABCD) using request POST /Clients."""):

                    # Test case configuration
                    clientDetails = context.sc.ClientDetails(
                        id='clientInvalidName3',
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
                        name='  ABCD',
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
                    except (HTTPBadRequest, HTTPForbidden) as e:  # 400, 403 error
                        get_error_message(e) | expect.any(
                            should.start_with('may not be empty'),
                            should.start_with('Invalid page parameter specified'),
                            should.contain('Invalid Authorization Token')
                        )
                    else:
                        raise Exception(
                            "Expected error message, got {} status code instead.".format(
                                response.status_code))

