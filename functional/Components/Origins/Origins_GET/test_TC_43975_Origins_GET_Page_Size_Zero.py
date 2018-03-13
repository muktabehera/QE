# -*- coding: UTF-8 -*-

"""PFE Component Tests - Origins.

* TC-43975 - Origins GET:

  Verify that 20 records is displayed on providing 'page-size' value as 0 for 'page' parameter using request GET /origins.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins?page=1;0 &showAll=false"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins?page=1;0 &showAll=false"

"""

import pytest

from qe_common import *

logger = init_logger()

@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Origins')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Origins test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43975')
    @pytest.mark.Origins
    @pytest.mark.GET
    def test_TC_43975_GET_Origins_Page_Size_Zero(self, context):
        """TC-43975 - Origins-GET
           Verify that 20 records is displayed on providing 'page-size' value as 0 for 'page' parameter using request GET /origins."""
        # Define a test step
        with pytest.allure.step("""Verify that 20 records is displayed on providing 'page-size' value as 0 for 'page' parameter using request GET /origins."""):

            # listEntities the Origins.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Origins.listEntities(
                    page='1;0', 
                    showAll='false'
                )
            )

