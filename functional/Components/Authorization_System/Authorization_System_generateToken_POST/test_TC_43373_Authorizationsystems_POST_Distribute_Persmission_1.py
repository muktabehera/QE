# -*- coding: UTF-8 -*-

"""PFE Component Tests - Authorization_Systems.

* TC-43373 - Authorization_Systems POST:

  Verify that user is able to generate Token with permission [Distribute] while same is selected in the Authorization system using request POST /authorizationSystems/{id}/generateToken  ".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/authorizationSystems/<data_ID1_under_test>/generateToken"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/authorizationSystems/ab.qumu.com/generateToken"

JSON data sent to PathFinder in this test:

  {'audience': 'qed:a1',
   'expirationTime': '2017-09-30T06:10:50.714Z',
   'generatedToken': 'string',
   'issueTime': '2016-01-29T06:10:50.714Z',
   'macKey': '123456789012345678901234567890121',
   'notBeforeTime': '2017-09-30T06:10:50.714Z',
   'permissions': ['MANAGE_SYSTEM', 'MANAGE_CONFIGURATION'],
   'qeda': {},
   'qedp': {},
   'subject': 'AU3',
   'url': '',
   'useCompactPermissions': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Authorization_Systems')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Authorization_Systems test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43373')
    @pytest.mark.Authorization_Systems
    @pytest.mark.POST
    def test_TC_43373_POST_Authorization_Systems_Distribute_Persmission(self, context):
        """TC-43373 - Authorization_Systems-POST
           Verify that user is able to generate Token with permission [Distribute] while same is selected in the Authorization system using request POST /authorizationSystems/{id}/generateToken  "."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to generate Token with permission [Distribute] while same is selected in the Authorization system using request POST /authorizationSystems/{id}/generateToken  "."""):

            ### Positive test example

            # Test case configuration
            tokenGenerationDetails = context.sc.TokenGenerationDetails(
                audience='qed:a1',
                expirationTime='2017-09-30T06:10:50.714Z',
                generatedToken='string',
                issueTime='2016-01-29T06:10:50.714Z',
                jwtId=None,
                macKey='123456789012345678901234567890121',
                notBeforeTime='2017-09-30T06:10:50.714Z',
                permissions=['MANAGE_SYSTEM', 'MANAGE_CONFIGURATION'],
                qeda={},
                qedp={},
                referrer=None,
                subject='AU3',
                url='',
                useCompactPermissions=True)


            # generateToken the Authorization_Systems.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Authorization_Systems.generateToken(
                    id='generateToken', 
                    body=tokenGenerationDetails
                
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is able to generate Token with permission [Distribute] while same is selected in the Authorization system using request POST /authorizationSystems/{id}/generateToken  "."""):

            ### Negative test example

            # Test case configuration
            tokenGenerationDetails = context.sc.TokenGenerationDetails(
                audience='qed:a1',
                expirationTime='2017-09-30T06:10:50.714Z',
                generatedToken='string',
                issueTime='2016-01-29T06:10:50.714Z',
                jwtId=None,
                macKey='123456789012345678901234567890121',
                notBeforeTime='2017-09-30T06:10:50.714Z',
                permissions=['MANAGE_SYSTEM', 'MANAGE_CONFIGURATION'],
                qeda={},
                qedp={},
                referrer=None,
                subject='AU3',
                url='',
                useCompactPermissions=True)


            # prepare the request, so we can modify it
            request = context.cl.Authorization_Systems.generateToken(
                    id='generateToken', 
                    body=tokenGenerationDetails
                
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # generateToken the Authorization_Systems, and check we got the error we expect
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
