# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audiences.

* TC-43012 - Audiences GET:

  Verify that user is able to GET the details of Audience using request  /audiences/{id}  using Audience ID.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences/POST_GETID"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Audiences')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Audiences test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43012')
    @pytest.mark.Audiences
    @pytest.mark.GET
    def test_TC_43012_GET_Audiences_Audience_Get_Details(self, context):
        """TC-43012 - Audiences-GET
           Verify that user is able to GET the details of Audience using request  /audiences/{id}  using Audience ID."""
        # Define a test step
        with pytest.allure.step("""Create Audience"""):

            # Test case configuration
            audienceDetails = context.sc.AudienceDetails(
                clients=[{
                    'id': 'clientsWithAllDetails'
                }],
                configurationId=None,
                deliverySystems=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrueTWO'
                }],
                estimatedTimeForMulticastStreamsToBeAvailable=None,
                id='POST_GETID',
                name='POST_GETID',
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
        with pytest.allure.step("""Verify that user is able to GET the details of Audience using request  /audiences/{id}  using Audience ID."""):

            # getEntity the Audiences.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Audiences.getEntity(
                    id='POST_GETID')
            )

