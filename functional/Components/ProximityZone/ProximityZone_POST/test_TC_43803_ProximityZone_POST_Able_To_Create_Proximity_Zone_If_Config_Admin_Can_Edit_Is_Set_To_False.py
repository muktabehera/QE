# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC-43803 - ProximityZone POST:

  Able To Create Proximity Zone If Config Admin Can Edit Is Set To False.


Equivalent test JSON payload: (modified to match PF configuration)

{'configAdminCanEdit': False,
 'configurations': [{'host': '172.30.2.149', 'id': 'default'}],
 'id': 'configadmin_false',
 'name': 'configadmin_false',
 'proximityDetails': [{'cidr': '0.0.0.0/0', 'metric': 2, 'notes': ''}],
 'visibleInAllConfigurations': False}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('ProximityZone')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE ProximityZone test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43803')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    def test_TC_43803_POST_ProximityZone_Able_To_Create_Proximity_Zone_If_Config_Admin_Can_Edit_Is_Set_To_False(self, context):
        """TC-43803 - ProximityZone-POST - Able To Create Proximity Zone If Config Admin Can Edit Is Set To False"""
        # Define a test step
        with pytest.allure.step('Able To Create Proximity Zone If Config Admin Can Edit Is Set To False.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=2,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=False,
                configAdminCanEdit=False,
                configurations=[context.status['globals']['configId']],
                id='configadmin_false',
                name='configadmin_false',
                proximityDetails=[proximityDetails])
            # POST the ProximityZone.
            # The `check` call validates return code and some of the swagger schema
            # (most schema checks are disabled)
            check(
                context.cl.Proximity_Zones.createEntity(
                    body=proximityZone
                )
            )
