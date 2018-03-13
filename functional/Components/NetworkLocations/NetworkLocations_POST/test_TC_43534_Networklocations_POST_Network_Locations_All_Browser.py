# -*- coding: UTF-8 -*-

"""PFE Component Tests - Network_Locations.

* TC-43534 - Network_Locations POST:

  Verify that user is able to create network location with rule and group having parameter 'Browser>Matches' using request POST '/networkLocations'.


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
   'id': 'browserIE',
   'matchingRule': {'groups': [{'groups': [],
                                'operator': 'ALL',
                                'rules': [{'contextField': 'browser',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 'IE',
                                           'operator': 'BROWSERMATCH'}]}],
                    'operator': 'ALL',
                    'rules': [{'contextField': 'browser',
                               'contextFieldKey': '',
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 'IE',
                               'operator': 'BROWSERMATCH'}]},
   'name': 'Network IE Browser'}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Network_Locations')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Network_Locations test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43534')
    @pytest.mark.Network_Locations
    @pytest.mark.POST
    def test_TC_43534_POST_Network_Locations_Network_Locations_Ie_Browser(self, context):
        """TC-43534 - Network_Locations-POST
           Verify that user is able to create network location with rule and group having parameter 'Browser>Matches' using request POST '/networkLocations'."""
        # Define a test step
        with pytest.allure.step("""IE: Verify that user is able to create network location with rule and group having parameter 'Browser>Matches' using request POST '/networkLocations'."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=0,
                bitrateCapVOD=0,
                id='browserIE',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE',
                        'contextFieldKey': ''
                    }],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'IE',
                            'contextFieldKey': ''
                        }],
                        'groups': []
                    }]
                },
                name='Network IE Browser')


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
        with pytest.allure.step("""IE6: Verify that user is able to create network location with rule and group having parameter 'Browser>Matches' using request POST '/networkLocations'."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=0,
                bitrateCapVOD=0,
                id='browserIE6',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE6',
                        'contextFieldKey': ''
                    }],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'IE6',
                            'contextFieldKey': ''
                        }],
                        'groups': []
                    }]
                },
                name='Network IE6 Browser')


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
        with pytest.allure.step("""IE7: Verify that user is able to create network location with rule and group having parameter 'Browser>Matches' using request POST '/networkLocations'."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=0,
                bitrateCapVOD=0,
                id='browserIE7',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE7',
                        'contextFieldKey': ''
                    }],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'IE7',
                            'contextFieldKey': ''
                        }],
                        'groups': []
                    }]
                },
                name='Network IE7 Browser')


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
        with pytest.allure.step("""IE8: Verify that user is able to create network location with rule and group having parameter 'Browser>Matches' using request POST '/networkLocations'."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=0,
                bitrateCapVOD=0,
                id='browserIE8',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE8',
                        'contextFieldKey': ''
                    }],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'IE8',
                            'contextFieldKey': ''
                        }],
                        'groups': []
                    }]
                },
                name='Network IE8 Browser')


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
        with pytest.allure.step("""IE9: Verify that user is able to create network location with rule and group having parameter 'Browser>Matches' using request POST '/networkLocations'."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=0,
                bitrateCapVOD=0,
                id='browserIE9',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE9',
                        'contextFieldKey': ''
                    }],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'IE9',
                            'contextFieldKey': ''
                        }],
                        'groups': []
                    }]
                },
                name='Network IE9 Browser')


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
        with pytest.allure.step("""IE10: Verify that user is able to create network location with rule and group having parameter 'Browser>Matches' using request POST '/networkLocations'."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=0,
                bitrateCapVOD=0,
                id='browserIE10',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE10',
                        'contextFieldKey': ''
                    }],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'IE10',
                            'contextFieldKey': ''
                        }],
                        'groups': []
                    }]
                },
                name='Network IE10 Browser')


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
        with pytest.allure.step("""IE11: Verify that user is able to create network location with rule and group having parameter 'Browser>Matches' using request POST '/networkLocations'."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=0,
                bitrateCapVOD=0,
                id='browserIE11',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'IE11',
                        'contextFieldKey': ''
                    }],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'IE11',
                            'contextFieldKey': ''
                        }],
                        'groups': []
                    }]
                },
                name='Network IE11 Browser')


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
        with pytest.allure.step("""FIREFOX: Verify that user is able to create network location with rule and group having parameter 'Browser>Matches' using request POST '/networkLocations'."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=0,
                bitrateCapVOD=0,
                id='browserFirefox',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'FIREFOX',
                        'contextFieldKey': ''
                    }],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'FIREFOX',
                            'contextFieldKey': ''
                        }],
                        'groups': []
                    }]
                },
                name='Network Firefox Browser')


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
        with pytest.allure.step("""CHROME: Verify that user is able to create network location with rule and group having parameter 'Browser>Matches' using request POST '/networkLocations'."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=0,
                bitrateCapVOD=0,
                id='browserCHROME',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'CHROME',
                        'contextFieldKey': ''
                    }],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'CHROME',
                            'contextFieldKey': ''
                        }],
                        'groups': []
                    }]
                },
                name='Network CHROME Browser')


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
        with pytest.allure.step("""SAFARI: Verify that user is able to create network location with rule and group having parameter 'Browser>Matches' using request POST '/networkLocations'."""):

            # Test case configuration
            networkLocationDetails = context.sc.NetworkLocationDetails(
                bitrateCapLive=0,
                bitrateCapVOD=0,
                id='browserSAFARI',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'browser',
                        'operator': 'BROWSERMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'SAFARI',
                        'contextFieldKey': ''
                    }],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'browser',
                            'operator': 'BROWSERMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'SAFARI',
                            'contextFieldKey': ''
                        }],
                        'groups': []
                    }]
                },
                name='Network SAFARI Browser')


            # createEntity the Network_Locations.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Network_Locations.createEntity(
                    body=networkLocationDetails
                )
            )