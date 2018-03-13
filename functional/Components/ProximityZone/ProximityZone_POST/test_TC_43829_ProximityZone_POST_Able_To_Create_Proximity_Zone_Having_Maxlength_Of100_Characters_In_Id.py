# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC-43829 - ProximityZone POST:

  Able To Create Proximity Zone Having Maxlength Of 100 Characters In Id.


Equivalent test JSON payload:

{'configAdminCanEdit': False,
 'configurations': [],
 'id': 'abcdefghijkl12345678abcdefghijkl12345678abcdefghijkl12345678abcdefghijkl12345678abcdefghijkl23456678',
 'name': 'long id',
 'proximityDetails': [{'cidr': '0.0.0.0/0', 'metric': 12, 'notes': ''}],
 'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('ProximityZone')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE ProximityZone test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43829')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    def test_TC_43829_POST_ProximityZone_Able_To_Create_Proximity_Zone_Having_Maxlength_Of_100_Characters_In_Id(self, context):
        """TC-43829 - ProximityZone-POST - Able To Create Proximity Zone Having Maxlength Of 100 Characters In Id"""
        # Define a test step
        with pytest.allure.step('Able To Create Proximity Zone Having Maxlength Of 100 Characters In Id.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=12,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=False,
                configurations=[],
                id='abcdefghijkl12345678abcdefghijkl12345678abcdefghijkl12345678abcdefghijkl12345678abcdefghijkl23456678',
                name='long id',
                proximityDetails=[proximityDetails])
            # POST the ProximityZone.
            # The `check` call validates return code and some of the swagger schema
            # (most schema checks are disabled)
            check(
                context.cl.Proximity_Zones.createEntity(
                    body=proximityZone
                )
            )
