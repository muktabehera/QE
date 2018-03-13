# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audience_Match.

* TC-45093 - Audience_Match POST:

  Verify the user is able to get the results for audience match by remoteAddress parameter using request POST /audienceMatch.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audienceMatch"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audienceMatch"

JSON data sent to PathFinder in this test:

  {'alternateHost': 'string',
   'headers': [{'name': 'string', 'value': 'string'}],
   'query': [{'name': 'string', 'value': 'string'}],
   'remoteAddress': '192.16.17.193',
   'remoteHost': 'string',
   'scheme': 'string',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-45093')
    @pytest.mark.Audience_Match
    @pytest.mark.POST
    def test_TC_45093_POST_Audience_Match_Able_To_Get_Results_By_Passing_Valid_Remote_Address(self, context):
        """TC-45093 - Audience_Match-POST
           Verify the user is able to get the results for audience match by remoteAddress parameter using request POST /audienceMatch."""
        # Define a test step
        with pytest.allure.step("""Verify the user is able to get the results for audience match by remoteAddress parameter using request POST /audienceMatch."""):

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
                remoteAddress='192.16.17.193',
                remoteHost='string',
                scheme='string',
                serverHost='string',
                serverPort=0,
                tags=[{
                    'name': 'string',
                    'value': 'string'
                }])


            # audienceMatchPost the Audience_Match.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Audience_Match.audienceMatchPost(
                    body=networkContextDetails
                )
            )

