# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audiences.

* TC-43160 - Audiences DELETE:

  Verify that user is able to delete the Audience using request DELETE audiences/{id} .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences/Delete_Audience"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Audiences')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Audiences test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43160')
    @pytest.mark.Audiences
    @pytest.mark.DELETE
    def test_TC_43160_DELETE_Audiences_Id(self, context):
        """TC-43160 - Audiences-DELETE
           Verify that user is able to delete the Audience using request DELETE audiences/{id} ."""
        # Define a test step
        with pytest.allure.step("""Create an Audience first"""):

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
                id='Delete_Audience1',
                name='Delete_Audience1',
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

        with pytest.allure.step("""Verify that user is able to delete the Audience using request DELETE audiences/{id} ."""):

            # deleteEntity the Audiences.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Audiences.deleteEntity(
                    id='Delete_Audience1')
            )

