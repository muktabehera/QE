# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC_43798_POST_ProximityZone_UnableToCreateProximityZoneIfMetricParameterMissing.

"""
import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Create a proximity zone')
@pytest.allure.feature('ProximityZone')
class Test_PFE_Components(object):
    """PFE ProximityZone test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43798')
    @pytest.mark.proximityZone
    @pytest.mark.post
    def test_TC_43798_POST_ProximityZone_UnableToCreateProximityZoneIfMetricParameterMissing(self, context):
        """TC_43798_POST_ProximityZone_UnableToCreateProximityZoneIfMetricParameterMissing"""
        # Define a test step
        # We put in the metric, and then delete it,
        # to work-around the swagger client schema validation
        with pytest.allure.step("Create ProximityZone - Unable To Create Proximity Zone If Metric Parameter Missing."):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=1,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=False,
                configurations=[],
                id='ABCDEFGH',
                name='ABCDEFGH',
                proximityDetails=[proximityDetails])
            # prepare the request
            request = context.cl.Proximity_Zones.createEntity(
                body=proximityZone
            )
            # Get the generated payload and corrupt the metric
            request.future.request.data = request.future.request.data.replace(
                '"metric": 1,', '"metric":,'
            )
            # Post the proximityZone request, and check for returned error.
            try:
                client, response = check(
                    request, quiet=True, returnResponse=True
                )
            except HTTPBadRequest as e:         # 400 error
                get_error_message(e) | should.start_with('Invalid request')
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
