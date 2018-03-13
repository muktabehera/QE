# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-42569 - Routes POST:

  Verify that user is able to Edit/Delete all the entities under "VideoNet Configuration" with "Manage Configuration" permission while "Configuration admin can edit" and "Configuration admin can create" flags are set to true within token expiration time.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X POST -d @<JSON_data_file> -H "Content-Type:
       application/json" "<PF_host>://<client_host>/routes"

Same, with test data:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X POST -d @<JSON_data_file> -H "Content-Type:
       application/json" "<PF_host>://<client_host>/routes"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': True,
   'configurations': [{'id': 'automation'}],
   'hops': [{'hops': [],
             'member': {'id': 'autoVideonetEdge'},
             'memberRoles': ['EDGE'],
             'memberType': 'EDGE_DEVICE'}],
   'id': 'autoDeleteRoute',
   'name': 'Auto Delete Route',
   'visibleInAllConfigurations': False}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Routes')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Routes test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42569')
    @pytest.mark.Routes
    @pytest.mark.POST
    def test_TC_42569_POST_Routes_Id(self, context):
        """TC-42569 - Routes-POST
           Verify that user is able to Edit/Delete all the entities under "VideoNet Configuration" with "Manage Configuration" permission while "Configuration admin can edit" and "Configuration admin can create" flags are set to true within token expiration time."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to Edit/Delete all the entities under "VideoNet Configuration" with "Manage Configuration" permission while "Configuration admin can edit" and "Configuration admin can create" flags are set to true within token expiration time."""):

            ### Positive test example

            # Test case configuration
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'automation'
                }],
                constraintViolations=None,
                hops=[{
                    'member': {
                        'id': 'autoVideonetEdge'
                    },
                    'memberType': 'EDGE_DEVICE',
                    'memberRoles': ['EDGE'],
                    'hops': []
                }],
                id='autoDeleteRoute',
                name='Auto Delete Route',
                visibleInAllConfigurations=False)


            # createEntity the Routes.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Routes.createEntity(
                    body=routeDetails
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is able to Edit/Delete all the entities under "VideoNet Configuration" with "Manage Configuration" permission while "Configuration admin can edit" and "Configuration admin can create" flags are set to true within token expiration time."""):

            ### Negative test example

            # Test case configuration
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'automation'
                }],
                constraintViolations=None,
                hops=[{
                    'member': {
                        'id': 'autoVideonetEdge'
                    },
                    'memberType': 'EDGE_DEVICE',
                    'memberRoles': ['EDGE'],
                    'hops': []
                }],
                id='autoDeleteRoute',
                name='Auto Delete Route',
                visibleInAllConfigurations=False)


            # prepare the request, so we can modify it
            request = context.cl.Routes.createEntity(
                    body=routeDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # createEntity the Routes, and check we got the error we expect
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
