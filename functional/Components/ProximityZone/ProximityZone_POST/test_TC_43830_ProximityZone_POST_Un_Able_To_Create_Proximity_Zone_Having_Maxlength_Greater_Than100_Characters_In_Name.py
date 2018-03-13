# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC-43830 - ProximityZone POST:

  Un Able To Create Proximity Zone Having Maxlength Greater Than 100 Characters In Name.


Equivalent test JSON payload:

{'configAdminCanEdit': False,
 'configurations': [],
 'id': '1112',
 'name': 'abcdefghijkl1342242345678abcdefghijkl12345678abcdefghijkl12345678abcdefghijkl12345678abcdefghijkl12345678',
 'proximityDetails': [{'cidr': '0.0.0.0/0', 'metric': 4, 'notes': ''}],
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43830')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    def test_TC_43830_POST_ProximityZone_Un_Able_To_Create_Proximity_Zone_Having_Maxlength_Greater_Than_100_Characters_In_Name(self, context):
        """TC-43830 - ProximityZone-POST - Un Able To Create Proximity Zone Having Maxlength Greater Than 100 Characters In Name"""
        # Define a test step
        with pytest.allure.step('Un Able To Create Proximity Zone Having Maxlength Greater Than 100 Characters In Name.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=4,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=False,
                configurations=[],
                id='1112',
                name='abcdefghijkl1342242345678abcdefghijkl12345678abcdefghijkl12345678abcdefghijkl12345678abcdefghijkl12345678',
                proximityDetails=[proximityDetails])
            # POST the ProximityZone, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Proximity_Zones.createEntity(body=proximityZone),
                    quiet=True, returnResponse=True)
            except HTTPBadRequest as e:         # 400 error
                get_error_message(e) | should.contain('length must be between 1 and 100')
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
