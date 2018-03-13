# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audience_Match.

* TC-45290 - Audience_Match POST:

  Verify user is unable to get results with blank parameters using request POST /audienceMatch.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audienceMatch"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audienceMatch"

JSON data sent to PathFinder in this test:

  {'headers': [{'name': 'string', 'value': 'string'}],
   'query': [{'name': 'string', 'value': 'string'}],
   'remoteAddress': 'string',
   'remoteHost': 'string',
   'serverHost': 'string',
   'serverPort': 0,
   'tags': [{'name': 'string', 'value': 'string'}]}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Audience_Match')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Audience_Match test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-45290')
    @pytest.mark.Audience_Match
    @pytest.mark.POST
    def test_TC_45290_POST_Audience_Match_Unable_To_Get_With_Blank_Parameters(self, context):
        """TC-45290 - Audience_Match-POST
           Verify user is unable to get results with blank parameters using request POST /audienceMatch."""
        # Define a test step

        with pytest.allure.step("""Verify user is unable to get results with blank parameters using request POST /audienceMatch."""):

            # Test case configuration
            networkContextDetails = context.sc.NetworkContextDetails(
                alternateHost='string',
                headers=[{
                    'name': 'string',
                    'value': 'string'
                }],
                query=[{
                    'name': 'string',
                    'value': 'string'
                }],
                remoteAddress='string',
                remoteHost='string',
                scheme='string',
                serverHost='string',
                serverPort=0,
                tags=[{
                    'name': 'string',
                    'value': 'string'
                }])


            # prepare the request, so we can modify it
            request = context.cl.Audience_Match.audienceMatchPost(
                    body=networkContextDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # audienceMatchPost the Audience_Match, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Invalid IP')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
