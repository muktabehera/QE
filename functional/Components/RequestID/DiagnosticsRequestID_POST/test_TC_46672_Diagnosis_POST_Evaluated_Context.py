# -*- coding: UTF-8 -*-

"""PFE Component Tests - Diagnosis.

* TC-46672 - Diagnosis POST:

  Verify that 'evaluatedContext' is displayed with parameters(remoteAddress, remoteHost, serverHost, serverPort, headers, query, tags) as per the provided model schema using request POST /diagnostices/requestId.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/diagnosis/requestId"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/diagnosis/requestId"

JSON data sent to PathFinder in this test:

  {'headers': [{'name': 'header', 'value': 'header'}],
   'query': [{'name': 'query', 'value': 'query'}],
   'remoteAddress': '192.16.17.106',
   'remoteHost': '192.16.17.106',
   'serverHost': '172.30.5.204',
   'serverPort': 80,
   'tags': [{'name': 'tag123', 'value': 'tag123'}]}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Diagnosis')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Diagnosis test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-46672')
    @pytest.mark.Diagnosis
    @pytest.mark.POST
    def test_TC_46672_POST_Diagnosis_Evaluated_Context(self, context):
        """TC-46672 - Diagnosis-POST
           Verify that 'evaluatedContext' is displayed with parameters(remoteAddress, remoteHost, serverHost, serverPort, headers, query, tags) as per the provided model schema using request POST /diagnostices/requestId."""
        # Define a test step
        with pytest.allure.step("""Verify that 'evaluatedContext' is displayed with parameters(remoteAddress, remoteHost, serverHost, serverPort, headers, query, tags) as per the provided model schema using request POST /diagnostices/requestId."""):

            ### Positive test example

            # Test case configuration
            networkContextEvaluationSetDetails = context.sc.NetworkContextEvaluationSetDetails(
                audienceEvaluations=None,
                clientEvaluations=None,
                evaluatedContext=None,
                networkLocationEvaluations=None)


            # evaluateNetworkContextPost the Diagnosis.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Diagnosis.evaluateNetworkContextPost(
                    body=networkContextEvaluationSetDetails
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that 'evaluatedContext' is displayed with parameters(remoteAddress, remoteHost, serverHost, serverPort, headers, query, tags) as per the provided model schema using request POST /diagnostices/requestId."""):

            ### Negative test example

            # Test case configuration
            networkContextEvaluationSetDetails = context.sc.NetworkContextEvaluationSetDetails(
                audienceEvaluations=None,
                clientEvaluations=None,
                evaluatedContext=None,
                networkLocationEvaluations=None)


            # prepare the request, so we can modify it
            request = context.cl.Diagnosis.evaluateNetworkContextPost(
                    body=networkContextEvaluationSetDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # evaluateNetworkContextPost the Diagnosis, and check we got the error we expect
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
