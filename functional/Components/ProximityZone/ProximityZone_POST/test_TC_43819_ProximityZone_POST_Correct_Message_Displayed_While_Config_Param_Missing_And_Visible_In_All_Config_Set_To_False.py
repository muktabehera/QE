# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC-43819 - ProximityZone POST:

  Correct Message Is Displayed While Configurations Parameter Is Missing And Visible In All Configurations Is Set To False.


Equivalent test JSON payload:

{'configAdminCanEdit': False,
 'configurations': [],
 'id': '1112',
 'name': 'ab1',
 'proximityDetails': [{'cidr': '0.0.0.0/0', 'metric': 123, 'notes': ''}],
 'visibleInAllConfigurations': False}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('ProximityZone')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE ProximityZone test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43819')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    def test_TC_43819_Configurations_Parameter_Is_Missing_And_Visible_In_All_Configurations_Is_Set_To_False(self, context):
        """TC-43819 - Correct Message Is Displayed While Configurations Parameter Is Missing And Visible In All Configurations Is Set To False"""
        # Define a test step
        with pytest.allure.step('Correct Message Is Displayed While Configurations Parameter Is Missing And VisibleInAllConfigurations Is False.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=123,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=False,
                configAdminCanEdit=False,
                configurations=[],
                id='1112',
                name='ab1',
                proximityDetails=[proximityDetails])
            # POST the ProximityZone, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Proximity_Zones.createEntity(body=proximityZone),
                    quiet=True, returnResponse=True)
            except HTTPBadRequest as e:         # 400 error
                get_error_message(e) | should.contain(
                    'Either provide the configurations where the system resource is visible or mark it visible in all configurations')
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
