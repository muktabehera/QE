# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-43878 - Proximity_Zones PATCH:

  Verify that user is able to Modify[Metric] with boundary value  (9 numeric ) for Proximity Zone using request PATCH /proximities{id} " .


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
   'name': 'metricmaxlenghUpdated',
   'proximityDetails': [{'cidr': '0.0.0.0/0', 'metric': 123456789, 'notes': ''}],
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43878')
    @pytest.mark.Proximity_Zones
    @pytest.mark.PATCH
    def test_TC_43878_PATCH_Proximity_Zones_Able_To_Modify_Proximity_Zone_Having_Maxlength_Of_9_Characters_In_Metric(self, context):
        """TC-43878 - Proximity_Zones-PATCH
           Verify that user is able to Modify[Metric] with boundary value  (9 numeric ) for Proximity Zone using request PATCH /proximities{id} " ."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to Modify[Metric] with boundary value  (9 numeric ) for Proximity Zone using request PATCH /proximities{id} " ."""):

            ### Positive test example

            # Test case configuration
            proximityZoneDetails = context.sc.ProximityZoneDetails(
                configAdminCanEdit=False,
                configurations=[],
                id=None,
                name='metricmaxlenghUpdated',
                proximityDetails=[{
                    'cidr': '0.0.0.0/0',
                    'metric': 123456789,
                    'notes': ''
                }],
                visibleInAllConfigurations=True)


            # updateEntity the Proximity_Zones.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Proximity_Zones.updateEntity(
                    id='ProximityUpdate',
                    body=proximityZoneDetails
                )
            )
