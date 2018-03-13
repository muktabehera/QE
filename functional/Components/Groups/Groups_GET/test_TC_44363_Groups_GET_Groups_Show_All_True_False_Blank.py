# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-44363 - Groups GET:

  Verify that user is able to GET the details of groups using request GET /groups with parameters 'Showall' as true/false/blank.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups?showAll=true"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups?showAll=true"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Groups')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Groups test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44363')
    @pytest.mark.Groups
    @pytest.mark.GET
    def test_TC_44363_GET_Groups_Groups_Show_All_True(self, context):
        """TC-44363 - Groups-GET
           Verify that user is able to GET the details of groups using request GET /groups with parameters 'Showall' as true/false/blank."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is able to GET the details of groups using request GET /groups with parameters 'Showall' as true."""):

            # getEntity the Groups.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Groups.listEntities(
                    showAll='true')
            )

        # Define a test step
        with pytest.allure.step("""Test2: Verify that user is able to GET the details of groups using request GET /groups with parameters 'Showall' as false."""):

            # getEntity the Groups.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Groups.listEntities(
                    showAll='false')
            )

        # Define a test step
        with pytest.allure.step("""Test3: Verify that user is able to GET the details of groups using request GET /groups with parameters 'Showall' as blank."""):

                # getEntity the Groups.
                # The `check` call validates return code
                # and some of the swagger schema.
                # Most schema checks are disabled.
                check(
                    context.cl.Groups.listEntities()
                )