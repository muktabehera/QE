# -*- coding: UTF-8 -*-

"""PFE Component Tests - Origins.

* TC-43979 - Origins GET:

  Verify that user is able to get the details of origins 'BaseUris'  on providing 'Id' parameter using request GET /origins{id}.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins/originFTP"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins/originFTP"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Origins')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Origins test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43979')
    @pytest.mark.Origins
    @pytest.mark.GET
    def test_TC_43979_GET_Origins_Base_Uri(self, context):
        """TC-43979 - Origins-GET
           Verify that user is able to get the details of origins 'BaseUris'  on providing 'Id' parameter using request GET /origins{id}."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to get the details of origins 'BaseUris'  on providing 'Id' parameter using request GET /origins{id}."""):

            # listEntities the Origins.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Origins.getEntity(
                    id='originGet'
                )
            )

