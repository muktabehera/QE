# -*- coding: UTF-8 -*-

"""PFE Component Tests - System.

* TC-43954 - System GET:

  Verify that user is able to GET the details of schema versions using  GET system/systemInfo without providing any parameter. .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/system/systemInfo"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/system/systemInfo"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('System')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE System test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43954')
    @pytest.mark.System
    @pytest.mark.GET
    def test_TC_43954_GET_System_System_Info(self, context):
        """TC-43954 - System-GET
           Verify that user is able to GET the details of schema versions using  GET system/systemInfo without providing any parameter. ."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of schema versions using  GET system/systemInfo without providing any parameter. ."""):

            # getSystemInfo the System.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.System.getSystemInfo()
            )

