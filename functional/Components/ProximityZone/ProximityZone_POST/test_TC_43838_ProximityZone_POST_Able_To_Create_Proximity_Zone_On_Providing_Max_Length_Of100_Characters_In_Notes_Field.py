# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC-43838 - ProximityZone POST:

  Able To Create Proximity Zone On Providing Max Length Of 100 Characters In Notes Field.


Equivalent test JSON payload:

{'configAdminCanEdit': False,
 'configurations': [],
 'id': 'Newtworknoteslimit1',
 'name': 'Newtworknoteslimit1',
 'proximityDetails': [{'cidr': '0.0.0.0/0',
                       'metric': 1,
                       'notes': 'Newtwork11Newtwork11NewtworknoteslimitNewtworknoteslimitNewtworknoteslimitNewtwork11Newtwork11check1'}],
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43838')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    def test_TC_43838_POST_ProximityZone_Able_To_Create_Proximity_Zone_On_Providing_Max_Length_Of_100_Characters_In_Notes_Field(self, context):
        """TC-43838 - ProximityZone-POST - Able To Create Proximity Zone On Providing Max Length Of 100 Characters In Notes Field"""
        # Define a test step
        with pytest.allure.step('Able To Create Proximity Zone On Providing Max Length Of 100 Characters In Notes Field.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=1,
                notes='Newtwork11Newtwork11NewtworknoteslimitNewtworknoteslimitNewtworknoteslimitNewtwork11Newtwork11check1')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=False,
                configurations=[],
                id='Newtworknoteslimit1',
                name='Newtworknoteslimit1',
                proximityDetails=[proximityDetails])
            # POST the ProximityZone.
            # The `check` call validates return code and some of the swagger schema
            # (most schema checks are disabled)
            check(
                context.cl.Proximity_Zones.createEntity(
                    body=proximityZone
                )
            )
