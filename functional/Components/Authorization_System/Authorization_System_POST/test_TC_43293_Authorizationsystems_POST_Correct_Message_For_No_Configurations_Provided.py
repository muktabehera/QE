# -*- coding: UTF-8 -*-

"""PFE Component Tests - Authorization_Systems.

* TC-43293 - Authorization_Systems POST:

  Verify that correct message is displayed while creating Authorization System for  "Configurations" parameter is not provided and "visibleInAllConfigurations" is set to false parameter using request POST /authorizationSystems.


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
   'configurations': [],
   'grantablePermissions': ['manageSystem', 'generate', 'manageConfiguration'],
   'id': 'POST_authorizationSystem_correctMessage_forNoConfigurationsProvided',
   'macKey': '12134687987654987651465498798798654564988494746465',
   'name': 'POST_authorizationSystem_correctMessage_forNoConfigurationsProvided',
   'visibleInAllConfigurations': False}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Authorization_Systems')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Authorization_Systems test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43293')
    @pytest.mark.Authorization_Systems
    @pytest.mark.POST
    def test_TC_43293_POST_Authorization_Systems_Correct_Message_For_No_Configurations_Provided(self, context):
        """TC-43293 - Authorization_Systems-POST
           Verify that correct message is displayed while creating Authorization System for  "Configurations" parameter is not provided and "visibleInAllConfigurations" is set to false parameter using request POST /authorizationSystems."""
        # Define a test step
        with pytest.allure.step("""Verify that correct message is displayed while creating Authorization System for  "Configurations" parameter is not provided and "visibleInAllConfigurations" is set to false parameter using request POST /authorizationSystems."""):

            # Test case configuration
            authorizationSystemDetails = context.sc.AuthorizationSystemDetails(
                configAdminCanEdit=True,
                configurations=[],
                grantablePermissions=['manageSystem', 'generate', 'manageConfiguration'],
                id='POST_authorizationSystem_correctMessage_forNoConfigurationsProvided',
                macKey='12134687987654987651465498798798654564988494746465',
                name='POST_authorizationSystem_correctMessage_forNoConfigurationsProvided',
                visibleInAllConfigurations=False)


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
                    should.start_with('Either provide the configurations where the system resource is visible or mark it visible in all configurations')
                    # should.start_with('Invalid page parameter specified'),
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
