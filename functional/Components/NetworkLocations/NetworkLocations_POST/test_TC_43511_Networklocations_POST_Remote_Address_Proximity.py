# -*- coding: UTF-8 -*-

"""PFE Component Tests - Network_Locations.

* TC-43511 - Network_Locations POST:

  Verify that user is able to create network location with rule and group having parameter 'Remote Address>Matches Proximity Zone' using request POST '/networkLocations'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations"

JSON data sent to PathFinder in this test:

  {'bitrateCapLive': 1024,
   'bitrateCapVOD': 512,
   'description': None,
   'id': 'remoteProximity',
   'matchingRule': {'groups': [{'groups': [],
                                'operator': 'ANY',
                                'rules': [{'contextField': 'remoteAddress',
                                           'contextFieldKey': None,
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 'proximityAuto',
                                           'operator': 'PROXIMITYMATCH'}]}],
                    'operator': 'ALL',
                    'rules': [{'contextField': 'remoteAddress',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 'proximityAuto',
                               'operator': 'PROXIMITYMATCH'}]},
   'name': 'Network Remote Proximity'}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Network_Locations')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Network_Locations test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43511')
    @pytest.mark.Network_Locations
    @pytest.mark.POST
    def test_TC_43511_POST_Network_Locations_Remote_Address_Proximity(self, context):
        """TC-43511 - Network_Locations-POST
           Verify that user is able to create network location with rule and group having parameter 'Remote Address>Matches Proximity Zone' using request POST '/networkLocations'."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create network location with rule and group having parameter 'Remote Address>Matches Proximity Zone' using request POST '/networkLocations'."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=1024,
                bitrateCapVOD=512,
                id='remoteProximity',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'PROXIMITYMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'proximityAuto',
                        'contextFieldKey': None
                    }],
                    'groups': [{
                        'operator':
                        'ANY',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'remoteAddress',
                            'operator': 'PROXIMITYMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'proximityAuto',
                            'contextFieldKey': None
                        }],
                        'groups': []
                    }]
                },
                name='Network Remote Proximity')


            # createEntity the Network_Locations.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Network_Locations.createEntity(
                    body=networkLocationDetails
                )
            )

