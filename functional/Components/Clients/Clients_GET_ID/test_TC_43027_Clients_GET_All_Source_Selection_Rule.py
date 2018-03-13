# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43027 - Clients GET:

  Verify that user is able to get 'sourceSelectionRule' details associated with client using request GET /client{id}.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/clientsAllRules"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43027')
    @pytest.mark.Clients
    @pytest.mark.GET
    def test_TC_43027_GET_Clients_All_Source_Selection_Rule(self, context):
        """TC-43027 - Clients-GET
           Verify that user is able to get 'sourceSelectionRule' details associated with client using request GET /client{id}."""
        with pytest.allure.step("""Create a Client with All Rules using POST"""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientsAllRules',
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
                name='To get Client with All Rules',
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

        # Define a test step
        with pytest.allure.step("""Verify that user is able to get 'sourceSelectionRule' details associated with client using request GET /client{id}."""):

            # getEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Clients.getEntity(
                    id='clientsAllRules')
            )

