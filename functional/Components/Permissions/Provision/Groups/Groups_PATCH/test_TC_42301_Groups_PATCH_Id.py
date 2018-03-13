# -*- coding: UTF-8 -*-

"""PFE Component Tests - Groups.

* TC-42301 - Groups PATCH:

  Verify that User is unable to Create/Edit/View/Delete, any entity on any page of the QED, using token with "Provision" permission within the token expiration time.


Equivalent test CURL command:

  curl -k -H "Host: <client_host>" -H "Authorization: Bearer
       <valid_token>" -X PATCH -d @<JSON_data_file> -H "Content-Type:
       application/json"
       "<PF_host>://<client_host>/groups/<data_ID1_under_test>"

Same, with test data:

  curl -k -H "Host: <client_host>" -H "Authorization: Bearer
       <valid_token>" -X PATCH -d @<JSON_data_file> -H "Content-Type:
       application/json"
       "<PF_host>://<client_host>/groups/testData_groups"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': True,
   'configurations': [{'id': 'default'}],
   'deliveryLoadBalancePolicy': 'DNS_NAME',
   'dnsName': 'autoQEDVCC1',
   'edgeDeviceRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
   'members': [{'id': 'autoEdge1'}],
   'name': 'Update Group Name',
   'originLoadBalancePolicy': 'ALL_MEMBERS',
   'provisioningPolicy': 'ONE_OR_MORE',
   'visibleInAllConfigurations': False}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Groups')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Groups test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42301')
    @pytest.mark.Groups
    @pytest.mark.PATCH
    def test_TC_42301_PATCH_Groups_Id(self, context):
        """TC-42301 - Groups-PATCH
           Verify that User is unable to Create/Edit/View/Delete, any entity on any page of the QED, using token with "Provision" permission within the token expiration time."""
        # Define a test step
        with pytest.allure.step("""Verify that User is unable to Create/Edit/View/Delete, any entity on any page of the QED, using token with "Provision" permission within the token expiration time."""):

            ### Positive test example

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'default'
                }],
                deliveryLoadBalancePolicy='DNS_NAME',
                dnsName='autoQEDVCC1',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id=None,
                members=[{
                    'id': 'autoEdge1'
                }],
                name='Update Group Name',
                originLoadBalancePolicy='ALL_MEMBERS',
                provisioningPolicy='ONE_OR_MORE',
                proximityDetails=None,
                visibleInAllConfigurations=False)


            # updateEntity the Groups.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Groups.updateEntity(
                    body=edgeDeviceGroupDetails, 
                    id='testData_groups'
                
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that User is unable to Create/Edit/View/Delete, any entity on any page of the QED, using token with "Provision" permission within the token expiration time."""):

            ### Negative test example

            # Test case configuration
            edgeDeviceGroupDetails = context.sc.EdgeDeviceGroupDetails(
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'default'
                }],
                deliveryLoadBalancePolicy='DNS_NAME',
                dnsName='autoQEDVCC1',
                edgeDeviceRoles=['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                id=None,
                members=[{
                    'id': 'autoEdge1'
                }],
                name='Update Group Name',
                originLoadBalancePolicy='ALL_MEMBERS',
                provisioningPolicy='ONE_OR_MORE',
                proximityDetails=None,
                visibleInAllConfigurations=False)


            # prepare the request, so we can modify it
            request = context.cl.Groups.updateEntity(
                    body=edgeDeviceGroupDetails, 
                    id='testData_groups'
                
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateEntity the Groups, and check we got the error we expect
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
