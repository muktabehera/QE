# -*- coding: UTF-8 -*-

"""PFE Component Tests - Origins.

* TC-44073 - Origins GET:

  Verify that user is able to GET the details of origins using request GET /origins with parameters 'Showall' as true/false/blank.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins?showAll=true"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins?showAll=true"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Origins')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Origins test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44073')
    @pytest.mark.Origins
    @pytest.mark.GET
    def test_TC_44073_GET_Origins_Origins_Showall_True(self, context):
        """TC-44073 - Origins-GET
           Verify that user is able to GET the details of origins using request GET /origins with parameters 'Showall' as true/false/blank."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is able to GET the details of origins using request GET /origins with parameters 'Showall' as true."""):

            # listEntities the Origins.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Origins.listEntities(
                    showAll='true')
            )

        # Define a test step
        with pytest.allure.step("""Test2: Verify that user is able to GET the details of origins using request GET /origins with parameters 'Showall' as false."""):

            # listEntities the Origins.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Origins.listEntities(
                    showAll='false')
            )

        # Define a test step
        with pytest.allure.step("""Test3: Verify that user is able to GET the details of origins using request GET /origins with parameters 'Showall' as blank."""):

            # listEntities the Origins.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Origins.listEntities()
            )