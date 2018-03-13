# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-42567 - Proximity_Zones DELETE:

  Verify that user is able to Create entities under "VideoNet Configuration" with "Manage Configuration" permission while "Config admin can create" flag is set to true, within the token expiration time.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/deleteProximityPersmission"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Proximity_Zones')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Proximity_Zones test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42567')
    @pytest.mark.Proximity_Zones
    @pytest.mark.DELETE
    def test_TC_42567_DELETE_Proximity_Zones_Admin_Create_Config_True(self, context):
        """TC-42567 - Proximity_Zones-DELETE
           Verify that user is able to Create entities under "VideoNet Configuration" with "Manage Configuration" permission while "Config admin can create" flag is set to true, within the token expiration time."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to Create entities under "VideoNet Configuration" with "Manage Configuration" permission while "Config admin can create" flag is set to true, within the token expiration time."""):

            ### Positive test example

            # deleteEntity the Proximity_Zones.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Proximity_Zones.deleteEntity(
                    id='deleteProximityPersmission')
            )

        with pytest.allure.step("""Verify that user is able to Create entities under "VideoNet Configuration" with "Manage Configuration" permission while "Config admin can create" flag is set to true, within the token expiration time."""):

            ### Negative test example

            # deleteEntity the Proximity_Zones, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Proximity_Zones.deleteEntity(
                        id='deleteProximityPersmission'),
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
