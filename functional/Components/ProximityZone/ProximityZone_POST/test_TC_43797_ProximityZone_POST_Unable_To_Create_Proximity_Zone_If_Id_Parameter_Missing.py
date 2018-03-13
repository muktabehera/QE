# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC-43797 - ProximityZone POST:

  Unable To Create Proximity Zone If Id Parameter Missing.


Equivalent test JSON payload:

{'configAdminCanEdit': False,
 'configurations': [],
 'id': '',
 'name': 'ABCDEFGH',
 'proximityDetails': [{'cidr': '0.0.0.0/0', 'metric': 1, 'notes': ''}],
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43797')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    def test_TC_43797_POST_ProximityZone_Unable_To_Create_Proximity_Zone_If_Id_Parameter_Missing(self, context):
        """TC-43797 - ProximityZone-POST - Unable To Create Proximity Zone If Id Parameter Missing"""
        # Define a test step
        with pytest.allure.step('Unable To Create Proximity Zone If Id Parameter Missing.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=1,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=False,
                configurations=[],
                id='',
                name='ABCDEFGH',
                proximityDetails=[proximityDetails])
            # POST the ProximityZone, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Proximity_Zones.createEntity(body=proximityZone),
                    quiet=True, returnResponse=True)
            except HTTPBadRequest as e:         # 400 error
                get_error_message(e) | expect.any(
                    should.start_with('may not be empty'),
                    should.start_with('Invalid identifier'),
                    should.contain('length must be between 1 and 100')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
