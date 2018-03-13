# -*- coding: UTF-8 -*-

"""PFE Component Tests - Pathfinder_Edge_Device_Profiles.

* TC-42609 - Pathfinder_Edge_Device_Profiles GET:

  Verify that user is able to GET VideoEdge Profile  details for GET request "/devices/veProfiles/{id}" .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veProfiles/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veProfiles/Proxy_profileByID1"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Pathfinder_Edge_Device_Profiles')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Pathfinder_Edge_Device_Profiles test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42609')
    @pytest.mark.Pathfinder_Edge_Device_Profiles
    @pytest.mark.GET
    def test_TC_42609_GET_Pathfinder_Edge_Device_Profiles_Video_Edge_Device_Profiles_Able_To_Get_With_Id(self, context):
        """TC-42609 - Pathfinder_Edge_Device_Profiles-GET
           Verify that user is able to GET VideoEdge Profile  details for GET request "/devices/veProfiles/{id}" ."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET VideoEdge Profile  details for GET request "/devices/veProfiles/{id}" ."""):

            ### Positive test example

            # getEntity the Pathfinder_Edge_Device_Profiles.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Pathfinder_Edge_Device_Profiles.getEntity(
                    id='Proxy_profileByID1')
            )

        with pytest.allure.step("""Verify that user is able to GET VideoEdge Profile  details for GET request "/devices/veProfiles/{id}" ."""):

            ### Negative test example

            # getEntity the Pathfinder_Edge_Device_Profiles, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Pathfinder_Edge_Device_Profiles.getEntity(
                        id='Proxy_profileByID1'),
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('may not be empty'),
                    should.start_with('Invalid page parameter specified'),
                    should.contain('Invalid Authorization Token')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
