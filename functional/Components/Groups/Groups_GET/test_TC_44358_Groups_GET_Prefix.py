# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-44358 - Groups GET:

  Verify that user is able to GET the details of groups using request GET /groups with parameter prefix.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups?prefix=G &showAll=false"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups?prefix=G &showAll=false"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Groups')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Groups test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44358')
    @pytest.mark.Groups
    @pytest.mark.GET
    def test_TC_44358_GET_Groups_Prefix(self, context):
        """TC-44358 - Groups-GET
           Verify that user is able to GET the details of groups using request GET /groups with parameter prefix."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of groups using request GET /groups with parameter prefix."""):

            # getEntity the Groups.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Groups.listEntities(
                    prefix='G', 
                    showAll='false'
                )
            )
