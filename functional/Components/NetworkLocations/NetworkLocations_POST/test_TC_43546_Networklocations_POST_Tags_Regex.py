# -*- coding: UTF-8 -*-

"""PFE Component Tests - Network_Locations.

* TC-43546 - Network_Locations POST:

  Verify that user is able to create network location with rule and group having parameter 'Tags>Matches Regex' using request POST '/networkLocations/'.


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
   'id': 'tagsRegex',
   'matchingRule': {'groups': [{'groups': [],
                                'operator': 'ALL',
                                'rules': [{'contextField': 'tags',
                                           'contextFieldKey': 'autovcc',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 'autovcc',
                                           'operator': 'REGEX'}]}],
                    'operator': 'ALL',
                    'rules': [{'contextField': 'tags',
                               'contextFieldKey': '101441',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': '101441',
                               'operator': 'REGEX'}]},
   'name': 'Network Tags REGEX'}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Network_Locations')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Network_Locations test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43546')
    @pytest.mark.Network_Locations
    @pytest.mark.POST
    def test_TC_43546_POST_Network_Locations_Tags_Regex(self, context):
        """TC-43546 - Network_Locations-POST
           Verify that user is able to create network location with rule and group having parameter 'Tags>Matches Regex' using request POST '/networkLocations/'."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create network location with rule and group having parameter 'Tags>Matches Regex' using request POST '/networkLocations/'."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=0,
                bitrateCapVOD=0,
                id='tagsRegex',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'tags',
                        'operator': 'REGEX',
                        'contextFieldType': 'String',
                        'matchValue': '101441',
                        'contextFieldKey': '101441'
                    }],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'tags',
                            'operator': 'REGEX',
                            'contextFieldType': 'String',
                            'matchValue': 'autovcc',
                            'contextFieldKey': 'autovcc'
                        }],
                        'groups': []
                    }]
                },
                name='Network Tags REGEX')


            # createEntity the Network_Locations.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Network_Locations.createEntity(
                    body=networkLocationDetails
                )
            )

