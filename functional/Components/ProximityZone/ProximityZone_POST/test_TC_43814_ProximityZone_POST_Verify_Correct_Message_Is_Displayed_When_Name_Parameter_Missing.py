# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC-43814 - ProximityZone POST:

  Verify Correct Message Is Displayed When Name Parameter Missing.


Equivalent test JSON payload:

{'configAdminCanEdit': True,
 'configurations': [],
 'id': 'no_name',
 'name': '',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43814')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    def test_TC_43814_POST_ProximityZone_Verify_Correct_Message_Is_Displayed_When_Name_Parameter_Missing(self, context):
        """TC-43814 - ProximityZone-POST - Verify Correct Message Is Displayed When Name Parameter Missing"""
        # Define a test step
        with pytest.allure.step('Verify Correct Message Is Displayed When Name Parameter Missing.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=2,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=True,
                configurations=[],
                id='no_name',
                name='',
                proximityDetails=[proximityDetails])
            # POST the ProximityZone, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Proximity_Zones.createEntity(body=proximityZone),
                    quiet=True, returnResponse=True)
            except HTTPBadRequest as e:         # 400 error
                get_error_message(e) | expect.any(
                    should.start_with('may not be empty'),
                    should.start_with('Invalid name'),
                    should.contain('length must be between 1 and 100')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
