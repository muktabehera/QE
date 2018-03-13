# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-43842 - Proximity_Zones DELETE:

  Verify that user is able to delete the Proximity Zone using request DELETE /proximities{id}  with 'id' parameter.


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


@pytest.mark.components
@pytest.allure.story('Proximity_Zones')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Proximity_Zones test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43842')
    @pytest.mark.Proximity_Zones
    @pytest.mark.DELETE
    def test_TC_43842_DELETE_Proximity_Zones_Able_To_Delete_Proximity_Zone(self, context):
        """TC-43842 - Proximity_Zones-DELETE
           Verify that user is able to delete the Proximity Zone using request DELETE /proximities{id}  with 'id' parameter."""

        # Define a test step
        with pytest.allure.step('Able To Create Proximity Zone With Mandatory Parameters.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=1,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=False,
                configurations=[],
                id='ProximityPostDelete',
                name='ProximityPostDelete',
                proximityDetails=[proximityDetails])
            # POST the ProximityZone.
            # The `check` call validates return code and some of the swagger schema
            # (most schema checks are disabled)
            check(
                context.cl.Proximity_Zones.createEntity(
                    body=proximityZone
                )
            )

        # Define a test step
        with pytest.allure.step("""Now verify that user is able to delete the Proximity Zone using request DELETE /proximities{id}  with 'id' parameter."""):

            # deleteEntity the Proximity_Zones.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Proximity_Zones.deleteEntity(id='ProximityPostDelete')
            )

