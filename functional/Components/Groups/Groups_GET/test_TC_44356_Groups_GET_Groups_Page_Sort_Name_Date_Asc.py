# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-44356 - Groups GET:

  Verify that user is able to GET the details of groups using request GET /groups with parameters page,sort=name;asc.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups?page=0;3 &sort=name;asc
       &showAll=false"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups?page=0;3 &sort=name;asc
       &showAll=false"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Groups')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Groups test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44356')
    @pytest.mark.Groups
    @pytest.mark.GET
    def test_TC_44356_GET_Groups_Groups_Page_Sort_Name_Asc(self, context):
        """TC-44356 - Groups-GET
           Verify that user is able to GET the details of groups using request GET /groups with parameters page,sort=name;asc."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is able to GET the details of groups using request GET /groups with parameters page,sort=name;asc."""):

            # getEntity the Groups.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Groups.listEntities(
                    page='0;3', 
                    sort='name;asc', 
                    showAll='false'
                )
            )

        # Define a test step
        with pytest.allure.step("""Test2: Verify that user is able to GET the details of groups using request GET /groups with parameters page,sort=Date;asc."""):


            # getEntity the Groups.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Groups.listEntities(
                    page='0;3',
                    sort='creationDate;asc',
                    showAll='false'
                )
            )