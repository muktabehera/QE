# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC-43822 - ProximityZone POST:

  Unable To Create Proximity Zone If Invalid Value Is Provided For Cidr.


Equivalent test JSON payload:

{'configAdminCanEdit': False,
 'configurations': [],
 'id': '1112',
 'name': 'ab1',
 'proximityDetails': [{'cidr': '234234234234abcd#$@#$',
                       'metric': 12,
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43822')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    def test_TC_43822_POST_ProximityZone_Unable_To_Create_Proximity_Zone_If_Invalid_Value_Is_Provided_For_Cidr(self, context):
        """TC-43822 - ProximityZone-POST - Unable To Create Proximity Zone If Invalid Value Is Provided For Cidr"""
        # Define a test step
        with pytest.allure.step('Unable To Create Proximity Zone If Invalid Value Is Provided For Cidr.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='234234234234abcd#$@#$',
                metric=12,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
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
                get_error_message(e) | should.start_with('must match \"([0-9]{1,3}\\.){3}[0-9]{1,3}\\/[0-9]{1,3}\"')
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
