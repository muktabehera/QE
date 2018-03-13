# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC-43801 - ProximityZone POST:

  Able To Create Proximity Zone With Configurations Parameter And Visible In All Configurations Is True.


Equivalent test JSON payload: (modified to match PF configuration)

{'configAdminCanEdit': False,
 'configurations': [{'host': '172.30.5.204', 'id': 'default'}],
 'id': 'pz12349',
 'name': 'pz12349',
 'proximityDetails': [{'cidr': '0.0.0.0/0', 'metric': 2, 'notes': ''}],
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43801')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    def test_TC_43801_Create_Proximity_Zone_With_Configurations_Parameter_And_Visible_In_All_Configurations_Is_True(self, context):
        """TC-43801 - ProximityZone-POST - Able To Create Proximity Zone With Configurations Parameter And Visible In All Configurations Is True"""
        # Define a test step
        with pytest.allure.step('Able To Create Proximity Zone With Configurations Parameter And Visible In All Configurations Is True.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=2,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=False,
                configurations=[context.status['globals']['configId']],
                id='pz12349',
                name='pz12349',
                proximityDetails=[proximityDetails])
            # POST the ProximityZone.
            # The `check` call validates return code and some of the swagger schema
            # (most schema checks are disabled)
            check(
                context.cl.Proximity_Zones.createEntity(
                    body=proximityZone
                )
            )
