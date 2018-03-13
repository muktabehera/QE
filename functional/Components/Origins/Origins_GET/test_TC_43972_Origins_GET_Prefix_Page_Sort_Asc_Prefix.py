# -*- coding: UTF-8 -*-

"""PFE Component Tests - Origins.

* TC-43972 - Origins GET:

  Verify that user is able to GET the details of origins using request GET /origins with parameters page,sort=name;asc and prefix.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins?page=0;3 &sort=name;asc
       &prefix=o &showAll=false"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins?page=0;3 &sort=name;asc
       &prefix=o &showAll=false"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Origins')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Origins test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43972')
    @pytest.mark.Origins
    @pytest.mark.GET
    def test_TC_43972_GET_Origins_Prefix_Page_Sort_Asc_Prefix(self, context):
        """TC-43972 - Origins-GET
           Verify that user is able to GET the details of origins using request GET /origins with parameters page,sort=name;asc and prefix."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is able to GET the details of origins using request GET /origins with parameters page,sort=name;asc and prefix."""):

            # listEntities the Origins.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Origins.listEntities(
                    page='0;3', 
                    sort='name;asc', 
                    prefix='o', 
                    showAll='false'
                )
            )

        # Define a test step
        with pytest.allure.step("""Test2: Verify that user is able to GET the details of origins using request GET /origins with parameters page,sort=name;asc and prefix."""):

            # listEntities the Origins.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Origins.listEntities(
                    page='0;3',
                    sort='creationDate;asc',
                    prefix='o',
                    showAll='false'
                )
            )