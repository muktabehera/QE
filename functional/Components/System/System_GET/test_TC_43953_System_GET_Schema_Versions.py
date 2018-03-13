# -*- coding: UTF-8 -*-

"""PFE Component Tests - System.

* TC-43953 - System GET:

  Verify that user is able to GET the details of schema versions using  GET system/schemaVersions without providing any parameter. .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/system/schemaVersions"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/system/schemaVersions"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('System')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE System test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43953')
    @pytest.mark.System
    @pytest.mark.GET
    def test_TC_43953_GET_System_Schema_Versions(self, context):
        """TC-43953 - System-GET
           Verify that user is able to GET the details of schema versions using  GET system/schemaVersions without providing any parameter. ."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of schema versions using  GET system/schemaVersions without providing any parameter. ."""):

            # getSchemaVersion the System.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.System.getSchemaVersion()
            )
