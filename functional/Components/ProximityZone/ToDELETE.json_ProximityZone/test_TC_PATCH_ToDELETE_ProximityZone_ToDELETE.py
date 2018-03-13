# -*- coding: UTF-8 -*-

"""PFE Component Tests - ToDELETE.json.

* TC-PATCH - ToDELETE.json ProximityZone:

  .


Equivalent test JSON payload:

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


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('ToDELETE')
@pytest.allure.feature('ProximityZone')
class Test_PFE_Components(object):
    """PFE ToDELETE.json test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-PATCH')
    @pytest.mark.ToDELETE
    @pytest.mark.ProximityZone
    def test_TC_PATCH_ProximityZone_ToDELETE(self, context):
        """TC-PATCH - ToDELETE.json-ProximityZone - """
        # Define a test step
        with pytest.allure.step('.'):
            proximityDetails = context.sc.ProximityDetails(
                cidr='19.0.0.0/8',
                metric=1,
                notes='')
            proximityZone = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=False,
                configurations=[],
                id='ProximityDELETE',
                name='ProximityDELETE',
                proximityDetails=[proximityDetails])

            # prepare the request, so we can modify it
            request = context.cl.Proximity_Zones.ProximityZone(
                body=proximityZone
            )

            ### Invalid Json Error injection example
            ### Errors that result in valid Json can be set above.

            # Get the generated payload and corrupt the metric
            request.future.request.data = request.future.request.data.replace(
                '"metric": 1,', '"metric":,'
            )

            ### Positive test example

            # ProximityZone the ToDELETE.json.
            # The `check` call validates return code and some of the swagger schema
            # (most schema checks are disabled)
            check(
                context.cl.Proximity_Zones.createEntity(
                    body=proximityZone
                )
            )

            ### Negative test example

            # ProximityZone the ToDELETE.json, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Proximity_Zones.ProximityZone(body=proximityZone),
                    quiet=True, returnResponse=True)
            except HTTPBadRequest as e:         # 400 error
                get_error_message(e) | expect.any(
                    should.start_with('may not be empty'),
                    should.start_with('Invalid identifier'),
                    should.contain('length must be between 1 and 100')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
