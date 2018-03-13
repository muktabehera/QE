# -*- coding: UTF-8 -*-

"""PFE Component Tests - Network_Locations.

* TC-43509 - Network_Locations POST:

  Verify that user is able to create network location with parameters ('VOD Maximum Bitrate', 'Live Maximum Bitrate') using request POST /networkLocations.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/networkLocations"

JSON data sent to PathFinder in this test:

  {'bitrateCapLive': 152,
   'bitrateCapVOD': 512,
   'description': None,
   'id': 'matchingRuleBitrate',
   'matchingRule': {'groups': [{'groups': [],
                                'operator': 'ANY',
                                'rules': [{'contextField': 'remoteAddress',
                                           'contextFieldKey': None,
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': '101.101.105.105/24',
                                           'operator': 'IPMATCH'}]}],
                    'operator': 'ALL',
                    'rules': [{'contextField': 'remoteAddress',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': '10.1.10.10/32',
                               'operator': 'IPMATCH'}]},
   'name': 'Network Matching Rule Max Bitrate'}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Network_Locations')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Network_Locations test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43509')
    @pytest.mark.Network_Locations
    @pytest.mark.POST
    def test_TC_43509_POST_Network_Locations_Max_Bitrate_Vod_Live(self, context):
        """TC-43509 - Network_Locations-POST
           Verify that user is able to create network location with parameters ('VOD Maximum Bitrate', 'Live Maximum Bitrate') using request POST /networkLocations."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create network location with parameters ('VOD Maximum Bitrate', 'Live Maximum Bitrate') using request POST /networkLocations."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=152,
                bitrateCapVOD=512,
                id='matchingRuleBitrate',
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
                        'ANY',
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
                name='Network Matching Rule Max Bitrate')


            # createEntity the Network_Locations.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Network_Locations.createEntity(
                    body=networkLocationDetails
                )
            )

