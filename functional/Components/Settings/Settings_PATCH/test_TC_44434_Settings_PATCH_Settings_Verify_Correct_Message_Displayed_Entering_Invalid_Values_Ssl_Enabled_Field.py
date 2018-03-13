# -*- coding: UTF-8 -*-

"""PFE Component Tests - Settings.

* TC-44434 - Settings PATCH:

  Verify correct message is displayed on entering invalid values ( 1234,abcd,!@#) in 'sslEnabled' field using request PATCH /settings.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/settings"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/settings"

JSON data sent to PathFinder in this test:

  {
    "configured": abcd,
    "hostname": "localhost",
    "port": 8080,
    "sslPort": 8443,
    "sslEnabled": false
  }

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Settings')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Settings test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44434')
    @pytest.mark.Settings
    @pytest.mark.PATCH
    def test_TC_44434_PATCH_Settings_Settings_Verify_Correct_Message_Displayed_Entering_Invalid_Values_Ssl_Enabled_Field(self, context):
        """TC-44434 - Settings-PATCH
           Verify correct message is displayed on entering invalid values ( 1234,abcd,!@#) in 'sslEnabled' field using request PATCH /settings."""

        # Define a test step
        with pytest.allure.step("""Test1: Verify user is getting correct message on entering invalid values (abcd) in 'sslEnabled' field using request PATCH /settings."""):

            # Test case configuration
            settingsDetails = context.sc.SettingsDetails(
                configured=True,
                hostname='localhost',
                port=8080,
                sslEnabled=abcd,
                sslPort=8443)

            # prepare the request, so we can modify it
            request = context.cl.Settings.updateSettings(
                body=settingsDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateSettings the Settings, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:  # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Unrecognized token'),
                    should.start_with('NameError: global name')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))



        # Define a test step
        with pytest.allure.step("""Test2: Verify user is getting correct message on entering invalid values (!@#) in 'sslEnabled' field using request PATCH /settings."""):

            # Test case configuration
            settingsDetails = context.sc.SettingsDetails(
                configured=True,
                hostname='localhost',
                port=8080,
                sslEnabled="!@#",
                sslPort=8443)

            # prepare the request, so we can modify it
            request = context.cl.Settings.updateSettings(
                body=settingsDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateSettings the Settings, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:  # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Unrecognized token'),
                    should.start_with('NameError: global name')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
