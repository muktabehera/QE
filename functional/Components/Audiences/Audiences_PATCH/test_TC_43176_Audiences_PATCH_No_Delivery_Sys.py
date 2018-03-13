# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audiences.

* TC-43176 - Audiences PATCH:

   Verify that correct validation message is displayed while removing mandatory field (Delivery System) from Audience  using PATCH "audiences/{id}".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences/PATCH_Audience"

JSON data sent to PathFinder in this test:

  {'clients': [{'id': 'clientsWithAllDetails'}],
   'deliverySystems': [],
   'name': 'PATCH_audience_noPublicProtectedDeliverySys',
   'networkLocations': [{'id': 'NetworkLocationWithRulesGroups'}]}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Audiences')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Audiences test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43176')
    @pytest.mark.Audiences
    @pytest.mark.PATCH
    def test_TC_43176_PATCH_Audiences_No_Delivery_Sys(self, context):
        """TC-43176 - Audiences-PATCH
            Verify that correct validation message is displayed while removing mandatory field (Delivery System) from Audience  using PATCH "audiences/{id}"."""
        # Define a test step

        with pytest.allure.step(""" Verify that correct validation message is displayed while removing mandatory field (Delivery System) from Audience  using PATCH "audiences/{id}"."""):

            # Test case configuration
            audienceDetails = context.sc.AudienceDetails(
                clients=[{
                    'id': 'clientsWithAllDetails'
                }],
                configurationId=None,
                deliverySystems=[],
                estimatedTimeForMulticastStreamsToBeAvailable=None,
                id=None,
                name='PATCH_audience_noPublicProtectedDeliverySys',
                networkLocations=[{
                    'id': 'NetworkLocationWithRulesGroups'
                }])


            # prepare the request, so we can modify it
            request = context.cl.Audiences.updateEntity(
                    body=audienceDetails, 
                    id='PATCH_Audience'
                
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateEntity the Audiences, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('size must be between 1 and 2147483647'),
                    should.start_with('Invalid delivery system')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
