# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-43843 - Proximity_Zones DELETE:

  Verify that error message is displayed on providing Proximity Zone ID which is already deleted using equest DELETE /proximities{id}  with 'id' parameter.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/ProximityDELETE"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/ProximityDELETE"

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43843')
    @pytest.mark.Proximity_Zones
    @pytest.mark.DELETE
    def test_TC_43843_DELETE_Proximity_Zones_Error_Message_Is_Displayed_On_Deleting_Already_Deleted_Id(self, context):
        """TC-43843 - Proximity_Zones-DELETE
           Verify that error message is displayed on providing Proximity Zone ID which is already deleted using equest DELETE /proximities{id}  with 'id' parameter."""
        # Define a test step
        with pytest.allure.step("""Verify that error message is displayed on providing Proximity Zone ID which is already deleted using equest DELETE /proximities{id}  with 'id' parameter."""):

             # deleteEntity the Proximity_Zones, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Proximity_Zones.deleteEntity(id='ProximityPost'),
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 404 error
                get_error_message(e) | expect.any(
                    should.start_with('Delivery Service entity not found')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
