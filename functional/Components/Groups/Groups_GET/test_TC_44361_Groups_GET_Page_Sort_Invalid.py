# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-44361 - Groups GET:

  Verify that error message is displayed on providing invalid value for page,sort parameter using request GET /groups.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups?page=pageee &sort=sorttt
       &showAll=false"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups?page=pageee &sort=sorttt
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44361')
    @pytest.mark.Groups
    @pytest.mark.GET
    def test_TC_44361_GET_Groups_Page_Sort_Invalid(self, context):
        """TC-44361 - Groups-GET
           Verify that error message is displayed on providing invalid value for page,sort parameter using request GET /groups."""
        # Define a test step
        with pytest.allure.step("""Verify that error message is displayed on providing invalid value for page,sort parameter using request GET /groups."""):

            # getEntity the Groups, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Groups.listEntities(
                        page='pageee', 
                        sort='sorttt', 
                        showAll='false'
                    ),
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Invalid page parameter specified'),
                    should.contain('No seperator')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
