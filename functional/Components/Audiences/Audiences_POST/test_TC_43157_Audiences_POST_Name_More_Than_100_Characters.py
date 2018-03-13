# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audiences.

* TC-43157 - Audiences POST:

  Verify that user is unable to create Audience  having length greater than 100 characters in Name parameter using request POST /audiences.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/audiences"

JSON data sent to PathFinder in this test:

  {'clients': [{'id': 'clientsWithAllDetails'}, {'id': 'autoclient'}],
   'deliverySystems': [{'id': 'VNE_Testing_API'}],
   'id': 'POST_audience_NameUpto100Characters',
   'name': 'POST_audience_NameUpto100CharactersPOST_audience_NameUpto100CharactersPOST_audience_NameUpto100Charaa',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43157')
    @pytest.mark.Audiences
    @pytest.mark.POST
    def test_TC_43157_POST_Audiences_Name_More_Than_100_Characters(self, context):
        """TC-43157 - Audiences-POST
           Verify that user is unable to create Audience  having length greater than 100 characters in Name parameter using request POST /audiences."""
        # Define a test step

        with pytest.allure.step("""Verify that user is unable to create Audience  having length greater than 100 characters in Name parameter using request POST /audiences."""):

            # Test case configuration
            audienceDetails = context.sc.AudienceDetails(
                clients=[{
                    'id': 'clientsWithAllDetails'
                }, {
                    'id': 'autoclient'
                }],
                configurationId=None,
                deliverySystems=[{
                    'id': 'POST_veDevices_AllConfigAdminMulticastTrue'
                }],
                estimatedTimeForMulticastStreamsToBeAvailable=None,
                id='POST_audience_NameUpto100Characters',
                name=
                'POST_audience_NameUpto100CharactersPOST_audience_NameUpto100CharactersPOST_audience_NameUpto100Charaa',
                networkLocations=[{
                    'id': 'NetworkLocationWithRulesGroups'
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
                    should.start_with('length must be between 1 and 100'),
                    should.start_with('Invalid entity')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
