# -*- coding: UTF-8 -*-

"""PFE Component Tests - proximityZone.

* TC_43799_POST_ProximityZone__UnableToCreateProximityZoneIfConfigurationsParameterMissingAnd_visibleInAllConfigurationsIsFalse.

"""
import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Create a proximity zone')
@pytest.allure.feature('proximityZone')
class Test_PFE_Components(object):
    """PFE proximityZone test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC_43799')
    @pytest.mark.proximityZone
    @pytest.mark.post
    def test_TC_43799_POST_Configurations_Missing_visibleInAllConfigurationsIsFalse(self, context):
        """TC_43799_POST_ProximityZone__UnableToCreateProximityZoneIfConfigurationsParameterMissingAnd_visibleInAllConfigurationsIsFalse"""
        # Define a test step
        with pytest.allure.step(
            "Create proximityZone - Unable To Create Proximity Zone" +
            "If Configurations Parameter Missing And " +
            "visibleInAllConfigurations Is False."
        ):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=2,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=False,
                configAdminCanEdit=False,
                configurations=[],
                id='ABCDE3FGH',
                name='ABCDEFGH',
                proximityDetails=[proximityDetails])
            # Post the proximityZone, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Proximity_Zones.createEntity(body=proximityZone),
                    quiet=True, returnResponse=True)
            except HTTPBadRequest as e:         # 400 error
                get_error_message(e) | should.contain(
                    'Either provide the configurations ' +
                    'where the system resource is visible ' +
                    'or mark it visible in all configurations')
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
