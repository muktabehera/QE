# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-44426 - Groups POST:

  Verify that correct error message is displayed in response on providing invalid values in parameters 'id' using request POST /groups.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/groups"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': True,
   'configurations': [],
   'deliveryLoadBalancePolicy': 'PROXIMITY_MATCHES',
   'dnsName': '10.1.25.46',
   'edgeDeviceRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
   'id': 'POST ID',
   'members': [{'id': 'Device_Test_API'}],
   'name': 'Group Id invalid 1',
   'originLoadBalancePolicy': 'DNS_NAME',
   'provisioningPolicy': 'ALL_MEMBERS',
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Groups')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Groups test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44426')
    @pytest.mark.Groups
    @pytest.mark.POST
    def test_TC_44426_POST_Groups_Group_Invalid_Id(self, context):
        """TC-44426 - Groups-POST
           Verify that correct error message is displayed in response on providing invalid values in parameters 'id' using request POST /groups."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that correct error message is displayed in response on providing invalid values in parameters 'id' using request POST /groups."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='PROXIMITY_MATCHES',
                dnsName='10.1.25.46',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id='POST ID',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Group Id invalid 1',
                originLoadBalancePolicy='DNS_NAME',
                provisioningPolicy='ALL_MEMBERS',
                proximityDetails=None,
                visibleInAllConfigurations=True)


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
                    should.start_with('Invalid identifier, the pattern must match \"^\\p{Alnum}+[\\w\\-\\:\\.]*$\"')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))


        # Define a test step
        with pytest.allure.step("""Test2: Verify that correct error message is displayed in response on providing invalid values in parameters 'id' using request POST /groups."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='PROXIMITY_MATCHES',
                dnsName='10.1.25.46',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id='POST 1234',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Group Id invalid 2',
                originLoadBalancePolicy='DNS_NAME',
                provisioningPolicy='ALL_MEMBERS',
                proximityDetails=None,
                visibleInAllConfigurations=True)


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
                    should.start_with('Invalid identifier, the pattern must match \"^\\p{Alnum}+[\\w\\-\\:\\.]*$\"')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))



        # Define a test step
        with pytest.allure.step("""Test3: Verify that correct error message is displayed in response on providing invalid values in parameters 'id' using request POST /groups."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='PROXIMITY_MATCHES',
                dnsName='10.1.25.46',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id='POST<>!@#$%^&*;/?',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Group Id invalid 3',
                originLoadBalancePolicy='DNS_NAME',
                provisioningPolicy='ALL_MEMBERS',
                proximityDetails=None,
                visibleInAllConfigurations=True)


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
                    should.start_with('Invalid identifier, the pattern must match \"^\\p{Alnum}+[\\w\\-\\:\\.]*$\"')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))


        # Define a test step
        with pytest.allure.step("""Test4: Verify that correct error message is displayed in response on providing invalid values in parameters 'id' using request POST /groups."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='PROXIMITY_MATCHES',
                dnsName='10.1.25.46',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id=' ',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Group Id invalid 4',
                originLoadBalancePolicy='DNS_NAME',
                provisioningPolicy='ALL_MEMBERS',
                proximityDetails=None,
                visibleInAllConfigurations=True)


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
                    should.start_with('Invalid identifier, the pattern must match \"^\\p{Alnum}+[\\w\\-\\:\\.]*$\"'),
                    should.start_with('may not be empty')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))



        # Define a test step
        with pytest.allure.step("""Test5: Verify that correct error message is displayed in response on providing invalid values in parameters 'id' using request POST /groups."""):

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[],
                deliveryLoadBalancePolicy='PROXIMITY_MATCHES',
                dnsName='10.1.25.46',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id='-_:.',
                members=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                name='Group Id invalid 5',
                originLoadBalancePolicy='DNS_NAME',
                provisioningPolicy='ALL_MEMBERS',
                proximityDetails=None,
                visibleInAllConfigurations=True)


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
                    should.start_with('Invalid identifier, the pattern must match \"^\\p{Alnum}+[\\w\\-\\:\\.]*$\"')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
