# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audiences.

* TC-43008 - Audiences GET:

  Verify that user is able to GET the details of Audience request /audiences  with page,sort and prefix parameter .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences?page=0;3 &sort=name;asc
       &prefix=a"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences?page=0;3 &sort=name;asc
       &prefix=a"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Audiences')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Audiences test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43008')
    @pytest.mark.Audiences
    @pytest.mark.GET
    def test_TC_43008_GET_Audiences_Page_Sort_Prefix(self, context):
        """TC-43008 - Audiences-GET
           Verify that user is able to GET the details of Audience request /audiences  with page,sort and prefix parameter ."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of Audience request /audiences  with page,sort and prefix parameter ."""):

            # listEntities the Audiences.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Audiences.listEntities(
                    page='0;3', 
                    sort='name;asc', 
                    prefix='a'
                )
            )

