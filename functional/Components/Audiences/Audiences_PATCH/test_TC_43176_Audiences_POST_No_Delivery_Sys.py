# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audiences.

* TC-43176 - Audiences POST:

   Verify that correct validation message is displayed while removing mandatory field (Delivery System) from Audience  using PATCH "audiences/{id}".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences"

JSON data sent to PathFinder in this test:

  {'clients': [{'id': 'clientsWithAllDetails'}],
   'deliverySystems': [{'id': 'VNE_Testing_API'}],
   'id': 'PATCH_Audience',
   'name': 'PATCH_Audience',
   'networkLocations': [{'id': 'NetworkLocationWithRulesGroups'}]}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Audiences')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Audiences test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43176')
    @pytest.mark.Audiences
    @pytest.mark.POST
    def test_TC_43176_POST_Audiences_No_Delivery_Sys(self, context):
        """TC-43176 - Audiences-POST
            Verify that correct validation message is displayed while removing mandatory field (Delivery System) from Audience  using PATCH "audiences/{id}"."""
        # Define a test step
        with pytest.allure.step(""" Verify that an Audience is created first using POST"""):

            # Test case configuration
            audienceDetails = context.sc.AudienceDetails(
                clients=[{
                    'id': 'clientsWithAllDetails'
                }],
                configurationId=None,
                deliverySystems=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                estimatedTimeForMulticastStreamsToBeAvailable=None,
                id='PATCH_Audience123',
                name='PATCH_Audience123',
                networkLocations=[{
                    'id': 'NetworkLocationWithRulesGroups'
                }])


            # createEntity the Audiences.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Audiences.createEntity(
                    body=audienceDetails
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step(""" Verify that correct validation message is displayed while removing mandatory field (Delivery System) from Audience  using PATCH "audiences/{id}"."""):



            # Test case configuration
            audienceDetails = context.sc.AudienceDetails(
                clients=[{
                    'id': 'clientsWithAllDetails'
                }],
                configurationId=None,
                deliverySystems=[],
                estimatedTimeForMulticastStreamsToBeAvailable=None,
                id='PATCH_Audience123',
                name='PATCH_Audience123',
                networkLocations=[{
                    'id': 'NetworkLocationWithRulesGroups'
                }])


            # prepare the request, so we can modify it
            request = context.cl.Audiences.updateEntity(
                    body=audienceDetails,
                    id='PATCH_Audience123'
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # createEntity the Audiences, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('size must be between 1 and 2147483647')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
