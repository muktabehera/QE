# -*- coding: UTF-8 -*-

"""PFE Component Tests - Configurations.

* TC-43185 - Configurations POST:

  Verfiy that correct message is displayed on providing invalid values in configurations using POST request "/configurations".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/configurations"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/configurations"

JSON data sent to PathFinder in this test:

  {'configAdminCanCreate': False, 'host': '!@', 'id': '!@aa'}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Configurations')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Configurations test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43185')
    @pytest.mark.Configurations
    @pytest.mark.POST
    def test_TC_43185_POST_Configurations_Verify_Correct_Message_Displayed_With_Invalid_Values(self, context):
        """TC-43185 - Configurations-POST
           Verfiy that correct message is displayed on providing invalid values in configurations using POST request "/configurations"."""
        # Define a test step
        with pytest.allure.step("""Verfiy that correct message is displayed on providing invalid values in configurations using POST request "/configurations"."""):

            ### Positive test example

            # Test case configuration
            configurationDetails = context.sc.ConfigurationDetails(
                configAdminCanCreate=False,
                configurationType=None,
                dsId=None,
                host='!@',
                id='!@aa',
                reflectorServiceActivationStatus=None)


            # createEntity the Configurations.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Configurations.createEntity(
                    body=configurationDetails
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verfiy that correct message is displayed on providing invalid values in configurations using POST request "/configurations"."""):

            ### Negative test example

            # Test case configuration
            configurationDetails = context.sc.ConfigurationDetails(
                configAdminCanCreate=False,
                configurationType=None,
                dsId=None,
                host='!@',
                id='!@aa',
                reflectorServiceActivationStatus=None)


            # prepare the request, so we can modify it
            request = context.cl.Configurations.createEntity(
                    body=configurationDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # createEntity the Configurations, and check we got the error we expect
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
