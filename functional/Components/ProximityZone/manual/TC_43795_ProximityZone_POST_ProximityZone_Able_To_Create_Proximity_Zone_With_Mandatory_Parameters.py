"""PFE Component Tests - ProximityZone.

*** NOTE: This (TC-43795) test case has been moved to ``setup_components_prerequisites_test.py``.
          This file has been renamed, so it does not get executed automatically,
          to avoid conflict with setup_components_prerequisites_test.py execution.

* TC-43795 - ProximityZone POST:

  Able To Create Proximity Zone With Mandatory Parameters.


Equivalent test JSON payload:

{'configAdminCanEdit': False,
 'configurations': [],
 'id': 'ProximityPost',
 'name': 'ProximityPost',
 'proximityDetails': [{'cidr': '0.0.0.0/0', 'metric': 1, 'notes': ''}],
 'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('ProximityZone')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE ProximityZone test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43795')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    def test_TC_43795_POST_ProximityZone_Able_To_Create_Proximity_Zone_With_Mandatory_Parameters(self, context):
        """TC-43795 - ProximityZone-POST - Able To Create Proximity Zone With Mandatory Parameters"""
        # Define a test step
        with pytest.allure.step('Able To Create Proximity Zone With Mandatory Parameters.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=1,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=False,
                configurations=[],
                id='ProximityPost',
                name='ProximityPost',
                proximityDetails=[proximityDetails])
            # POST the ProximityZone.
            # The `check` call validates return code and some of the swagger schema
            # (most schema checks are disabled)
            check(
                context.cl.Proximity_Zones.createEntity(
                    body=context.status.proximityZone
                )
            )
