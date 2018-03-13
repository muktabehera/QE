# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC-43832 - ProximityZone POST:

  Able To Create Proximity Zone Having Maxlength Of 9 Characters In Metric.


Equivalent test JSON payload:

{'configAdminCanEdit': False,
 'configurations': [],
 'id': 'metric',
 'name': 'metricmaxlengh12',
 'proximityDetails': [{'cidr': '0.0.0.0/0', 'metric': 123456789, 'notes': ''}],
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43832')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    def test_TC_43832_POST_ProximityZone_Able_To_Create_Proximity_Zone_Having_Maxlength_Of_9_Characters_In_Metric(self, context):
        """TC-43832 - ProximityZone-POST - Able To Create Proximity Zone Having Maxlength Of 9 Characters In Metric"""
        # Define a test step
        with pytest.allure.step('Able To Create Proximity Zone Having Maxlength Of 9 Characters In Metric.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=123456789,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=False,
                configurations=[],
                id='metric',
                name='metricmaxlengh12',
                proximityDetails=[proximityDetails])
            # POST the ProximityZone.
            # The `check` call validates return code and some of the swagger schema
            # (most schema checks are disabled)
            check(
                context.cl.Proximity_Zones.createEntity(
                    body=proximityZone
                )
            )
