# -*- coding: UTF-8 -*-

"""PFE Component Tests - Settings.

* TC-44431 - Settings PATCH:

  Verify user is unable to modify the settings on entering invalid values ( 1234,abcd,!@#) in 'configured' field using request PATCH /settings.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/settings"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/settings"

JSON data sent to PathFinder in this test:

  {'configured': 1234,
   'hostname': 'localhost',
   'port': 8080,
   'sslEnabled': False,
   'sslPort': 8443}

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44431')
    @pytest.mark.Settings
    @pytest.mark.PATCH
    def test_TC_44431_PATCH_Settings_Settings_Unable_To_Modify_Using_Invalid_Values_Configured_Field(self, context):
        """TC-44431 - Settings-PATCH
           Verify user is unable to modify the settings on entering invalid values ( 1234,abcd,!@#) in 'configured' field using request PATCH /settings."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify user is able to modify the settings on entering values (1234) in 'configured' field using request PATCH /settings."""):

            ### As per QED-1011 "Integer 0 is treated as false, integer value greater than 0 is treated as true."

            # Test case configuration
            settingsDetails = context.sc.SettingsDetails(
                configured=1234,
                hostname='localhost',
                port=8080,
                sslEnabled=False,
                sslPort=8443)

            # updateSettings the Settings.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Settings.updateSettings(
                    body=settingsDetails
                )
            )


        # Define a test step
        with pytest.allure.step("""Test2: Verify user is unable to modify the settings on entering invalid values (abcd) in 'configured' field using request PATCH /settings."""):

            # Test case configuration
            settingsDetails = context.sc.SettingsDetails(
                configured=abcd,
                hostname='localhost',
                port=8080,
                sslEnabled=False,
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
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Unrecognized token'),
                    should.start_with('NameError: global name')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))



        # Define a test step
        with pytest.allure.step("""Test3: Verify user is unable to modify the settings on entering invalid values (!@#) in 'configured' field using request PATCH /settings."""):

            # Test case configuration
            settingsDetails = context.sc.SettingsDetails(
                configured="!@#",
                hostname='localhost',
                port=8080,
                sslEnabled=False,
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
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Unrecognized token'),
                    should.start_with('NameError: global name')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
