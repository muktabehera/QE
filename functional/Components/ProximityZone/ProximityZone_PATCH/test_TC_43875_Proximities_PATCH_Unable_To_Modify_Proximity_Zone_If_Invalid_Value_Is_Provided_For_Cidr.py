# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-43875 - Proximity_Zones PATCH:

  Verify that user is unable to Modify[CIDR] with invalid value for Proximity Zone using request PATCH /proximities{id} " .


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
   'configurations': [],
   'name': 'InvalidCidrValue',
   'proximityDetails': [{'cidr': '234234234234abcd#$@#$',
                         'metric': 12,
                         'notes': ''}],
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43875')
    @pytest.mark.Proximity_Zones
    @pytest.mark.PATCH
    def test_TC_43875_PATCH_Proximity_Zones_Unable_To_Modify_Proximity_Zone_If_Invalid_Value_Is_Provided_For_Cidr(self, context):
        """TC-43875 - Proximity_Zones-PATCH
           Verify that user is unable to Modify[CIDR] with invalid value for Proximity Zone using request PATCH /proximities{id} " ."""
        # Define a test step
        with pytest.allure.step("Verify that user is unable to POST[CIDR] with invalid value for Proximity Zone using request POST"):

            # Test case configuration
            proximityZoneDetails = context.sc.ProximityZoneDetails(
                configAdminCanEdit=False,
                configurations=[],
                id='InvalidCidrValue',
                name='InvalidCidrValue',
                proximityDetails=[{
                    'cidr': '234234234234abcd#$@#$',
                    'metric': 12,
                    'notes': 'invalid cidr'
                }],
                visibleInAllConfigurations=True)

            # prepare the request, so we can create it
            request = context.cl.Proximity_Zones.createEntity(
                body=proximityZoneDetails
            )

            # createEntity the Proximity_Zones, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('must match \"([0-9]{1,3}\\.){3}[0-9]{1,3}\\/[0-9]{1,3}\"'),
                    should.start_with('Invalid configuration identifier')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))

        with pytest.allure.step("""Verify that user is unable to Modify[CIDR] with invalid value for Proximity Zone using request PATCH /proximities{id} " ."""):

            # Test case configuration
            proximityZoneDetails = context.sc.ProximityZoneDetails(
                configAdminCanEdit=False,
                configurations=[],
                id=None,
                name='InvalidCidrValue',
                proximityDetails=[{
                    'cidr': '234234234234abcd#$@#$',
                    'metric': 12,
                    'notes': ''
                }],
                visibleInAllConfigurations=True)


            # prepare the request, so we can modify it
            request = context.cl.Proximity_Zones.updateEntity(
                    id='ProximityUpdate',
                    body=proximityZoneDetails
            )


            # updateEntity the Proximity_Zones, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('must match \"([0-9]{1,3}\\.){3}[0-9]{1,3}\\/[0-9]{1,3}\"'),
                    should.start_with('Invalid configuration identifier')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
