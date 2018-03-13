# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-43842 - Proximity_Zones POST:

  Verify that user is able to delete the Proximity Zone using request DELETE /proximities{id}  with 'id' parameter.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': False,
   'configurations': [],
   'id': 'ProximityDELETE',
   'name': 'ProximityDELETE',
   'proximityDetails': [{'cidr': '19.0.0.0/8', 'metric': 1, 'notes': ''}],
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43842')
    @pytest.mark.Proximity_Zones
    @pytest.mark.POST
    def test_TC_43842_POST_Proximity_Zones_Able_To_Delete_Proximity_Zone(self, context):
        """TC-43842 - Proximity_Zones-POST
           Verify that user is able to delete the Proximity Zone using request DELETE /proximities{id}  with 'id' parameter."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to delete the Proximity Zone using request DELETE /proximities{id}  with 'id' parameter."""):

            ### Positive test example

            # Test case configuration
            proximityZoneDetails = context.sc.ProximityZoneDetails(
                configAdminCanEdit=False,
                configurations=[],
                id='ProximityDELETE',
                name='ProximityDELETE',
                proximityDetails=[{
                    'cidr': '19.0.0.0/8',
                    'metric': 1,
                    'notes': ''
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

            ### Delete the proximityzome created above

            check(
                context.cl.Proximity_Zones.deleteEntity(id='ProximityDELETE')
            )