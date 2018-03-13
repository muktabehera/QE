# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC-43802 - ProximityZone POST:

  Able To Create Proximity Zone With Configurations Parameter And Visible In All Configurations Is False.


Equivalent test JSON payload: (modified to match PF configuration)

{'configAdminCanEdit': False,
 'configurations': [{'host': '172.30.5.204', 'id': 'default'}],
 'id': 'pz123492',
 'name': 'pz123492',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43802')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    def test_TC_43802_Create_Proximity_Zone_With_Configurations_Parameter_And_Visible_In_All_Configurations_Is_False(self, context):
        """TC-43802 - ProximityZone-POST - Able To Create Proximity Zone With Configurations Parameter And Visible In All Configurations Is False"""
        # Define a test step
        with pytest.allure.step('Able To Create Proximity Zone With Configurations Parameter And Visible In All Configurations Is False.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=2,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=False,
                configAdminCanEdit=False,
                configurations=[context.status['globals']['configId']],
                id='pz123492',
                name='pz123492',
                proximityDetails=[proximityDetails])
            # POST the ProximityZone.
            # The `check` call validates return code and some of the swagger schema
            # (most schema checks are disabled)
            check(
                context.cl.Proximity_Zones.createEntity(
                    body=proximityZone
                )
            )
