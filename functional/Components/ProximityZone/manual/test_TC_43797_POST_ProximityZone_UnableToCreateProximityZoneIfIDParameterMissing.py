# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity Zones.

* TC_43797_POST_ProximityZone_UnableToCreateProximityZoneIfIDParameterMissing.

"""
import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.mark.proximityZone
@pytest.allure.story('Create a proximity zone')
@pytest.allure.feature('Proximity Zones')
class Test_PFE_Components(object):
    """PFE Proximity Zone creation test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43797')
    @pytest.mark.post
    def test_TC_43797_POST_ProximityZone_UnableToCreateProximityZoneIfIDParameterMissing(self, context):
        """TC_43797_POST_ProximityZone_UnableToCreateProximityZoneIfIDParameterMissing"""
        # Define a test step
        with pytest.allure.step("Create proximityZone - Unable To Create Proximity Zone If ID Parameter Missing."):
            # Per Swagger schema, proximityDetails is an object
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=1,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=False,
                configurations=[],
                id='',
                name='ABCDEFGH',
                proximityDetails=[proximityDetails])
            # Post the proximityZone, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Proximity_Zones.createEntity(body=proximityZone),
                    quiet=True, returnResponse=True)
            except HTTPBadRequest as e:         # 400 error
                get_error_message(e) | expect.any(
                    should.start_with('may not be empty'),
                    should.start_with('Invalid identifier'),
                    should.contain('length must be between 1 and 100')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
