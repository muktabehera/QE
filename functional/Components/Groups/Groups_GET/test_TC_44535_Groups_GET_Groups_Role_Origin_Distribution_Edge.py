# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-44535 - Groups GET:

  Verify that user is able to GET the details of groups on providing values(Origin, Distribution, Edge) in Role parameter  using request GET /groups.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups?role=origin &showAll=false"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups?role=origin &showAll=false"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Groups')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Groups test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44535')
    @pytest.mark.Groups
    @pytest.mark.GET
    def test_TC_44535_GET_Groups_Groups_Role_Origin(self, context):
        """TC-44535 - Groups-GET
           Verify that user is able to GET the details of groups on providing values(Origin, Distribution, Edge) in Role parameter  using request GET /groups."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is able to GET the details of groups on providing values(Origin) in Role parameter  using request GET /groups."""):

            # getEntity the Groups.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Groups.listEntities(
                    role='origin', 
                    showAll='false'
                )
            )

        # Define a test step
        with pytest.allure.step("""Test2: Verify that user is able to GET the details of groups on providing values(Distribution) in Role parameter  using request GET /groups."""):

            # getEntity the Groups.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Groups.listEntities(
                    role='distribution',
                    showAll='false'
                )
            )

        # Define a test step
        with pytest.allure.step("""Test3: Verify that user is able to GET the details of groups on providing values(Edge) in Role parameter  using request GET /groups."""):

            # getEntity the Groups.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Groups.listEntities(
                    role='edge',
                    showAll='false'
                )
            )