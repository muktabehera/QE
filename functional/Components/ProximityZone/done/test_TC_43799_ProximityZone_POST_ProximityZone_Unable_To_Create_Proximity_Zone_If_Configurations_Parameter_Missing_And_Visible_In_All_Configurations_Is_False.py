# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC-43799 - ProximityZone POST:

  Unable To Create Proximity Zone If Configurations Parameter Missing And Visible In All Configurations Is False.


Equivalent test JSON payload:

{'configAdminCanEdit': False,
 'configurations': [],
 'id': 'ABCDE3FGH',
 'name': 'ABCDEFGH',
 'proximityDetails': [{'cidr': '0.0.0.0/0', 'metric': 2, 'notes': ''}],
 'visibleInAllConfigurations': False}

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43799')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    def test_TC_43799_Configurations_Parameter_Missing_And_Visible_In_All_Configurations_Is_False(self, context):
        """TC-43799 - Unable To Create Proximity Zone If Configurations Parameter Missing And Visible In All Configurations Is False"""
        # Define a test step
        with pytest.allure.step('Unable To Create Proximity Zone If Configurations Parameter Missing And Visible In All Configurations Is False.'):
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
