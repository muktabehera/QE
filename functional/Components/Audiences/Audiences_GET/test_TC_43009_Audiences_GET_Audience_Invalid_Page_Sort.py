# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audiences.

* TC-43009 - Audiences GET:

  Verify that user is unable to GET the details of Audience request /audiences  with invalid values in  page and sort parameter .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences?page=sdadadad"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences?page=sdadadad"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Audiences')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Audiences test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43009')
    @pytest.mark.Audiences
    @pytest.mark.GET
    def test_TC_43009_GET_Audiences_Audience_Invalid_Page(self, context):
        """TC-43009 - Audiences-GET
           Verify that user is unable to GET the details of Audience request /audiences  with invalid values in  page and sort parameter ."""
        # Define a test step


        with pytest.allure.step("""Test1: Verify that user is unable to GET the details of Audience request /audiences  with invalid values in  page parameter ."""):


            # listEntities the Audiences, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Audiences.listEntities(
                        page='sdadadad'),
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


        # Define a test step
        with pytest.allure.step("""Test2: Verify that user is unable to GET the details of Audience request /audiences  with invalid values in sort parameter ."""):

            # listEntities the Audiences, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Audiences.listEntities(
                        sort='sdfsfs'),
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Invalid sort parameter specified. No seperator')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))