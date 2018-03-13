# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audiences.

* TC-43143 - Audiences POST:

  Verify that correct message is displayed while creating Audience with providing invalid value for Network Location using request POST /audiences.


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
   'id': 'POSTAudiInvalidNetwork',
   'name': 'POSTAudiInvalidNetwork',
   'networkLocations': [{'id': 'NetworkLocationWithRulesGroups1234'}]}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Audiences')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Audiences test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43143')
    @pytest.mark.Audiences
    @pytest.mark.POST
    def test_TC_43143_POST_Audiences_Message_Invalid_Network_Location(self, context):
        """TC-43143 - Audiences-POST
           Verify that correct message is displayed while creating Audience with providing invalid value for Network Location using request POST /audiences."""
        # Define a test step

        with pytest.allure.step("""Verify that correct message is displayed while creating Audience with providing invalid value for Network Location using request POST /audiences."""):

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
                id='POSTAudiInvalidNetwork',
                name='POSTAudiInvalidNetwork',
                networkLocations=[{
                    'id': 'InvalidNetworkLocation'
                }])


            # prepare the request, so we can modify it
            request = context.cl.Audiences.createEntity(
                    body=audienceDetails
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
                    should.start_with('Invalid entity')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
