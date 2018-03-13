# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC-43841 - ProximityZone POST:

  Able To Create Proximity Zone On Providing Values In Correct Format In Cidr.


Equivalent test JSON payload:

{'configAdminCanEdit': False,
 'configurations': [],
 'id': 'qaqa13',
 'name': 'ab331',
 'proximityDetails': [{'cidr': '192.30.14.14/32', 'metric': 1, 'notes': '123'}],
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43841')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    def test_TC_43841_POST_ProximityZone_Able_To_Create_Proximity_Zone_On_Providing_Values_In_Correct_Format_In_Cidr(self, context):
        """TC-43841 - ProximityZone-POST - Able To Create Proximity Zone On Providing Values In Correct Format In Cidr"""
        # Define a test step
        with pytest.allure.step('Able To Create Proximity Zone On Providing Values In Correct Format In Cidr.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='192.30.14.14/32',
                metric=1,
                notes='123')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=False,
                configurations=[],
                id='qaqa13',
                name='ab331',
                proximityDetails=[proximityDetails])
            # POST the ProximityZone.
            # The `check` call validates return code and some of the swagger schema
            # (most schema checks are disabled)
            check(
                context.cl.Proximity_Zones.createEntity(
                    body=proximityZone
                )
            )
