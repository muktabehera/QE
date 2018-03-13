# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC-43817 - ProximityZone POST:

  Unable To Create Proximity Zone Having Name Starting With Number Or Special Character.


Equivalent test JSON payload:

{'configAdminCanEdit': True,
 'configurations': [],
 'id': 'a1b1c1',
 'name': '2<>abc',
 'proximityDetails': [{'cidr': '0.0.0.0/0', 'metric': 2, 'notes': ''}],
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43817')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    def test_TC_43817_POST_ProximityZone_Unable_To_Create_Proximity_Zone_Having_Name_Starting_With_Number_Or_Special_Character(self, context):
        """TC-43817 - ProximityZone-POST - Unable To Create Proximity Zone Having Name Starting With Number Or Special Character"""
        # Define a test step
        with pytest.allure.step('Unable To Create Proximity Zone Having Name Starting With Number Or Special Character.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=2,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=True,
                configurations=[],
                id='a1b1c1',
                name='2<>abc',
                proximityDetails=[proximityDetails])
            # POST the ProximityZone, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Proximity_Zones.createEntity(body=proximityZone),
                    quiet=True, returnResponse=True)
            except HTTPBadRequest as e:         # 400 error
                get_error_message(e) | should.start_with('Invalid name')
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
