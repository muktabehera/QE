# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC-43818 - ProximityZone POST:

  Correct Message Is Displayed On Providing Invalid Value Starting With Number Or Special Character For Name Parameter.


Equivalent test JSON payload:

{'configAdminCanEdit': True,
 'configurations': [],
 'id': 'a1b12c1',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43818')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    def test_TC_43818_Invalid_Value_Starting_With_Number_Or_Special_Character_For_Name_Parameter(self, context):
        """TC-43818 - Correct Message Is Displayed On Providing Invalid Value Starting With Number Or Special Character For Name Parameter"""
        # Define a test step
        with pytest.allure.step('Correct Message Is Displayed On Providing Invalid Value Starting With Number/Special Character For Name Parameter.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=2,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=True,
                configurations=[],
                id='a1b12c1',
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
