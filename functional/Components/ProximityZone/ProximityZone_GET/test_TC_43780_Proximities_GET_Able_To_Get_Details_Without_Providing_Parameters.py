"""PFE Component Tests - Proximity_Zones.
# coding: utf-8
* TC-43780 - Proximity_Zones GET:

  Verify that user is able to GET the details of  proximities using request “/proximities “ without providing any parameters with “Showall=false(default)”. .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities?showAll=false"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities?showAll=false"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Proximity_Zones')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Proximity_Zones test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43780')
    @pytest.mark.Proximity_Zones
    @pytest.mark.GET
    def test_TC_43780_GET_Proximity_Zones_Able_To_Get_Details_Without_Providing_Parameters(self, context):
        """TC-43780 - Proximity_Zones-GET
           Verify that user is able to GET the details of  proximities using request “/proximities “ without providing any parameters with “Showall=false(default)”. ."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of  proximities using request “/proximities “ without providing any parameters with “Showall=false(default)”. ."""):

            ### Positive test example

            # listEntities the Proximity_Zones.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Proximity_Zones.listEntities(
                    showAll='false')
            )

