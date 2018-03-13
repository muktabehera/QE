# -*- coding: UTF-8 -*-

"""PFE Component Tests - ProximityZone.

* TC-43827 - ProximityZone POST:

  Multiple Ranges Configurations.


Equivalent test JSON payload:

{'configAdminCanEdit': False,
 'configurations': [{'id': 'default'}, {'id': 'QA_Test'}],
 'id': 'ProximityPostMultpleConfigRanges',
 'name': 'ProximityPostMultpleConfigRanges',
 'proximityDetails': [{'cidr': '1.0.0.0/8', 'metric': 0, 'notes': '1'},
                      {'cidr': '1.1.0.0/16', 'metric': 1, 'notes': '2'},
                      {'cidr': '2.2.2.0/24', 'metric': 2, 'notes': '3'},
                      {'cidr': '3.3.3.0/32', 'metric': 3, 'notes': '4'},
                      {'cidr': '1.0.0.0/8', 'metric': 4, 'notes': '5'},
                      {'cidr': '1.0.0.0/8', 'metric': 5, 'notes': '6'},
                      {'cidr': '1.0.0.0/8', 'metric': 6, 'notes': '7'},
                      {'cidr': '7.0.0.0/8', 'metric': 7, 'notes': '8'},
                      {'cidr': '8.0.0.0/8', 'metric': 8, 'notes': '9'},
                      {'cidr': '9.0.0.0/8', 'metric': 9, 'notes': '10'}],
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43827')
    @pytest.mark.ProximityZone
    @pytest.mark.POST
    def test_TC_43827_POST_ProximityZone_Multiple_Ranges_Configurations(self, context):
        """TC-43827 - ProximityZone-POST - Multiple Ranges Configurations"""
        # Define a test step
        with pytest.allure.step('Multiple Ranges Configurations.'):
            proximityDetailsList = list()
            proximityDetailsList.append(context.sc.ProximityDetails(
                cidr='1.0.0.0/8', metric=0, notes='1'))
            proximityDetailsList.append(context.sc.ProximityDetails(
                cidr='1.1.0.0/16', metric=1, notes='2'))
            proximityDetailsList.append(context.sc.ProximityDetails(
                cidr='2.2.2.0/24', metric=2, notes='3'))
            proximityDetailsList.append(context.sc.ProximityDetails(
                cidr='3.3.3.0/32', metric=3, notes='4'))
            proximityDetailsList.append(context.sc.ProximityDetails(
                cidr='1.0.0.0/8', metric=4, notes='5'))
            proximityDetailsList.append(context.sc.ProximityDetails(
                cidr='1.0.0.0/8', metric=5, notes='6'))
            proximityDetailsList.append(context.sc.ProximityDetails(
                cidr='1.0.0.0/8', metric=6, notes='7'))
            proximityDetailsList.append(context.sc.ProximityDetails(
                cidr='7.0.0.0/8', metric=7, notes='8'))
            proximityDetailsList.append(context.sc.ProximityDetails(
                cidr='8.0.0.0/8', metric=8, notes='9'))
            proximityDetailsList.append(context.sc.ProximityDetails(
                cidr='9.0.0.0/8', metric=9, notes='10'))
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=False,
                configAdminCanEdit=False,
                configurations=[
                    context.status['globals']['configId'],
                    context.status['globals']['tenantConfigId']
                ],
                id='ProximityPostMultpleConfigRanges',
                name='ProximityPostMultpleConfigRanges',
                proximityDetails=proximityDetailsList)
            # POST the ProximityZone.
            # The `check` call validates return code and some of the swagger schema
            # (most schema checks are disabled)
            check(
                context.cl.Proximity_Zones.createEntity(
                    body=proximityZone
                )
            )
