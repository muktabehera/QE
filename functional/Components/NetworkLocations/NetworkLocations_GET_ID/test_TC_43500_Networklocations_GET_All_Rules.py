# -*- coding: UTF-8 -*-

"""PFE Component Tests - Network_Locations.

* TC-43500 - Network_Locations GET:

  Verify that user is able to get 'rules' details associated with network location using request GET /networkLocation{id}.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations/getNetworkLocationRules"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations/getNetworkLocationRules"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Network_Locations')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Network_Locations test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43500')
    @pytest.mark.Network_Locations
    @pytest.mark.GET
    def test_TC_43500_GET_Network_Locations_All_Rules(self, context):
        """TC-43500 - Network_Locations-GET
           Verify that user is able to get 'rules' details associated with network location using request GET /networkLocation{id}."""

        # Define a test step
        with pytest.allure.step("""First create network location with Rules using request POST /networkLocation{id}."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=0,
                bitrateCapVOD=0,
                id='getNetworkLocationRulesTest',
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'IPMATCH',
                        'contextFieldType': 'String',
                        'matchValue': '10.19.20.0/32',
                        'contextFieldKey': None
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'remoteHost',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'autovcc.qumu.com',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverHost',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': '10.10.10.25',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 8080,
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'operatingSystem',
                        'operator': 'OSMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'ANDROID',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE6',
                        'contextFieldKey': ''
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'headerMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': '45',
                        'contextFieldKey': '45'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'queryParamMap',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'qmu',
                        'contextFieldKey': 'qumu'
                    }, {
                        'expressionType': 'Map',
                        'contextField': 'tags',
                        'operator': 'EQ',
                        'contextFieldType': 'String',
                        'matchValue': 'tag',
                        'contextFieldKey': 'tag'
                    }],
                    'groups': []
                },
                name='GET Network Location with All Rules')

            # createEntity the Network_Locations.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Network_Locations.createEntity(
                    body=networkLocationDetails
                )
            )


        # Define a test step
        with pytest.allure.step("""Now verify that user is able to get 'rules' details associated with network location using request GET /networkLocation{id}."""):

            # listEntities the Network_Locations.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Network_Locations.getEntity(
                    id='getNetworkLocationRulesTest'
                )
            )
