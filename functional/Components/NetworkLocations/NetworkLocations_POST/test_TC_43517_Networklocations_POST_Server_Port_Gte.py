# -*- coding: UTF-8 -*-

"""PFE Component Tests - Network_Locations.

* TC-43517 - Network_Locations POST:

  Verify that user is able to create network location with rule and group having parameter 'Server Port>GTE(Greater Than Equal)' using request POST '/networkLocations'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations"

JSON data sent to PathFinder in this test:

  {'bitrateCapLive': 0,
   'bitrateCapVOD': 0,
   'description': None,
   'id': 'serverPortGTE',
   'matchingRule': {'groups': [{'groups': [],
                                'operator': 'ALL',
                                'rules': [{'contextField': 'serverPort',
                                           'contextFieldKey': None,
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 8080,
                                           'operator': 'GTE'}]}],
                    'operator': 'ALL',
                    'rules': [{'contextField': 'serverPort',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 80,
                               'operator': 'GTE'}]},
   'name': 'Network Server Port GTE'}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Network_Locations')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Network_Locations test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43517')
    @pytest.mark.Network_Locations
    @pytest.mark.POST
    def test_TC_43517_POST_Network_Locations_Server_Port_Gte(self, context):
        """TC-43517 - Network_Locations-POST
           Verify that user is able to create network location with rule and group having parameter 'Server Port>GTE(Greater Than Equal)' using request POST '/networkLocations'."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create network location with rule and group having parameter 'Server Port>GTE(Greater Than Equal)' using request POST '/networkLocations'."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=0,
                bitrateCapVOD=0,
                id='serverPortGTE',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'serverPort',
                        'operator': 'GTE',
                        'contextFieldType': 'String',
                        'matchValue': 80,
                        'contextFieldKey': None
                    }],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'serverPort',
                            'operator': 'GTE',
                            'contextFieldType': 'String',
                            'matchValue': 8080,
                            'contextFieldKey': None
                        }],
                        'groups': []
                    }]
                },
                name='Network Server Port GTE')


            # createEntity the Network_Locations.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Network_Locations.createEntity(
                    body=networkLocationDetails
                )
            )

