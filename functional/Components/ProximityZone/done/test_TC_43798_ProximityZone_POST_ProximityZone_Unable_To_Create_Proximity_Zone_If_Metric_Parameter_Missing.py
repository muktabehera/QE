# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC-43798 - ProximityZone POST:

  Unable To Create Proximity Zone If Metric Parameter Missing.


Equivalent test JSON payload:

{
"visibleInAllConfigurations": true,
"configAdminCanEdit": false,
"configurations": [],
"id": "ABCDEFGH",
"name": "ABCDEFGH",
"proximityDetails": [
{ "cidr": "0.0.0.0/0", "metric": , "notes": "" }

]
}

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43798')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    def test_TC_43798_POST_ProximityZone_Unable_To_Create_Proximity_Zone_If_Metric_Parameter_Missing(self, context):
        """TC-43798 - ProximityZone-POST - Unable To Create Proximity Zone If Metric Parameter Missing"""
        # Define a test step
        with pytest.allure.step('Unable To Create Proximity Zone If Metric Parameter Missing.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=1,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=False,
                configAdminCanEdit=False,
                configurations=[],
                id='ProximityPostDuplicateConfig',
                name='ProximityDuplicateConfig',
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
