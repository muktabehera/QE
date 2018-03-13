# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audiences.

* TC-45519 - Audiences PATCH:

  Verify that user is not able to add duplicate Clients/Network Locations/Delivery Systems in Audience using request PATCH "/audiences/{id}".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences/PATCH_Audience"

JSON data sent to PathFinder in this test:

  {'clients': [{'id': 'clientsWithAllDetails'},
               {'id': 'clientsWithAllDetails'},
               {'id': 'clientsWithAllDetails'}],
   'deliverySystems': [{'id': 'VNE_Testing_API'},
                       {'id': 'VNE_Testing_API'},
                       {'id': 'VNE_Testing_API'}],
   'name': 'PATCH_audience_addDuplicateClientNtwrkLocationDS',
   'networkLocations': [{'id': 'NetworkLocationWithRulesGroups'},
                        {'id': 'NetworkLocationWithRulesGroups'},
                        {'id': 'NetworkLocationWithRulesGroups'}]}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.allure.issue('https://jira.qumu.com/browse/QED-1427')
@pytest.mark.components
@pytest.allure.story('Audiences')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Audiences test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-45519')
    @pytest.mark.Audiences
    @pytest.mark.PATCH
    def test_TC_45519_PATCH_Audiences_Add_Duplicate_Client_Ntwrk_Location_Ds(self, context):
        """TC-45519 - Audiences-PATCH
           Verify that user is not able to add duplicate Clients/Network Locations/Delivery Systems in Audience using request PATCH "/audiences/{id}"."""
        # Define a test step

        with pytest.allure.step("""Verify that user is not able to add duplicate Clients/Network Locations/Delivery Systems in Audience using request PATCH "/audiences/{id}"."""):

            # Test case configuration
            context.status.globals.deliverySystemsId = 'POST_veDevices_AllConfigAdminMulticastTrueTWO'
            audienceDetails = context.sc.AudienceDetails(
                clients=[{
                    'id': 'clientsWithAllDetails'
                }, {
                    'id': 'clientsWithAllDetails'
                }, {
                    'id': 'clientsWithAllDetails'
                }],
                configurationId=None,
                deliverySystems=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrueTWO'
                }, {
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrueTWO'
                }, {
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrueTWO'
                }],
                estimatedTimeForMulticastStreamsToBeAvailable=None,
                id=None,
                name='PATCH_audience_addDuplicateClientNtwrkLocationDS',
                networkLocations=[{
                    'id': 'NetworkLocationWithRulesGroups'
                }, {
                    'id': 'NetworkLocationWithRulesGroups'
                }, {
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
                    should.start_with('may not be empty'),
                    should.start_with('Invalid page parameter specified'),
                    should.contain('Invalid Authorization Token')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
