# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43092 - Clients POST:

  Verify that user is able to add child group with parameter 'Browser>Matches' using request POST '/clients/'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

JSON data sent to PathFinder in this test:

  {'bitrateCapLive': 0,
   'bitrateCapVOD': 0,
   'description': None,
   'id': 'clientGroupbrowserIE',
   'matchingRule': {'groups': [{'groups': [],
                                'operator': 'ALL',
                                'rules': [{'contextField': 'browser',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 'IE',
                                           'operator': 'BROWSERMATCH'}]}],
                    'operator': 'ALL',
                    'rules': []},
   'name': 'POST: Client Group IE Browser',
   'sourceSelectionRule': []}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43092')
    @pytest.mark.Clients
    @pytest.mark.POST
    def test_TC_43092_POST_Clients_Client_Group_Ie_Browser(self, context):
        """TC-43092 - Clients-POST
           Verify that user is able to add child group with parameter 'Browser>Matches' using request POST '/clients/'."""
        # Define a test step
        with pytest.allure.step("""IE: Verify that user is able to add child group with parameter 'Browser>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientGroupbrowserIE',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [],
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
                name='POST: Client Group IE Browser',
                sourceSelectionRule=[])


            # createEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Clients.createEntity(
                    body=clientDetails
                )
            )

        # Define a test step
        with pytest.allure.step("""IE6: Verify that user is able to add child group with parameter 'Browser>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientGroupbrowserIE6',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [],
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
                name='POST: Client Group IE6 Browser',
                sourceSelectionRule=[])


            # createEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Clients.createEntity(
                    body=clientDetails
                )
            )


        # Define a test step
        with pytest.allure.step("""IE7: Verify that user is able to add child group with parameter 'Browser>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientGroupbrowserIE7',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [],
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
                name='POST: Client Group IE7 Browser',
                sourceSelectionRule=[])


            # createEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Clients.createEntity(
                    body=clientDetails
                )
            )

        # Define a test step
        with pytest.allure.step("""IE8: Verify that user is able to add child group with parameter 'Browser>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientgroupbrowserIE8',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [],
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
                name='POST: Client group IE8 Browser',
                sourceSelectionRule=[])


            # createEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Clients.createEntity(
                    body=clientDetails
                )
            )

        # Define a test step
        with pytest.allure.step("""IE9: Verify that user is able to add child group with parameter 'Browser>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientGroupbrowserIE9',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [],
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
                name='POST: Client Group IE9 Browser',
                sourceSelectionRule=[])


            # createEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Clients.createEntity(
                    body=clientDetails
                )
            )

        # Define a test step
        with pytest.allure.step("""IE10: Verify that user is able to add child group with parameter 'Browser>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientGroupbrowserIE10',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [],
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
                name='POST: Client Group IE10 Browser',
                sourceSelectionRule=[])


            # createEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Clients.createEntity(
                    body=clientDetails
                )
            )


        # Define a test step
        with pytest.allure.step("""IE11: Verify that user is able to add child group with parameter 'Browser>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientGroupbrowserIE11',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [],
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
                name='POST: Client Group IE11 Browser',
                sourceSelectionRule=[])


            # createEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Clients.createEntity(
                    body=clientDetails
                )
            )
        # Define a test step
        with pytest.allure.step("""IE11 Client rule: Verify that user is able to add child group with parameter 'Browser>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientGroupbrowsermatchIE11',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [],
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
                name='POST: Client Group IE11 Browsermatch',
                sourceSelectionRule=[])


            # createEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Clients.createEntity(
                    body=clientDetails
                )
            )

        # Define a test step
        with pytest.allure.step("""FIREFOX: Verify that user is able to add child group with parameter 'Browser>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientGroupbrowsermatchFirefox',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [],
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
                name='POST: Client Group Firefox Browsermatch',
                sourceSelectionRule=[])


            # createEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Clients.createEntity(
                    body=clientDetails
                )
            )

        # Define a test step
        with pytest.allure.step("""CHROME: Verify that user is able to add child group with parameter 'Browser>Matches' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientGroupbrowsermatchCHROME',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [],
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
                name='POST: Client Group CHROME Browsermatch',
                sourceSelectionRule=[])


            # createEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Clients.createEntity(
                    body=clientDetails
                )
            )

        # Define a test step
        with pytest.allure.step("""SAFARI: Verify that user is able to add child group with parameter 'Browser>Matches' using request POST '/clients/'."""):


            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientGroupbrowsermatchSAFARI',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [],
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
                name='POST: Client Group SAFARI Browsermatch',
                sourceSelectionRule=[])


            # createEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Clients.createEntity(
                    body=clientDetails
                )
            )
