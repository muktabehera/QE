# -*- coding: UTF-8 -*-

"""PFE Component Tests - Authorization_Systems.

* TC-42557 - Authorization_Systems PATCH:

  Verify that user with Manage Configuration permission is unable to edit/delete entities on "Authorization System" and "Origin" page  if "Config admin can create"  and "Configuration admin can edit" is set to true, after token expiry time. .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X PATCH -d @<JSON_data_file> -H "Content-Type:
       application/json"
       "<PF_host>://<client_host>/authorizationSystems/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X PATCH -d @<JSON_data_file> -H "Content-Type:
       application/json"
       "<PF_host>://<client_host>/authorizationSystems/autoAuthorization"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': True,
   'configurations': [{'id': 'automation'}],
   'grantablePermissions': ['manageSystem', 'generate', 'manageConfiguration'],
   'name': 'PATCH: Auto Authorization',
   'visibleInAllConfigurations': False}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Authorization_Systems')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Authorization_Systems test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42557')
    @pytest.mark.Authorization_Systems
    @pytest.mark.PATCH
    def test_TC_42557_PATCH_Authorization_Systems_Modify_Name(self, context):
        """TC-42557 - Authorization_Systems-PATCH
           Verify that user with Manage Configuration permission is unable to edit/delete entities on "Authorization System" and "Origin" page  if "Config admin can create"  and "Configuration admin can edit" is set to true, after token expiry time. ."""
        # Define a test step
        with pytest.allure.step("""Verify that user with Manage Configuration permission is unable to edit/delete entities on "Authorization System" and "Origin" page  if "Config admin can create"  and "Configuration admin can edit" is set to true, after token expiry time. ."""):

            ### Positive test example

            # Test case configuration
            authorizationSystemDetails = context.sc.AuthorizationSystemDetails(
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'automation'
                }],
                grantablePermissions=['manageSystem', 'generate', 'manageConfiguration'],
                id=None,
                macKey=None,
                name='PATCH: Auto Authorization',
                visibleInAllConfigurations=False)


            # updateEntity the Authorization_Systems.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Authorization_Systems.updateEntity(
                    body=authorizationSystemDetails, 
                    id='autoAuthorization'
                
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user with Manage Configuration permission is unable to edit/delete entities on "Authorization System" and "Origin" page  if "Config admin can create"  and "Configuration admin can edit" is set to true, after token expiry time. ."""):

            ### Negative test example

            # Test case configuration
            authorizationSystemDetails = context.sc.AuthorizationSystemDetails(
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'automation'
                }],
                grantablePermissions=['manageSystem', 'generate', 'manageConfiguration'],
                id=None,
                macKey=None,
                name='PATCH: Auto Authorization',
                visibleInAllConfigurations=False)


            # prepare the request, so we can modify it
            request = context.cl.Authorization_Systems.updateEntity(
                    body=authorizationSystemDetails, 
                    id='autoAuthorization'
                
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateEntity the Authorization_Systems, and check we got the error we expect
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
