# -*- coding: UTF-8 -*-

"""PFE Component Tests - Authorization_Systems.

* TC-43288 - Authorization_Systems POST:

  Verify that correct message is displayed while creating Authorization System on providing no value for "Name" parameter using request POST /authorizationSystems.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/authorizationSystems"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/authorizationSystems"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': True,
   'configurations': [{'host': '172.30.5.204', 'id': 'default'}],
   'grantablePermissions': ['manageSystem', 'generate', 'manageConfiguration'],
   'id': 'POST_authorizationSystem_correctMessage_noNameprovided',
   'macKey': '1123456897813256498713254698713564987321654987314654',
   'name': '',
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Authorization_Systems')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Authorization_Systems test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43288')
    @pytest.mark.Authorization_Systems
    @pytest.mark.POST
    def test_TC_43288_POST_Authorization_Systems_Correct_Message_No_Nameprovided(self, context):
        """TC-43288 - Authorization_Systems-POST
           Verify that correct message is displayed while creating Authorization System on providing no value for "Name" parameter using request POST /authorizationSystems."""
        # Define a test step
        with pytest.allure.step("""Verify that correct message is displayed while creating Authorization System on providing no value for "Name" parameter using request POST /authorizationSystems."""):

            # Test case configuration
            authorizationSystemDetails = context.sc.AuthorizationSystemDetails(
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'default',
                    'host': '172.30.5.204'
                }],
                grantablePermissions=['manageSystem', 'generate', 'manageConfiguration'],
                id='POST_authorizationSystem_correctMessage_noNameprovided',
                macKey='1123456897813256498713254698713564987321654987314654',
                name='',
                visibleInAllConfigurations=True)


            # prepare the request, so we can modify it
            request = context.cl.Authorization_Systems.createEntity(
                    body=authorizationSystemDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # createEntity the Authorization_Systems, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Invalid name, the pattern must match \"^[\\p{IsAlphabetic}\\p{IsDigit}]+[\\p{Blank}\\p{IsAlphabetic}\\p{IsDigit}[\\p{Punct}&&[^/\\<>\\|\\^]]]*$\"'),
                    should.start_with('length must be between 1 and 100'),
                    should.start_with('size must be between 1 and 2147483647'),
                    should.start_with('may not be empty')
                )

            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
