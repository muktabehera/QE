# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-43318 - Proximity_Zones POST:

  Verify that user is able to modify client rule with parameter 'Server Port>GT(Greater Than)' using request PATCH '/clients/'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': True,
   'configurations': [],
   'id': 'proximityAutoUpdate',
   'name': 'ProximityAutoUpdate',
   'proximityDetails': [{'cidr': '0.0.0.0/0', 'metric': 1, 'notes': 'a'}],
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Proximity_Zones')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Proximity_Zones test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43318')
    @pytest.mark.Proximity_Zones
    @pytest.mark.POST
    def test_TC_43318_POST_Proximity_Zones_Server_Port_Gt(self, context):
        """TC-43318 - Proximity_Zones-POST
           Verify that user is able to modify client rule with parameter 'Server Port>GT(Greater Than)' using request PATCH '/clients/'."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create Proximity Zone using request POST '/Proximity_Zones/'."""):


            # Test case configuration
            proximityZoneDetails = context.sc.ProximityZoneDetails(
                configAdminCanEdit=True,
                configurations=[],
                id='proximityAutoUpdate',
                name='ProximityAutoUpdate',
                proximityDetails=[{
                    'cidr': '0.0.0.0/0',
                    'metric': 1,
                    'notes': 'a'
                }],
                visibleInAllConfigurations=True)


            # createEntity the Proximity_Zones.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Proximity_Zones.createEntity(
                    body=proximityZoneDetails
                )
            )

