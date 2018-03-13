# -*- coding: UTF-8 -*-

"""PFE Component Tests - Network_Locations.

* TC-43501 - Network_Locations GET:

  Verify that user is able to get 'Groups' details associated with network location using request GET /networkLocation{id}.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations/getNetworkLocationGroups"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations/getNetworkLocationGroups"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Network_Locations')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Network_Locations test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43501')
    @pytest.mark.Network_Locations
    @pytest.mark.GET
    def test_TC_43501_GET_Network_Locations_All_Groups(self, context):
        """TC-43501 - Network_Locations-GET
           Verify that user is able to get 'Groups' details associated with network location using request GET /networkLocation{id}."""

        # Define a test step
        with pytest.allure.step("""First create a Network Location with Matching Rules having Group, using POST /networkLocation."""):
            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=0,
                bitrateCapVOD=0,
                id='NetworkLocation2',
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [],
                    'groups': [{
                        'operator':
                            'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'remoteAddress',
                            'operator': 'IPMATCH',
                            'contextFieldType': 'String',
                            'matchValue': '10.0.0.0/32',
                            'contextFieldKey': None
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'remoteHost',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 'autoQEd',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverHost',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': '101.101.101.101',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'serverPort',
                            'operator': 'EQ',
                            'contextFieldType': 'String',
                            'matchValue': 80,
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'operatingSystem',
                            'operator': 'OSMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'BLACKBERRY',
                            'contextFieldKey': ''
                        }, {
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'CHROME',
                            'contextFieldKey': ''
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
                            'matchValue': 'tags',
                            'contextFieldKey': 'tags'
                        }],
                        'groups': []
                    }]
                },
                name='NetworkLocation2')

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
        with pytest.allure.step("""Verify that user is able to get 'Groups' details associated with network location using request GET /networkLocation{id}."""):

            # listEntities the Network_Locations.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Network_Locations.getEntity(
                    id='NetworkLocation2'
                )
            )

