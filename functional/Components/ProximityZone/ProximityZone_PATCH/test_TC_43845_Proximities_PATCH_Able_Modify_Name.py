# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-43845 - Proximity_Zones PATCH:

  Verify that user is able to Modify[name] of Proximity Zone using request PATCH /proximities{id} " .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/ProximityUpdate"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/ProximityUpdate"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': False,
   'configurations': [],
   'name': 'ProximityUpdated',
   'proximityDetails': [{'cidr': '0.0.0.0/0', 'metric': 1, 'notes': ''}],
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()







@pytest.mark.components
@pytest.allure.story('Proximity_Zones')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Proximity_Zones test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43845')
    @pytest.mark.Proximity_Zones
    @pytest.mark.PATCH
    def test_TC_43845_PATCH_Proximity_Zones_Able_Modify_Name(self, context):
        """TC-43845 - Proximity_Zones-PATCH
           Verify that user is able to Modify[name] of Proximity Zone using request PATCH /proximities{id} " ."""
        # Define a test step
        with pytest.allure.step('First create Proximity Zone'):
            # Test case configuration
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=1,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=False,
                configurations=[],
                id='ProximityPosttest',
                name='ProximityPosttest',
                proximityDetails=[proximityDetails])
            # POST the ProximityZone.
            # The `check` call validates return code and some of the swagger schema
            # (most schema checks are disabled)
            check(
                context.cl.Proximity_Zones.createEntity(
                    body=proximityZone
                )
            )


        with pytest.allure.step("""Verify that user is able to Modify[name] of Proximity Zone using request PATCH /proximities{id} " ."""):

            # Test case configuration
            proximityZoneDetails = context.sc.ProximityZoneDetails(
                configAdminCanEdit=False,
                configurations=[],
                id=None,
                name='ProximityUpdated2',
                proximityDetails=[{
                    'cidr': '0.0.0.0/0',
                    'metric': 1,
                    'notes': 'updated'
                }],
                visibleInAllConfigurations=True)


            # updateEntity the Proximity_Zones using Proximity Id.
            check(
                context.cl.Proximity_Zones.updateEntity(
                    id='ProximityPosttest', body=proximityZoneDetails)
            )

