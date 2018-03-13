# -*- coding: UTF-8 -*-

"""PFE Component Tests - Settings.

* TC-44434 - Settings GET:

  Verify that setting info is displayed using request GET /settings.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/settings"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/settings"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Settings')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Settings test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44434')
    @pytest.mark.Settings
    @pytest.mark.GET
    def test_TC_44434_GET_Settings_Settings_Verify_Correct_Message_Displayed_Entering_Invalid_Values_Ssl_Enabled_Field(self, context):
        """TC-44434 - Settings-GET
           Verify correct message is displayed on entering invalid values ( 1234,abcd,!@#) in 'sslEnabled' field using request PATCH /settings."""
        # Define a test step
        with pytest.allure.step("""Verify that setting info is displayed using request GET /settings."""):

            # getSettings the Settings.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Settings.getSettings()
            )
