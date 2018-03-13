# -*- coding: UTF-8 -*-

"""PFE Component Tests - Settings.

* TC-44447 - Settings PATCH:

  Verify correct error message is displayed on entering more than 100 characters in hostname field using request PATCH /settings.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/settings"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/settings"

JSON data sent to PathFinder in this test:

  {'configured': True,
   'hostname': 'aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddee1',
   'port': 8080,
   'sslEnabled': True,
   'sslPort': 8443}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Settings')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Settings test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44447')
    @pytest.mark.Settings
    @pytest.mark.PATCH
    def test_TC_44447_PATCH_Settings_Verify_Correct_Message_Displayed_On_Entering_More_Than_100_Characters_In_Hostname_Field(self, context):
        """TC-44447 - Settings-PATCH
           Verify correct error message is displayed on entering more than 100 characters in hostname field using request PATCH /settings."""
        # Define a test step
        with pytest.allure.step("""Verify correct error message is displayed on entering more than 100 characters in hostname field using request PATCH /settings."""):

            # Test case configuration
            settingsDetails = context.sc.SettingsDetails(
                configured=True,
                hostname=
                'aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddee1',
                port=8080,
                sslEnabled=True,
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
            except (HTTPBadRequest, HTTPForbidden, HTTPConflict) as e:        # 400, 403, 409 error
                get_error_message(e) | expect.any(
                    should.start_with('Constraint violation. PATCH on /settings resource failed.')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
