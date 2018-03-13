# -*- coding: UTF-8 -*-

"""PFE Component Tests - Settings.

* TC-44531 - Settings PATCH:

  Verify that user is able to GET the response from the server when sslEnabled= false using request PATCH /setting.


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
   'hostname': 'localhost',
   'port': 8080,
   'sslEnabled': False,
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44531')
    @pytest.mark.Settings
    @pytest.mark.PATCH
    def test_TC_44531_PATCH_Settings_Unable_To_Get_Response_Ssl_Enabled_False(self, context):
        """TC-44531 - Settings-PATCH
           Verify that user is able to GET the response from the server when sslEnabled= false using request PATCH /setting."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the response from the server when sslEnabled= false using request PATCH /setting."""):

            # Test case configuration
            settingsDetails = context.sc.SettingsDetails(
                configured=True,
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
