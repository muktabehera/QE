# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-43793 - Proximity_Zones GET:

  Verify that user is able to GET the details of  proximities having id with 100 characters using request /proximities/{id}.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/abcdefghijkl12345678abcdefghijkl12345678abcdefghijkl12345678abcdefghijkl12345678abcdefghijkl23456678"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities/abcdefghijkl12345678abcdefghijkl12345678abcdefghijkl12345678abcdefghijkl12345678abcdefghijkl23456678"

"""

import pytest

from qe_common import *

logger = init_logger()







@pytest.mark.components
@pytest.allure.story('Proximity_Zones')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Proximity_Zones test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43793')
    @pytest.mark.Proximity_Zones
    @pytest.mark.GET
    def test_TC_43793_GET_Proximity_Zones_Able_To_Get_Details_Having_Id_With_100_Characters(self, context):
        """TC-43793 - Proximity_Zones-GET
           Verify that user is able to GET the details of  proximities having id with 100 characters using request /proximities/{id}."""
        # Define a test step
        with pytest.allure.step('First Create Proximity Zone having id with 100 characters.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=1,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=False,
                configurations=[],
                id='qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiop',
                name='idwith100characters',
                proximityDetails=[proximityDetails])
            # POST the ProximityZone.
            # The `check` call validates return code and some of the swagger schema
            # (most schema checks are disabled)
            check(
                context.cl.Proximity_Zones.createEntity(
                    body=proximityZone
                )
            )


        with pytest.allure.step("""Verify that user is able to GET the details of  proximities having id with 100 characters using request /proximities/{id}."""):

            # listEntities the Proximity_Zones, having id with 100 characters
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Proximity_Zones.getEntity(
                id='qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiop')
            )
