# -*- coding: UTF-8 -*-

"""PFE Component Tests - Origins.

* TC-43974 - Origins GET:

  Verify that error message is displayed on providing invalid value for page,sort parameter using request GET /origins.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins?page=pagee &sort=sortt
       &showAll=false"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins?page=pagee &sort=sortt
       &showAll=false"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Origins')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Origins test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43974')
    @pytest.mark.Origins
    @pytest.mark.GET
    def test_TC_43974_GET_Origins_Page_Sort_Invalid(self, context):
        """TC-43974 - Origins-GET
           Verify that error message is displayed on providing invalid value for page,sort parameter using request GET /origins."""
        # Define a test step
        with pytest.allure.step("""Verify that error message is displayed on providing invalid value for page,sort parameter using request GET /origins."""):

            # listEntities the Origins, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Origins.listEntities(
                        page='pagee', 
                        sort='sortt', 
                        showAll='false'
                    ),
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Invalid page parameter specified. No seperator')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
