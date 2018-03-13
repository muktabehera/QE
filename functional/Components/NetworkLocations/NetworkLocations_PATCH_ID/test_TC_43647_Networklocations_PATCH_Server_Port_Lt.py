# -*- coding: UTF-8 -*-

"""PFE Component Tests - Network_Locations.

* TC-43647 - Network_Locations PATCH:

  Verify that user is able to modify network location with rule and group having parameter 'Server Port>LT(Less Than)' using request PATCH '/networkLocations'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations/networkUpdate"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations/networkUpdate"

JSON data sent to PathFinder in this test:

  {
    "id": "networkUpdate",
    "name": "Network Locations Updated",
    "bitrateCapVOD": 650,
    "bitrateCapLive": 1024,
    "matchingRule": {
      "operator": "ALL",
      "rules": [
        {
          "expressionType": "Single",
          "contextField": "serverPort",
          "operator": "LT",
          "contextFieldType": "String",
          "matchValue": 8080,
          "contextFieldKey": ""
        }
      ],
      "groups": [
 
        {
          "expressionType": "Single",
          "contextField": "serverPort",
          "operator": "LT",
          "contextFieldType": "String",
          "matchValue": 8080,
          "contextFieldKey": ""
        }
          ],
          "groups": []
        }
      ]
    }
  }


"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Network_Locations')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Network_Locations test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43647')
    @pytest.mark.Network_Locations
    @pytest.mark.PATCH
    def test_TC_43647_PATCH_Network_Locations_Server_Port_Lt(self, context):
        """TC-43647 - Network_Locations-PATCH
           Verify that user is able to modify network location with rule and group having parameter 'Server Port>LT(Less Than)' using request PATCH '/networkLocations'."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to modify network location with rule and group having parameter 'Server Port>LT(Less Than)' using request PATCH '/networkLocations'."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=1024,
                bitrateCapVOD=650,
                id=None,
                matchingRule={
                    'operator':
                        'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'LT',
                        'contextFieldType': 'String',
                        'matchValue': 8080,
                        'contextFieldKey': ''
                    }],
                    'groups': [{
                        'operator':
                            'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'serverPort',
                            'operator': 'LT',
                            'contextFieldType': 'String',
                            'matchValue': 8080,
                            'contextFieldKey': ''
                        }],
                        'groups': []
                    }]
                },
                name='Network Locations Updated3')
            

            # updateEntity the Network_Locations.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Network_Locations.updateEntity(
                    id='networkpatchUpdate',
                    body=networkLocationDetails
                )
            )

