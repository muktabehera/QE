# -*- coding: UTF-8 -*-

"""PFE Component Tests - Authorization_Systems.

* TC-42556 - Authorization_Systems POST:

  Verify that user with Manage Configuration permission is able to delete entities on "System Configuration" pages  if "Config admin can create" is True in Configuration and "Configuration admin can edit" is true in the entity. .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X POST -d @<JSON_data_file> -H "Content-Type:
       application/json" "<PF_host>://<client_host>/authorizationSystems"

Same, with test data:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X POST -d @<JSON_data_file> -H "Content-Type:
       application/json" "<PF_host>://<client_host>/authorizationSystems"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': True,
   'configurations': [{'id': 'automation'}],
   'grantablePermissions': ['manageSystem', 'generate', 'manageConfiguration'],
   'id': 'Delete_authorizationSystem',
   'macKey': '11111111111111111111111111111111',
   'name': 'Delete_authorizationSystem',
   'visibleInAllConfigurations': False}

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42556')
    @pytest.mark.Authorization_Systems
    @pytest.mark.POST
    def test_TC_42556_POST_Authorization_Systems_Id(self, context):
        """TC-42556 - Authorization_Systems-POST
           Verify that user with Manage Configuration permission is able to delete entities on "System Configuration" pages  if "Config admin can create" is True in Configuration and "Configuration admin can edit" is true in the entity. ."""
        # Define a test step
        with pytest.allure.step("""Verify that user with Manage Configuration permission is able to delete entities on "System Configuration" pages  if "Config admin can create" is True in Configuration and "Configuration admin can edit" is true in the entity. ."""):

            ### Positive test example

            # Test case configuration
            authorizationSystemDetails = context.sc.AuthorizationSystemDetails(
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'automation'
                }],
                grantablePermissions=['manageSystem', 'generate', 'manageConfiguration'],
                id='Delete_authorizationSystem',
                macKey='11111111111111111111111111111111',
                name='Delete_authorizationSystem',
                visibleInAllConfigurations=False)


            # createEntity the Authorization_Systems.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Authorization_Systems.createEntity(
                    body=authorizationSystemDetails
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user with Manage Configuration permission is able to delete entities on "System Configuration" pages  if "Config admin can create" is True in Configuration and "Configuration admin can edit" is true in the entity. ."""):

            ### Negative test example

            # Test case configuration
            authorizationSystemDetails = context.sc.AuthorizationSystemDetails(
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'automation'
                }],
                grantablePermissions=['manageSystem', 'generate', 'manageConfiguration'],
                id='Delete_authorizationSystem',
                macKey='11111111111111111111111111111111',
                name='Delete_authorizationSystem',
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
                    should.start_with('may not be empty'),
                    should.start_with('Invalid page parameter specified'),
                    should.contain('Invalid Authorization Token')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
