# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audiences.

* TC-43014 - Audiences POST:

  Verify that user is able to GET the details of Audience having id with 100 characters using request /audiences/{id}  using Audience ID.


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
   'id': 'POST_GETID_100CHaracters12-...:fml...mfsl..mfsm0heswhkejwk3243798283942hffkjsjkfkfksbfkbhrhjhjhjh398',
   'name': 'POST_GETID_100CHaracters12-...:fml...mfsl..mfsm0heswhkejwk3243798283942hffkjsjkfkfksbfkbhrhjhjhjh398',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43014')
    @pytest.mark.Audiences
    @pytest.mark.POST
    def test_TC_43014_POST_Audiences_Audience_Get_Id_100_Character_Id(self, context):
        """TC-43014 - Audiences-POST
           Verify that user is able to GET the details of Audience having id with 100 characters using request /audiences/{id}  using Audience ID."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create an Audience having id with 100 characters using request /POST  """):

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
                id=
                'qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiop',
                name=
                'POST_GETID_100CHaracters',
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

        # Define a test step
        with pytest.allure.step( """Verify that user is able to GET the details of Audience having id with 100 characters using request /audiences/{id}  using Audience ID."""):
            # Test case configuration
            check(
                context.cl.Audiences.getEntity(
                    id=
                'qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiop'
                )
            )