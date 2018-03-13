# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-42567 - Groups POST:

  Verify that user is able to Create entities under "VideoNet Configuration" with "Manage Configuration" permission while "Config admin can create" flag is set to true, within the token expiration time.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X POST -d @<JSON_data_file> -H "Content-Type:
       application/json" "<PF_host>://<client_host>/groups"

Same, with test data:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X POST -d @<JSON_data_file> -H "Content-Type:
       application/json" "<PF_host>://<client_host>/groups"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': True,
   'configurations': [{'id': 'automation'}],
   'deliveryLoadBalancePolicy': 'PROXIMITY_MATCHES',
   'dnsName': '10.1.25.46',
   'edgeDeviceRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
   'id': 'autoGroup',
   'members': [{'id': 'autoVideonetEdge'}],
   'name': 'Post: Auto Group',
   'originLoadBalancePolicy': 'DNS_NAME',
   'provisioningPolicy': 'ALL_MEMBERS',
   'visibleInAllConfigurations': False}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Groups')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Groups test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42567')
    @pytest.mark.Groups
    @pytest.mark.POST
    def test_TC_42567_POST_Groups_Admin_Create_Config_True(self, context):
        """TC-42567 - Groups-POST
           Verify that user is able to Create entities under "VideoNet Configuration" with "Manage Configuration" permission while "Config admin can create" flag is set to true, within the token expiration time."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to Create entities under "VideoNet Configuration" with "Manage Configuration" permission while "Config admin can create" flag is set to true, within the token expiration time."""):

            ### Positive test example

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'automation'
                }],
                deliveryLoadBalancePolicy='PROXIMITY_MATCHES',
                dnsName='10.1.25.46',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id='autoGroup',
                members=[{
                    'id': 'autoVideonetEdge'
                }],
                name='Post: Auto Group',
                originLoadBalancePolicy='DNS_NAME',
                provisioningPolicy='ALL_MEMBERS',
                proximityDetails=None,
                visibleInAllConfigurations=False)


            # createEntity the Groups.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Groups.createEntity(
                    body=edgeDeviceGroupDetails
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is able to Create entities under "VideoNet Configuration" with "Manage Configuration" permission while "Config admin can create" flag is set to true, within the token expiration time."""):

            ### Negative test example

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'automation'
                }],
                deliveryLoadBalancePolicy='PROXIMITY_MATCHES',
                dnsName='10.1.25.46',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id='autoGroup',
                members=[{
                    'id': 'autoVideonetEdge'
                }],
                name='Post: Auto Group',
                originLoadBalancePolicy='DNS_NAME',
                provisioningPolicy='ALL_MEMBERS',
                proximityDetails=None,
                visibleInAllConfigurations=False)


            # prepare the request, so we can modify it
            request = context.cl.Groups.createEntity(
                    body=edgeDeviceGroupDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # createEntity the Groups, and check we got the error we expect
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
