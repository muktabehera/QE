# -*- coding: UTF-8 -*-

"""PFE Component Tests - Authorization_Systems.

* TC-43341 - Authorization_Systems POST:

  Verify that user is unable to create Authorization System having Mackey length value less than 32 characters and more than 512 characters with using request POST /authorizationSystems.


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
   'grantablePermissions': ['manageSystem',
                            'matchAny',
                            'provision',
                            'match',
                            'distribute',
                            'generate',
                            'manageConfiguration'],
   'id': 'POST_authorizationSystem_unableToCreate_macKeyLessThan32Character',
   'macKey': '12345',
   'name': 'POST_authorizationSystem_unableToCreate_macKeyLessThan32Character',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43341')
    @pytest.mark.Authorization_Systems
    @pytest.mark.POST
    def test_TC_43341_POST_Authorization_Systems_Authorization_System_Unable_To_Create_Mac_Key_Less_Than_32_Character(self, context):
        """TC-43341 - Authorization_Systems-POST
           Verify that user is unable to create Authorization System having Mackey length value less than 32 characters and more than 512 characters with using request POST /authorizationSystems."""
        # Define a test step

        with pytest.allure.step("""Test1: Verify that user is unable to create Authorization System having Mackey length value less than 32 characters."""):

            # Test case configuration
            authorizationSystemDetails = context.sc.AuthorizationSystemDetails(
                configAdminCanEdit=True,
                configurations=[],
                grantablePermissions=[
                    'manageSystem', 'matchAny', 'provision', 'match', 'distribute',
                    'generate', 'manageConfiguration'
                ],
                id='POST_authorizationSystem_unableToCreate_macKeyLessThan32Character',
                macKey='12345',
                name='POST_authorizationSystem_unableToCreate_macKeyLessThan32Character',
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
                    should.start_with('Invalid Authorization Token'),
                    should.start_with('length must be between 32 and 512')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))


            
        # Define a test step
        with pytest.allure.step("""Test2: Verify that user is unable to create Authorization System having Mackey length value more than 512 characters with using request POST /authorizationSystems."""):

            # Test case configuration
            authorizationSystemDetails = context.sc.AuthorizationSystemDetails(
                configAdminCanEdit=True,
                configurations=[],
                grantablePermissions=[
                    'manageSystem', 'matchAny', 'provision', 'match', 'distribute',
                    'generate', 'manageConfiguration'
                ],
                id='POST_authorizationSystem_unableToCreate_macKeyLessThan32Character',
                macKey=
                '124356798546132546798546213451243567985461325467985462134512435679854613254679854621345124356798546132546798546213451243567985461325467985462134512435679854613254679854621345124356798546132546798546213451243567985461325467985462134512435679854613254679854621345124356798546132546798546213451243567985461325467985462134512435679854613254679854621345124356798546132546798546213451243567985461325467985462134512435679854613254679854621345124356798546132546798546213451243567985461325467985462134512435679854613254679',
                name='POST_authorizationSystem_unableToCreate_macKeyLessThan32Character',
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
                    should.start_with('Invalid Authorization Token'),
                    should.start_with('length must be between 32 and 512')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
