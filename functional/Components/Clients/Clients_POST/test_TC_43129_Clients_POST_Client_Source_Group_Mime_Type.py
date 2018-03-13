# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43129 - Clients POST:

  Verify that user is able to add source constraint rule with specific group for parameter 'MimeType>Matches MIME Type' using request POST '/clients/'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients"

JSON data sent to PathFinder in this test:

  {'id': 'sourceGroupmimeType',
   'matchingRule': {'groups': [], 'operator': 'ALL', 'rules': []},
   'name': 'POST: Client with Source Group Mime Type MP4',
   'sourceSelectionRule': [{'groups': [{'groups': [],
                                        'operator': 'ALL',
                                        'rules': [{'contextField': 'mimetype',
                                                   'contextFieldKey': None,
                                                   'contextFieldType': 'String',
                                                   'expressionType': 'Single',
                                                   'matchValue': 'video/mp4',
                                                   'operator': 'MIMEMATCH'}]}],
                            'operator': 'ALL',
                            'rules': []}]}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43129')
    @pytest.mark.Clients
    @pytest.mark.POST
    def test_TC_43129_POST_Clients_Client_Source_Group_Mime_Type(self, context):
        """TC-43129 - Clients-POST
           Verify that user is able to add source constraint rule with specific group for parameter 'MimeType>Matches MIME Type' using request POST '/clients/'."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is able to add source constraint rule with specific group for parameter 'MimeType>Matches MIME Type' using request POST '/clients/'."""):


            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='sourceGroupmimeType',
                matchingRule={'operator': 'ALL',
                              'rules': [],
                              'groups': []},
                name='POST: Client with Source Group Mime Type MP4',
                sourceSelectionRule=[{
                    'operator':
                    'ALL',
                    'rules': [],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'mimetype',
                            'operator': 'MIMEMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'video/mp4',
                            'contextFieldKey': None
                        }],
                        'groups': []
                    }]
                }])


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
        with pytest.allure.step("""Test2: Verify that user is able to add source constraint rule with specific group for parameter 'MimeType>Matches MIME Type' using request POST '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='sourceGroupmimeType2',
                matchingRule={'operator': 'ALL',
                              'rules': [],
                              'groups': []},
                name='POST: Client with Source Group Mime Type vnd',
                sourceSelectionRule=[{
                    'operator':
                    'ALL',
                    'rules': [],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'mimetype',
                            'operator': 'MIMEMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'application/vnd.apple.mpegurl',
                            'contextFieldKey': None
                        }],
                        'groups': []
                    }]
                }])


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
        with pytest.allure.step("""Test3: Verify that user is able to add source constraint rule with specific group for parameter 'MimeType>Matches MIME Type' using request POST '/clients/'."""):


            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='sourceGroupmimeType3',
                matchingRule={'operator': 'ALL',
                              'rules': [],
                              'groups': []},
                name='POST: Client with Source Group Mime Type application',
                sourceSelectionRule=[{
                    'operator':
                    'ALL',
                    'rules': [],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'mimetype',
                            'operator': 'MIMEMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'application/x-mpegURL',
                            'contextFieldKey': None
                        }],
                        'groups': []
                    }]
                }])


            # createEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Clients.createEntity(
                    body=clientDetails
                )
            )
