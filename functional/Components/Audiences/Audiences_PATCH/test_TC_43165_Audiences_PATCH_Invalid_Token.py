# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audiences.

* TC-43165 - Audiences PATCH:

  Verify that user is unable to modify(PATCH) the Audience using request  audiences/{id} "  with invalid token.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <invalid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <invalid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences/PATCH_Audience"

JSON data sent to PathFinder in this test:

  {'clients': [{'id': 'client1', 'name': 'client'}],
   'deliverySystems': [{'id': 'AudienceLinuxStandalone172.30.3.124',
                        'name': 'AudienceLinuxStandalone172.30.3.124'}],
   'id': 'PATCH_Audience',
   'name': 'PATCH_AudienceModified',
   'networkLocations': [{'id': '192.16.17.170', 'name': 'local'}]}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Audiences')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Audiences test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43165')
    @pytest.mark.Audiences
    @pytest.mark.PATCH
    def test_TC_43165_PATCH_Audiences_Invalid_Token(self, context):
        """TC-43165 - Audiences-PATCH
           Verify that user is unable to modify(PATCH) the Audience using request  audiences/{id} "  with invalid token."""
        # Define a test step


        with pytest.allure.step("""Verify that user is unable to modify(PATCH) the Audience using request  audiences/{id} "  with invalid token."""):


            # Test case configuration
            audienceDetails = context.sc.AudienceDetails(
                clients=[{
                    'id': 'clientsWithAllDetails'
                }],
                configurationId=None,
                deliverySystems=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrueTWO'
                }],
                estimatedTimeForMulticastStreamsToBeAvailable=None,
                id=None,
                name='invalidToken',
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
                    token='invalid_token',
                    quiet=True, returnResponse=True

                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Invalid Authorization Token')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
