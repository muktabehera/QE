# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-43311 - Clients PATCH:

  Verify that user is able to modify client rule with parameter 'Remote Address>Matches Proximity Zone' using request PATCH '/clients/'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients/clientUpdate"

JSON data sent to PathFinder in this test:

  {'matchingRule': {'groups': [],
                    'operator': 'ALL',
                    'rules': [{'contextField': 'remoteAddress',
                               'contextFieldKey': None,
                               'contextFieldType': 'String',
                               'expressionType': 'Single',
                               'matchValue': 'ProximityAutoUpdate',
                               'operator': 'PROXIMITYMATCH'}]},
   'name': 'PATCH: Client Updated with RemoteAddress Proximity Rule',
   'sourceSelectionRule': []}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43311')
    @pytest.mark.Clients
    @pytest.mark.PATCH
    def test_TC_43311_PATCH_Clients_Remote_Address_Proximity(self, context):
        """TC-43311 - Clients-PATCH
           Verify that user is able to modify client rule with parameter 'Remote Address>Matches Proximity Zone' using request PATCH '/clients/'."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to modify client rule with parameter 'Remote Address>Matches Proximity Zone' using request PATCH '/clients/'."""):

            # Test case configuration
            clientDetails = context.sc.ClientDetails(
                id=None,
                matchingRule={
                    'operator':
                    'ALL',
                    'rules': [{
                        'expressionType': 'Single',
                        'contextField': 'remoteAddress',
                        'operator': 'PROXIMITYMATCH',
                        'contextFieldType': 'String',
                        'matchValue': 'ProximityAutoUpdate',
                        'contextFieldKey': None
                    }],
                    'groups': []
                },
                name='PATCH: Client Updated with RemoteAddress Proximity Rule',
                sourceSelectionRule=[])


            # updateEntity the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Clients.updateEntity(
                    body=clientDetails, 
                    id='clientUpdatetest'
                
                )
            )

