# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC-43824 - ProximityZone POST:

  Able To Createwith Same Name Unique Id Value.


Equivalent test JSON payload:

{'configAdminCanEdit': False,
 'configurations': [],
 'id': 'ProximityPostNew',
 'name': 'ProximityPost',
 'proximityDetails': [{'cidr': '0.0.0.0/0', 'metric': 1, 'notes': ''}],
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43824')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    def test_TC_43824_POST_ProximityZone_Able_To_Createwith_Same_Name_Unique_Id_Value(self, context):
        """TC-43824 - ProximityZone-POST - Able To Createwith Same Name Unique Id Value"""
        # Define a test step
        with pytest.allure.step('Able To Createwith Same Name Unique Id Value.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=1,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=False,
                configurations=[],
                id='ProximityPostNew',
                name='ProximityPost',
                proximityDetails=[proximityDetails])
            # POST the ProximityZone.
            # The `check` call validates return code and some of the swagger schema
            # (most schema checks are disabled)
            check(
                context.cl.Proximity_Zones.createEntity(
                    body=proximityZone
                )
            )
