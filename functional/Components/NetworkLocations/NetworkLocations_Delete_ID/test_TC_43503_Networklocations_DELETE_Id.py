# -*- coding: UTF-8 -*-

"""PFE Component Tests - Network_Locations.

* TC-43503 - Network_Locations DELETE:

  Verify that user is able to delete the network location on providing 'Id' parameter using request DELETE /networkLocation{id}.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations/deleteNetworkLocation"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations/deleteNetworkLocation"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Network_Locations')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Network_Locations test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43503')
    @pytest.mark.Network_Locations
    @pytest.mark.DELETE
    def test_TC_43503_DELETE_Network_Locations_Id(self, context):
        """TC-43503 - Network_Locations-DELETE
           Verify that user is able to delete the network location on providing 'Id' parameter using request DELETE /networkLocation{id}."""

        # Define a test step
        with pytest.allure.step("""First create network location with rule and group using request POST '/networkLocations'."""):
            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=0,
                bitrateCapVOD=0,
                id='NPtest',
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
                name='NPtest')

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
        with pytest.allure.step("""Verify that user is able to delete the network location on providing 'Id' parameter using request DELETE /networkLocation{id}."""):

            # deleteEntity the Network_Locations.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Network_Locations.deleteEntity(
                    id='NPtest'
                )
            )

