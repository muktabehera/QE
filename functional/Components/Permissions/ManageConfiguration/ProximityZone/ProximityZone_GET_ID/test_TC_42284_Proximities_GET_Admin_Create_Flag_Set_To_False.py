# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-42284 - Proximity_Zones GET:

  Verify that Create button is not displayed on 'Proximities zones' page under Intelligent Content Routing menu for user with "Manage Configuration" permission, while "Config admin can create" flag is set to false within the token expiration time.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/auto_proximity"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Proximity_Zones')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Proximity_Zones test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42284')
    @pytest.mark.Proximity_Zones
    @pytest.mark.GET
    def test_TC_42284_GET_Proximity_Zones_Admin_Create_Flag_Set_To_False(self, context):
        """TC-42284 - Proximity_Zones-GET
           Verify that Create button is not displayed on 'Proximities zones' page under Intelligent Content Routing menu for user with "Manage Configuration" permission, while "Config admin can create" flag is set to false within the token expiration time."""
        # Define a test step
        with pytest.allure.step("""Verify that Create button is not displayed on 'Proximities zones' page under Intelligent Content Routing menu for user with "Manage Configuration" permission, while "Config admin can create" flag is set to false within the token expiration time."""):

            ### Positive test example

            # getEntity the Proximity_Zones.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Proximity_Zones.getEntity(
                    id='auto_proximity')
            )

        with pytest.allure.step("""Verify that Create button is not displayed on 'Proximities zones' page under Intelligent Content Routing menu for user with "Manage Configuration" permission, while "Config admin can create" flag is set to false within the token expiration time."""):

            ### Negative test example

            # getEntity the Proximity_Zones, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Proximity_Zones.getEntity(
                        id='auto_proximity'),
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
