# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC-43836 - ProximityZone POST:

  Verify Correct Error Message Displayed On Entering Invalid Value Except Numbers In Metric.


Equivalent test JSON payload:

{
  "visibleInAllConfigurations": true,
  "configAdminCanEdit": false,
  "configurations": [],
  "id": "qa1234",
  "name": "metricmax1lengh",
  "proximityDetails": [

    {
      "cidr": "0.0.0.0/0",
      "metric": @#$3424*&^9123,
      "notes": ""
    }
  ]
}


"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('ProximityZone')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE ProximityZone test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43836')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    def test_TC_43836_POST_ProximityZone_Verify_Correct_Error_Message_Displayed_On_Entering_Invalid_Value_Except_Numbers_In_Metric(self, context):
        """TC-43836 - ProximityZone-POST - Verify Correct Error Message Displayed On Entering Invalid Value Except Numbers In Metric"""
        # Define a test step
        with pytest.allure.step('Verify Correct Error Message Displayed On Entering Invalid Value Except Numbers In Metric.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=1,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=False,
                configurations=[],
                id='qa1234',
                name='metricmax1lengh',
                proximityDetails=[proximityDetails])

            # prepare the request, so we can modify it
            request = context.cl.Proximity_Zones.createEntity(
                body=proximityZone
            )

            # Get the generated payload and corrupt the metric
            request.future.request.data = request.future.request.data.replace(
                '"metric": 1', '"metric": @#$3424*&^9123'
            )

            # POST the ProximityZone, and check we got the error we expect
            try:
                client, response = check(
                    request, quiet=True, returnResponse=True)
            except HTTPBadRequest as e:         # 400 error
                get_error_message(e) | expect.all(
                    should.start_with('Invalid request'),
                    should.contain('Unexpected character'),
                    should.contain('expected a valid value')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
