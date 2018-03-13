# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-43886 - Proximity_Zones PATCH:

  Verify that user is able to Modify[Notes] by providing max length of 1000 characters for Proximity Zone using request PATCH /proximities{id} " .


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
   'name': 'UpdatedNotesMaxLength1000Character',
   'proximityDetails': [{'cidr': '0.0.0.0/0',
                         'metric': 3,
                         'notes': '1234567890123434234256789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012343423425678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234342342567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123434234256789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012343423425678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234342342567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123434234256789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012343423425678901234567890123456789012'}],
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43886')
    @pytest.mark.Proximity_Zones
    @pytest.mark.PATCH
    def test_TC_43886_PATCH_Proximity_Zones_Able_To_Create_Proximity_On_Providing_Max_Length_1000_Characters_In_Notes_Field(self, context):
        """TC-43886 - Proximity_Zones-PATCH
           Verify that user is able to Modify[Notes] by providing max length of 1000 characters for Proximity Zone using request PATCH /proximities{id} " ."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to Modify[Notes] by providing max length of 1000 characters for Proximity Zone using request PATCH /proximities{id} " ."""):

            # Test case configuration
            proximityZoneDetails = context.sc.ProximityZoneDetails(
                configAdminCanEdit=False,
                configurations=[],
                id=None,
                name='UpdatedNotesMaxLength1000Character',
                proximityDetails=[{
                    'cidr':
                    '0.0.0.0/0',
                    'metric':
                    3,
                    'notes':
                    '1234567890123434234256789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012343423425678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234342342567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123434234256789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012343423425678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234342342567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123434234256789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012343423425678901234567890123456789012'
                }],
                visibleInAllConfigurations=True)


            # updateEntity the Proximity_Zones.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Proximity_Zones.updateEntity(
                    id='ProximityUpdate',
                    body=proximityZoneDetails
                )
            )

