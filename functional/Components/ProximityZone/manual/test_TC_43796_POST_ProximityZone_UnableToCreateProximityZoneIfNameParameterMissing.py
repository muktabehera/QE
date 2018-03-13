# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity Zones.

* TC_43796_POST_ProximityZone_UnableToCreateProximityZoneIfNameParameterMissing.

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43796')
    @pytest.allure.link('https://jira.qumu.com/browse/QED-1940')
    @pytest.mark.post
    def test_TC_43796_POST_ProximityZone_UnableToCreateProximityZoneIfNameParameterMissing(self, context):
        """TC_43796_POST_ProximityZone_UnableToCreateProximityZoneIfNameParameterMissing"""
        # Define a test step
        with pytest.allure.step("Create proximityZone - Unable To Create Proximity Zone If Name Parameter Missing."):
            # Per Swagger schema, proximityDetails is an object
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=1,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=False,
                configurations=[],
                id='test12',
                name='',
                proximityDetails=[proximityDetails])
            # Post the proximityZone, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Proximity_Zones.createEntity(body=proximityZone),
                    quiet=True, returnResponse=True)
            except HTTPBadRequest as e:         # 400 error
                # Multiple error messages are retured - QED-1940
                get_error_message(e) | expect.any(
                    should.start_with('may not be empty'),
                    should.start_with('Invalid name, the pattern must match'),
                    should.contain('length must be between 1 and 100')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
