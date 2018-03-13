# -*- coding: UTF-8 -*-

"""PFE Component Tests - Audiences.

* TC-42284 - Audiences POST:

  Verify that Create button is not displayed on 'Proximities zones' page under Intelligent Content Routing menu for user with "Manage Configuration" permission, while "Config admin can create" flag is set to false within the token expiration time.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X POST -d @<JSON_data_file> -H "Content-Type:
       application/json" "<PF_host>://<client_host>/audiences"

Same, with test data:

  curl -H "Host: <client_host>" -k -H "Authorization: Bearer
       <valid_token>" -X POST -d @<JSON_data_file> -H "Content-Type:
       application/json" "<PF_host>://<client_host>/audiences"

JSON data sent to PathFinder in this test:

  {'clients': [{'id': 'auto_client'}],
   'id': 'adminFlagSetToFalse',
   'name': 'Unable To POST audience',
   'networkLocations': [{'id': 'auto_network'}],
   'protectedDeliverySystems': [],
   'publicDeliverySystems': [{'id': 'auto_DS'}]}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Audiences')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Audiences test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42284')
    @pytest.mark.Audiences
    @pytest.mark.POST
    def test_TC_42284_POST_Audiences_Admin_Create_Flag_Set_To_False(self, context):
        """TC-42284 - Audiences-POST
           Verify that Create button is not displayed on 'Proximities zones' page under Intelligent Content Routing menu for user with "Manage Configuration" permission, while "Config admin can create" flag is set to false within the token expiration time."""
        # Define a test step
        with pytest.allure.step("""Verify that Create button is not displayed on 'Proximities zones' page under Intelligent Content Routing menu for user with "Manage Configuration" permission, while "Config admin can create" flag is set to false within the token expiration time."""):

            ### Positive test example

            # Test case configuration
            audienceDetails = context.sc.AudienceDetails(
                clients=[{
                    'id': 'auto_client'
                }],
                configurationId=None,
                deliverySystems=None,
                estimatedTimeForMulticastStreamsToBeAvailable=None,
                id='adminFlagSetToFalse',
                name='Unable To POST audience',
                networkLocations=[{
                    'id': 'auto_network'
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

        with pytest.allure.step("""Verify that Create button is not displayed on 'Proximities zones' page under Intelligent Content Routing menu for user with "Manage Configuration" permission, while "Config admin can create" flag is set to false within the token expiration time."""):

            ### Negative test example

            # Test case configuration
            audienceDetails = context.sc.AudienceDetails(
                clients=[{
                    'id': 'auto_client'
                }],
                configurationId=None,
                deliverySystems=None,
                estimatedTimeForMulticastStreamsToBeAvailable=None,
                id='adminFlagSetToFalse',
                name='Unable To POST audience',
                networkLocations=[{
                    'id': 'auto_network'
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
                    should.start_with('may not be empty'),
                    should.start_with('Invalid page parameter specified'),
                    should.contain('Invalid Authorization Token')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
