# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43224 - Clients POST:

  Verify that user is able to create client on providing max length of 100 character in parameter 'Name' using request POST '/clients/'.


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
   'id': 'clientNameMaxLength',
   'matchingRule': {'groups': [{'groups': [],
                                'operator': 'ALL',
                                'rules': [{'contextField': 'operatingSystem',
                                           'contextFieldKey': '',
                                           'contextFieldType': 'String',
                                           'expressionType': 'Single',
                                           'matchValue': 'WINDOWS_MOBILE_8',
                                           'operator': 'OSMATCH'}]}],
                    'operator': 'ALL',
                    'rules': []},
   'name': 'clientAPI1234!@# clientAPI1234!@# clientAPI1234!@# clientAPI1234!@# '
           'clientAPI1234!@#clientAPI1234!@#',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43224')
    @pytest.mark.Clients
    @pytest.mark.POST
    def test_TC_43224_POST_Clients_Max_Length_Name(self, context):
        """TC-43224 - Clients-POST
           Verify that user is able to create client on providing max length of 100 character in parameter 'Name' using request POST '/clients/'."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create client on providing max length of 100 character in parameter 'Name' using request POST '/clients/'."""):


            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id='clientNameMaxLength',
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [],
                    'groups': [{
                        'operator':
                        'ALL',
                        'rules': [{
                            'expressionType': 'Single',
                            'contextField': 'operatingSystem',
                            'operator': 'OSMATCH',
                            'contextFieldType': 'String',
                            'matchValue': 'WINDOWS_MOBILE_8',
                            'contextFieldKey': ''
                        }],
                        'groups': []
                    }]
                },
                name=
                'clientAPI1234!@# clientAPI1234!@# clientAPI1234!@# clientAPI1234!@# clientAPI1234!@#clientAPI1234!@#',
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

