# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-42284 - Clients POST:

  Verify that Create button is not displayed on 'Proximities zones' page under Intelligent Content Routing menu for user with "Manage Configuration" permission, while "Config admin can create" flag is set to false within the token expiration time.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X POST -d @<JSON_data_file> -H "Content-Type:
       application/json" "<PF_host>://<client_host>/clients"

Same, with test data:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X POST -d @<JSON_data_file> -H "Content-Type:
       application/json" "<PF_host>://<client_host>/clients"

JSON data sent to PathFinder in this test:

  {'id': 'adminFlagSetToFalse',
   'matchingRule': {'groups': [{'groups': [],
                                'operator': 'ALL',
                                'rules': [{'contextField': 'remoteAddress',
                                           'contextFieldKey': None,
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': '172.0.0.0/8',
                                           'operator': 'IPMATCH'},
                                          {'contextField': 'remoteHost',
                                           'contextFieldKey': None,
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 'qed.com',
                                           'operator': 'EQ'},
                                          {'contextField': 'serverHost',
                                           'contextFieldKey': None,
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': '172.30.3.174',
                                           'operator': 'EQ'},
                                          {'contextField': 'serverPort',
                                           'contextFieldKey': None,
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 8080,
                                           'operator': 'EQ'},
                                          {'contextField': 'operatingSystem',
                                           'contextFieldKey': None,
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 'WINDOWS_8',
                                           'operator': 'OSMATCH'},
                                          {'contextField': 'browser',
                                           'contextFieldKey': None,
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 'IE',
                                           'operator': 'BROWSERMATCH'},
                                          {'contextField': 'headerMap',
                                           'contextFieldKey': 'headergroup',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Map',
                                           'matchValue': 'headergroup',
                                           'operator': 'EQ'},
                                          {'contextField': 'queryParamMap',
                                           'contextFieldKey': 'query1',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Map',
                                           'matchValue': 'query1',
                                           'operator': 'EQ'},
                                          {'contextField': 'tags',
                                           'contextFieldKey': '1234',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Map',
                                           'matchValue': '1234',
                                           'operator': 'EQ'}]}],
                    'operator': 'ALL',
                    'rules': [{'contextField': 'remoteAddress',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': '172.0.0.0/8',
                               'operator': 'IPMATCH'},
                              {'contextField': 'remoteHost',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 'qed.com',
                               'operator': 'EQ'},
                              {'contextField': 'serverHost',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': '172.30.3.174',
                               'operator': 'EQ'},
                              {'contextField': 'operatingSystem',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 'BLACKBERRY',
                               'operator': 'OSMATCH'},
                              {'contextField': 'browser',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 'IE10',
                               'operator': 'BROWSERMATCH'},
                              {'contextField': 'headerMap',
                               'contextFieldKey': 'header',
                               'contextFieldType': 'String',
                               'expressionType': 'Map',
                               'matchValue': 'header',
                               'operator': 'EQ'},
                              {'contextField': 'queryParamMap',
                               'contextFieldKey': 'query',
                               'contextFieldType': 'String',
                               'expressionType': 'Map',
                               'matchValue': 'query',
                               'operator': 'EQ'},
                              {'contextField': 'tags',
                               'contextFieldKey': 'tag',
                               'contextFieldType': 'String',
                               'expressionType': 'Map',
                               'matchValue': 'tag',
                               'operator': 'EQ'},
                              {'contextField': 'serverPort',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 8080,
                               'operator': 'EQ'}]},
   'name': 'POST: Unable To create Client',
   'sourceSelectionRule': [{'groups': [{'groups': [],
                                        'operator': 'ALL',
                                        'rules': [{'contextField': 'bitrateKbps',
                                                   'contextFieldKey': None,
                                                   'contextFieldType': 'String',
                                                   'expressionType': 'Single',
                                                   'matchValue': 523,
                                                   'operator': 'EQ'},
                                                  {'contextField': 'heightPx',
                                                   'contextFieldKey': None,
                                                   'contextFieldType': 'String',
                                                   'expressionType': 'Single',
                                                   'matchValue': 456,
                                                   'operator': 'EQ'},
                                                  {'contextField': 'mimetype',
                                                   'contextFieldKey': None,
                                                   'contextFieldType': 'String',
                                                   'expressionType': 'Single',
                                                   'matchValue': 'video/mp4',
                                                   'operator': 'MIMEMATCH'},
                                                  {'contextField': 'tags',
                                                   'contextFieldKey': '456',
                                                   'contextFieldType': 'String',
                                                   'expressionType': 'Map',
                                                   'matchValue': '456',
                                                   'operator': 'EQ'},
                                                  {'contextField': 'widthPx',
                                                   'contextFieldKey': None,
                                                   'contextFieldType': 'String',
                                                   'expressionType': 'Single',
                                                   'matchValue': 200,
                                                   'operator': 'EQ'}]}],
                            'operator': 'ALL',
                            'rules': [{'contextField': 'bitrateKbps',
                                       'contextFieldKey': None,
                                       'contextFieldType': 'String',
                                       'expressionType': 'Single',
                                       'matchValue': 256,
                                       'operator': 'EQ'},
                                      {'contextField': 'heightPx',
                                       'contextFieldKey': None,
                                       'contextFieldType': 'String',
                                       'expressionType': 'Single',
                                       'matchValue': 563,
                                       'operator': 'EQ'},
                                      {'contextField': 'mimetype',
                                       'contextFieldKey': None,
                                       'contextFieldType': 'String',
                                       'expressionType': 'Single',
                                       'matchValue': 'application/x-mpegURL',
                                       'operator': 'MIMEMATCH'},
                                      {'contextField': 'tags',
                                       'contextFieldKey': '124',
                                       'contextFieldType': 'String',
                                       'expressionType': 'Map',
                                       'matchValue': '124',
                                       'operator': 'EQ'},
                                      {'contextField': 'widthPx',
                                       'contextFieldKey': None,
                                       'contextFieldType': 'String',
                                       'expressionType': 'Single',
                                       'matchValue': 250,
                                       'operator': 'EQ'}]}]}

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42284')
    @pytest.mark.Clients
    @pytest.mark.POST
    def test_TC_42284_POST_Clients_Admin_Create_Flag_Set_To_False(self, context):
        """TC-42284 - Clients-POST
           Verify that Create button is not displayed on 'Proximities zones' page under Intelligent Content Routing menu for user with "Manage Configuration" permission, while "Config admin can create" flag is set to false within the token expiration time."""
        # Define a test step
        with pytest.allure.step("""Verify that Create button is not displayed on 'Proximities zones' page under Intelligent Content Routing menu for user with "Manage Configuration" permission, while "Config admin can create" flag is set to false within the token expiration time."""):

            ### Positive test example

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='adminFlagSetToFalse',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'IPMATCH',
                        'contextFieldType': 'String',
                        'matchValue': '172.0.0.0/8',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'remoteHost',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'qed.com',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverHost',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': '172.30.3.174',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'operatingSystem',
                        'operator': 'OSMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'BLACKBERRY',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE10',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'header',
                        'contextFieldKey': 'header'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'queryParamMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'query',
                        'contextFieldKey': 'query'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'tags',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'tag',
                        'contextFieldKey': 'tag'
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 8080,
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
                            'matchValue': '172.0.0.0/8',
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'remoteHost',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'qed.com',
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverHost',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': '172.30.3.174',
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverPort',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 8080,
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'operatingSystem',
                            'operator': 'OSMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'WINDOWS_8',
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'IE',
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'headergroup',
                            'contextFieldKey': 'headergroup'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'queryParamMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'query1',
                            'contextFieldKey': 'query1'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'tags',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': '1234',
                            'contextFieldKey': '1234'
                        }],
                        'groups': []
                    }]
                },
                name='POST: Unable To create Client',
                sourceSelectionRule=[{
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'bitrateKbps',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 256,
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'heightPx',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 563,
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'mimetype',
                        'operator': 'MIMEMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'application/x-mpegURL',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'tags',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': '124',
                        'contextFieldKey': '124'
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'widthPx',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 250,
                        'contextFieldKey': None
                    }],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'bitrateKbps',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 523,
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'heightPx',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 456,
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'mimetype',
                            'operator': 'MIMEMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'video/mp4',
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'tags',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': '456',
                            'contextFieldKey': '456'
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'widthPx',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 200,
                            'contextFieldKey': None
                        }],
                        'groups': []
                    }]
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

        with pytest.allure.step("""Verify that Create button is not displayed on 'Proximities zones' page under Intelligent Content Routing menu for user with "Manage Configuration" permission, while "Config admin can create" flag is set to false within the token expiration time."""):

            ### Negative test example

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='adminFlagSetToFalse',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'IPMATCH',
                        'contextFieldType': 'String',
                        'matchValue': '172.0.0.0/8',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'remoteHost',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'qed.com',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverHost',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': '172.30.3.174',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'operatingSystem',
                        'operator': 'OSMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'BLACKBERRY',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE10',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'header',
                        'contextFieldKey': 'header'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'queryParamMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'query',
                        'contextFieldKey': 'query'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'tags',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'tag',
                        'contextFieldKey': 'tag'
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 8080,
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
                            'matchValue': '172.0.0.0/8',
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'remoteHost',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'qed.com',
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverHost',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': '172.30.3.174',
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverPort',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 8080,
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'operatingSystem',
                            'operator': 'OSMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'WINDOWS_8',
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'IE',
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'headerMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'headergroup',
                            'contextFieldKey': 'headergroup'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'queryParamMap',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'query1',
                            'contextFieldKey': 'query1'
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'tags',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': '1234',
                            'contextFieldKey': '1234'
                        }],
                        'groups': []
                    }]
                },
                name='POST: Unable To create Client',
                sourceSelectionRule=[{
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'bitrateKbps',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 256,
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'heightPx',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 563,
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'mimetype',
                        'operator': 'MIMEMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'application/x-mpegURL',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'tags',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': '124',
                        'contextFieldKey': '124'
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'widthPx',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 250,
                        'contextFieldKey': None
                    }],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'bitrateKbps',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 523,
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'heightPx',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 456,
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'mimetype',
                            'operator': 'MIMEMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'video/mp4',
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Map',
                            'contextField': 'tags',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': '456',
                            'contextFieldKey': '456'
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'widthPx',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 200,
                            'contextFieldKey': None
                        }],
                        'groups': []
                    }]
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
