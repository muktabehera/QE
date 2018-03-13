# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audiences.

* TC-43155 - Audiences POST:

  Verify that user is able to create Audience  having Max length of 100 characters in Name parameter using request POST /audiences.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences"

JSON data sent to PathFinder in this test:

  {'clients': [{'id': 'clientsWithAllDetails'}, {'id': 'autoclient'}],
   'deliverySystems': [{'id': 'VNE_Testing_API'}],
   'id': 'POST_audience_NameUpto100Characters',
   'name': 'POST_audience_NameUpto100CharactersPOST_audience_NameUpto100CharactersPOST_audience_NameUpto100Chara',
   'networkLocations': [{'id': 'NetworkLocationWithRulesGroups'}]}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Audiences')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Audiences test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43155')
    @pytest.mark.Audiences
    @pytest.mark.POST
    def test_TC_43155_POST_Audiences_Name_Upto_100_Characters(self, context):
        """TC-43155 - Audiences-POST
           Verify that user is able to create Audience  having Max length of 100 characters in Name parameter using request POST /audiences."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create Audience  having Max length of 100 characters in Name parameter using request POST /audiences."""):

            # Test case configuration
            audienceDetails = context.sc.AudienceDetails(
                clients=[{
                    'id': 'clientsWithAllDetails'
                }],
                configurationId=None,
                deliverySystems=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                estimatedTimeForMulticastStreamsToBeAvailable=None,
                id='POST_audience_NameUpto100Characters',
                name=
                'POST_audience_NameUpto100CharactersPOST_audience_NameUpto100CharactersPOST_audience_NameUpto100Chara',
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

