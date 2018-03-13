# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audiences.

* TC-43162 - Audiences PATCH:

  Verify that user is able to Modify[name] the details of Audience using request PATCH audiences/{id} ".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences/PATCH_Audience"

JSON data sent to PathFinder in this test:

  {'clients': [{'id': 'clientsWithAllDetails'}],
   'deliverySystems': [{'id': 'VNE_Testing_API'}],
   'id': 'PATCH_Audience',
   'name': 'PATCH_AudienceModified',
   'networkLocations': [{'id': 'NetworkLocationWithRulesGroups'}]}

"""

import pytest

from qe_common import *

logger = init_logger()



@pytest.mark.components
@pytest.allure.story('Audiences')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Audiences test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43162')
    @pytest.mark.Audiences
    @pytest.mark.PATCH
    def test_TC_43162_PATCH_Audiences_Modify_Name(self, context):
        """TC-43162 - Audiences-PATCH
           Verify that user is able to Modify[name] the details of Audience using request PATCH audiences/{id} "."""
        # Define a test step

        with pytest.allure.step(""" Create an Audience first using POST"""):

            # Test case configuration
            context.status.globals.deliverySystemsId = 'POST_veDevices_AllConfigAdminMulticastTrue'

            audienceDetails = context.sc.AudienceDetails(
                clients=[{
                    'id': 'clientsWithAllDetails'
                }],
                configurationId=None,
                deliverySystems=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                estimatedTimeForMulticastStreamsToBeAvailable=None,
                id='PATCH_Audience',
                name='PATCH_Audience',
                networkLocations=[{
                    'id': 'NetworkLocationWithRulesGroups'
                }])


            # createEntity the Audiences.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Audiences.createEntity(
                    body=audienceDetails
                )
            )


        with pytest.allure.step("""Verify that user is able to Modify[name] the details of Audience using request PATCH audiences/{id} "."""):

            # Test case configuration
            context.status.globals.deliverySystemsId = 'POST_veDevices_AllConfigAdminMulticastTrue'

            audienceDetails = context.sc.AudienceDetails(
                clients=[{
                    'id': 'clientsWithAllDetails'
                }],
                configurationId=None,
                deliverySystems=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                estimatedTimeForMulticastStreamsToBeAvailable=None,
                id='PATCH_Audience',
                name='PATCH_AudienceModified',
                networkLocations=[{
                    'id': 'NetworkLocationWithRulesGroups'
                }])


            # updateEntity the Audiences.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Audiences.updateEntity(
                    body=audienceDetails, 
                    id='PATCH_Audience'
                
                )
            )

