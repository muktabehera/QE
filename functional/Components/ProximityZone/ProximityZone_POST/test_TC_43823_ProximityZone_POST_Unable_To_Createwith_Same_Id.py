# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC-43823 - ProximityZone POST:

  Unable To Createwith Same Id.


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


@pytest.mark.components
@pytest.allure.story('ProximityZone')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE ProximityZone test cases."""

    # @pytest.allure.testcase('TC-43823')
    @pytest.allure.link('https://jira.qumu.com/browse/TC-43823')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    # @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @flaky(max_runs=3, min_passes=3, rerun_filter=delay_rerun)
    def test_TC_43823_POST_ProximityZone_Unable_To_Createwith_Same_Id(self, context):
        """TC-43823 - ProximityZone-POST - Unable To Createwith Same Id."""
        # Define a test step
        with pytest.allure.step('First create a Proximity Zone.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=1,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=False,
                configurations=[],
                id='ProximityPostSameid',
                name='ProximityPostSameid',
                proximityDetails=[proximityDetails])
            # POST the ProximityZone.
            # The `check` call validates return code and some of the swagger schema
            # (most schema checks are disabled)
            check(
                context.cl.Proximity_Zones.createEntity(
                    body=proximityZone
                )
            )


        # Define a test step
        with pytest.allure.step('Verify that unable To Create Proximity Zone with Same Id.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=1,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=False,
                configurations=[],
                id='ProximityPostSameid',
                name='ProximityPostSameidTest',
                proximityDetails=[proximityDetails])
            # POST the ProximityZone, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Proximity_Zones.createEntity(body=proximityZone),
                    quiet=True, returnResponse=True)
            except HTTPConflict as e:         # 409 error
                get_error_message(e) | should.contain('The ID value you have specified is in use or is invalid')
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
