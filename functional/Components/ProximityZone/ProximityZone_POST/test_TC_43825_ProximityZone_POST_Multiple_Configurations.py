# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC-43825 - ProximityZone POST:

  Multiple Configurations.


Equivalent test JSON payload: (modified to match PF configuration)

{'configAdminCanEdit': False,
 'configurations': [{'id': 'default'}, {'id': 'QA_Test'}],
 'id': 'ProximityPostDuplicateConfig',
 'name': 'ProximityDuplicateConfig',
 'proximityDetails': [{'cidr': '0.0.0.0/0', 'metric': 1, 'notes': ''}],
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43825')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    def test_TC_43825_POST_ProximityZone_Multiple_Configurations(self, context):
        """TC-43825 - ProximityZone-POST - Multiple Configurations"""
        # Define a test step
        with pytest.allure.step('Multiple Configurations.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=1,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=False,
                configAdminCanEdit=False,
                configurations=[
                    context.status['globals']['configId'],
                    context.status['globals']['tenantConfigId']
                ],
                id='ProximityPostDuplicateConfig',
                name='ProximityDuplicateConfig',
                proximityDetails=[proximityDetails])
            # POST the ProximityZone.
            # The `check` call validates return code and some of the swagger schema
            # (most schema checks are disabled)
            check(
                context.cl.Proximity_Zones.createEntity(
                    body=proximityZone
                )
            )
