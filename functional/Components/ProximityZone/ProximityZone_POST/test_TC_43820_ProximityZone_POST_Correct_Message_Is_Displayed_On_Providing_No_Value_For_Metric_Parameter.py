# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC-43820 - ProximityZone POST:

  Correct Message Is Displayed On Providing No Value For Metric Parameter.


Equivalent test JSON payload:

{'configAdminCanEdit': False,
 'configurations': [],
 'id': '1112',
 'name': 'ab1',
 'proximityDetails': [{'cidr': '0.0.0.0/0', 'metric': '', 'notes': ''}],
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43820')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    def test_TC_43820_POST_ProximityZone_Correct_Message_Is_Displayed_On_Providing_No_Value_For_Metric_Parameter(self, context):
        """TC-43820 - ProximityZone-POST - Correct Message Is Displayed On Providing No Value For Metric Parameter"""
        # Define a test step
        with pytest.allure.step('Correct Message Is Displayed On Providing No Value For Metric Parameter.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=1,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=False,
                configurations=[],
                id='1112',
                name='ab1',
                proximityDetails=[proximityDetails])

            # prepare the request, so we can modify it
            request = context.cl.Proximity_Zones.createEntity(
                body=proximityZone
            )

            # Get the generated payload and corrupt the metric
            request.future.request.data = request.future.request.data.replace(
                '"metric": 1', '"metric":'
            )

            # POST the ProximityZone, and check we got the error we expect
            try:
                client, response = check(
                    request, quiet=True, returnResponse=True)
            except HTTPBadRequest as e:         # 400 error
                get_error_message(e) | should.start_with('Invalid request')
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
