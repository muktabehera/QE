# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC-43833 - ProximityZone POST:

  Un Able To Create Proximity Zone Having Maxlength Greater Than 9 Characters In Metric.


Equivalent test JSON payload:

{'configAdminCanEdit': False,
 'configurations': [],
 'id': 'qa1234',
 'name': 'metricmax1lengh',
 'proximityDetails': [{'cidr': '0.0.0.0/0',
                       'metric': 123456789012,
                       'notes': ''}],
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43833')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    def test_TC_43833_POST_ProximityZone_Un_Able_To_Create_Proximity_Zone_Having_Maxlength_Greater_Than_9_Characters_In_Metric(self, context):
        """TC-43833 - ProximityZone-POST - Un Able To Create Proximity Zone Having Maxlength Greater Than 9 Characters In Metric"""
        # Define a test step
        with pytest.allure.step('Un Able To Create Proximity Zone Having Maxlength Greater Than 9 Characters In Metric.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=123456789012,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=False,
                configurations=[],
                id='qa1234',
                name='metricmax1lengh',
                proximityDetails=[proximityDetails])
            # POST the ProximityZone, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Proximity_Zones.createEntity(body=proximityZone),
                    quiet=True, returnResponse=True)
            except HTTPBadRequest as e:         # 400 error
                get_error_message(e) | expect.all(
                    should.start_with('Invalid request'),
                    should.contain('Numeric value'),
                    should.contain('out of range of int')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
