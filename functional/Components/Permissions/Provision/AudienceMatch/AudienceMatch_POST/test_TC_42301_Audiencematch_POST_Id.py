# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audience_Match.

* TC-42301 - Audience_Match POST:

  Verify that User is unable to Create/Edit/View/Delete, any entity on any page of the QED, using token with "Provision" permission within the token expiration time.


Equivalent test CURL command:

  curl -k -H "Host: <client_host>" -H "Authorization: Bearer
       <valid_token>" -X POST -d @<JSON_data_file> -H "Content-Type:
       application/json" "<PF_host>://<client_host>/audienceMatch"

Same, with test data:

  curl -k -H "Host: <client_host>" -H "Authorization: Bearer
       <valid_token>" -X POST -d @<JSON_data_file> -H "Content-Type:
       application/json" "<PF_host>://<client_host>/audienceMatch"

JSON data sent to PathFinder in this test:

  {'headers': [{'name': 'string', 'value': 'string'}],
   'query': [{'name': 'string', 'value': 'string'}],
   'remoteAddress': '192.0.0.0',
   'remoteHost': 'string',
   'serverHost': 'string',
   'serverPort': 0,
   'tags': [{'name': 'string', 'value': 'string'}]}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Audience_Match')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Audience_Match test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42301')
    @pytest.mark.Audience_Match
    @pytest.mark.POST
    def test_TC_42301_POST_Audience_Match_Id(self, context):
        """TC-42301 - Audience_Match-POST
           Verify that User is unable to Create/Edit/View/Delete, any entity on any page of the QED, using token with "Provision" permission within the token expiration time."""
        # Define a test step
        with pytest.allure.step("""Verify that User is unable to Create/Edit/View/Delete, any entity on any page of the QED, using token with "Provision" permission within the token expiration time."""):

            ### Positive test example

            # Test case configuration
            networkContextDetails = context.sc.NetworkContextDetails(
                alternateHost=None,
                headers=[{
                    'name': 'string',
                    'value': 'string'
                }],
                query=[{
                    'name': 'string',
                    'value': 'string'
                }],
                remoteAddress='192.0.0.0',
                remoteHost='string',
                scheme=None,
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

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that User is unable to Create/Edit/View/Delete, any entity on any page of the QED, using token with "Provision" permission within the token expiration time."""):

            ### Negative test example

            # Test case configuration
            networkContextDetails = context.sc.NetworkContextDetails(
                alternateHost=None,
                headers=[{
                    'name': 'string',
                    'value': 'string'
                }],
                query=[{
                    'name': 'string',
                    'value': 'string'
                }],
                remoteAddress='192.0.0.0',
                remoteHost='string',
                scheme=None,
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
                    should.start_with('may not be empty'),
                    should.start_with('Invalid page parameter specified'),
                    should.contain('Invalid Authorization Token')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
