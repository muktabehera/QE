# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-44362 - Groups GET:

  Verify that 20 records is displayed on providing 'page-size' value as 0 for 'page' parameter using request GET /groups.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups?page=1;0 &showAll=false"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups?page=1;0 &showAll=false"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Groups')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Groups test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44362')
    @pytest.mark.Groups
    @pytest.mark.GET
    def test_TC_44362_GET_Groups_Pagesize_Zero(self, context):
        """TC-44362 - Groups-GET
           Verify that 20 records is displayed on providing 'page-size' value as 0 for 'page' parameter using request GET /groups."""
        # Define a test step
        with pytest.allure.step("""Verify that 20 records is displayed on providing 'page-size' value as 0 for 'page' parameter using request GET /groups."""):

            # getEntity the Groups.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Groups.getEntity(
                    page='1;0', 
                    showAll='false'
                )
            )
