# -*- coding: UTF-8 -*-

"""PFE Component Tests - Network_Locations.

* TC-43483 - Network_Locations GET:

  Verify that user is able to GET the details of network location on providing 'Id' parameter using request GET /networkLocation{id}.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations/getNetworkLocationGroupsRules"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations/getNetworkLocationGroupsRules"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Network_Locations')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Network_Locations test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43483')
    @pytest.mark.Network_Locations
    @pytest.mark.GET
    def test_TC_43483_GET_Network_Locations_Id(self, context):
        """TC-43483 - Network_Locations-GET
           Verify that user is able to GET the details of network location on providing 'Id' parameter using request GET /networkLocation{id}."""

        # Define a test step
        with pytest.allure.step("""First create network location with rule and group using request POST '/networkLocations'."""):
            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=0,
                bitrateCapVOD=0,
                id='NPtest2',
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'IPMATCH',
                        'contextFieldType': 'String',
                        'matchValue': '10.1.10.10/32',
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
                            'matchValue': '101.101.105.105/24',
                            'contextFieldKey': None
                        }],
                        'groups': []
                    }]
                },
                name='NPtest2')

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
        with pytest.allure.step("""Now verify that user is able to GET the details of network location on providing 'Id' parameter using request GET /networkLocation{id}."""):

            # listEntities the Network_Locations.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Network_Locations.getEntity(
                    id='NPtest2'
                )
            )

