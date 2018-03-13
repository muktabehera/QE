# -*- coding: UTF-8 -*-

"""PFE Component Tests - Proximity_Zones.

* TC-43847 - Proximity_Zones PATCH:

  Verify that user is unable to Modify[name] starting with Numeric/special character for Proximity Zone using request PATCH /proximities{id} " .


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
   'name': '@31_/><',
   'proximityDetails': [{'cidr': '0.0.0.0/0', 'metric': 1, 'notes': ''}],
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43847')
    @pytest.mark.Proximity_Zones
    @pytest.mark.PATCH
    def test_TC_43847_PATCH_Proximity_Zones_Unable_Modify_Name_Starting_With_Numeric_Or_Special_Character(self, context):
        """TC-43847 - Proximity_Zones-PATCH
           Verify that user is unable to Modify[name] starting with Numeric/special character for Proximity Zone using request PATCH /proximities{id} " ."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to Modify[name] starting with Numeric/special character for Proximity Zone using request PATCH /proximities{id} " ."""):

            # Test case configuration
            proximityZoneDetails = context.sc.ProximityZoneDetails(
                configAdminCanEdit=False,
                configurations=[],
                id=None,
                name='@31_/><',
                proximityDetails=[{
                    'cidr': '0.0.0.0/0',
                    'metric': 1,
                    'notes': ''
                }],
                visibleInAllConfigurations=True)


            # updateEntity the Proximity_Zones.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            request = context.cl.Proximity_Zones.updateEntity(
                    id='ProximityPost1',
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
                    should.start_with('Invalid name, the pattern must match \"^[\\p{IsAlphabetic}\\p{IsDigit}]+[\\p{Blank}\\p{IsAlphabetic}\\p{IsDigit}[\\p{Punct}&&[^/\\<>\\|\\^]]]*$\"'),
                    should.start_with('Invalid configuration identifier'),
                    should.start_with('must match \"([0-9]{1,3}\\.){3}[0-9]{1,3}\\/[0-9]{1,3}\"')

                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
