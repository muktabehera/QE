# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-43791 - Proximity_Zones GET:

  Verify that user is able to GET the details of  proximities using request /proximities/{id} using proximity ID.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/ProximityPost"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/ProximityPost"

"""

import pytest

from qe_common import *

logger = init_logger()







@pytest.mark.components
@pytest.allure.story('Proximity_Zones')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Proximity_Zones test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43791')
    @pytest.mark.Proximity_Zones
    @pytest.mark.GET
    def test_TC_43791_GET_Proximity_Zones_Able_To_Get_Details_With_Proximity_Id(self, context):
        """TC-43791 - Proximity_Zones-GET
           Verify that user is able to GET the details of  proximities using request /proximities/{id} using proximity ID."""
        # Define a test step
        with pytest.allure.step('First Create Proximity Zone With Mandatory Parameters.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=1,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=False,
                configurations=[],
                id='ProximityPost1',
                name='ProximityPost1',
                proximityDetails=[proximityDetails])
            # POST the ProximityZone.
            # The `check` call validates return code and some of the swagger schema
            # (most schema checks are disabled)
            check(
                context.cl.Proximity_Zones.createEntity(
                    body=proximityZone
                )
            )


        with pytest.allure.step("""Verify that user is able to GET the details of  proximities using request /proximities/{id} using proximity ID."""):

            # listEntities the Proximity_Zones using proximity ID.

            check(
                context.cl.Proximity_Zones.getEntity(id='ProximityPost1')
            )
