# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-43868 - Proximity_Zones PATCH:

  Verify that user is able to Modify [Add Multiple Ranges] in Proximity Zone using request PATCH /proximities{id} ".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/ProximityUpdate"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/ProximityUpdate"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': False,
   'configurations': [{'host': '172.30.2.149', 'id': 'default'}],
   'name': 'ProximityUpdatedMultipeRanges',
   'proximityDetails': [{'cidr': '0.0.0.0/0', 'metric': 1, 'notes': ''},
                        {'cidr': '0.0.0.0/0', 'metric': 2, 'notes': 'Notes1'},
                        {'cidr': '0.0.0.0/0', 'metric': 3, 'notes': 'Notes13'},
                        {'cidr': '0.0.0.0/0',
                         'metric': 42,
                         'notes': 'Notes13123'},
                        {'cidr': '0.0.0.0/0',
                         'metric': 43,
                         'notes': 'Notes13123'},
                        {'cidr': '0.0.0.0/0',
                         'metric': 44,
                         'notes': 'Notes13123'},
                        {'cidr': '0.0.0.0/0',
                         'metric': 45,
                         'notes': 'Notes13123'},
                        {'cidr': '0.0.0.0/0',
                         'metric': 46,
                         'notes': 'Notes13123'},
                        {'cidr': '0.0.0.0/0',
                         'metric': 47,
                         'notes': 'Notes13123'},
                        {'cidr': '0.0.0.0/0',
                         'metric': 48,
                         'notes': 'Notes13123'}],
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()







@pytest.mark.components
@pytest.allure.story('Proximity_Zones')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Proximity_Zones test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43868')
    @pytest.mark.Proximity_Zones
    @pytest.mark.PATCH
    def test_TC_43868_PATCH_Proximity_Zones_Able_To_Update_Add_Multiple_Ranges(self, context):
        """TC-43868 - Proximity_Zones-PATCH
           Verify that user is able to Modify [Add Multiple Ranges] in Proximity Zone using request PATCH /proximities{id} "."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to Modify [Add Multiple Ranges] in Proximity Zone using request PATCH /proximities{id} "."""):

            # Test case configuration
            proximityZoneDetails = context.sc.ProximityZoneDetails(
                configAdminCanEdit=False,
                configurations=[{
                    'id': 'default',
                    'host': '172.30.6.174'
                }],
                id=None,
                name='ProximityUpdatedMultipeRanges',
                proximityDetails=[{
                    'cidr': '0.0.0.0/0',
                    'metric': 1,
                    'notes': ''
                }, {
                    'cidr': '0.0.0.0/0',
                    'metric': 2,
                    'notes': 'Notes1'
                }, {
                    'cidr': '0.0.0.0/0',
                    'metric': 3,
                    'notes': 'Notes13'
                }, {
                    'cidr': '0.0.0.0/0',
                    'metric': 42,
                    'notes': 'Notes13123'
                }, {
                    'cidr': '0.0.0.0/0',
                    'metric': 43,
                    'notes': 'Notes13123'
                }, {
                    'cidr': '0.0.0.0/0',
                    'metric': 44,
                    'notes': 'Notes13123'
                }, {
                    'cidr': '0.0.0.0/0',
                    'metric': 45,
                    'notes': 'Notes13123'
                }, {
                    'cidr': '0.0.0.0/0',
                    'metric': 46,
                    'notes': 'Notes13123'
                }, {
                    'cidr': '0.0.0.0/0',
                    'metric': 47,
                    'notes': 'Notes13123'
                }, {
                    'cidr': '0.0.0.0/0',
                    'metric': 48,
                    'notes': 'Notes13123'
                }],
                visibleInAllConfigurations=True)


            # updateEntity the Proximity_Zones.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Proximity_Zones.updateEntity(
                    id='ProximityPosttest',
                    body=proximityZoneDetails
                )
            )

