# -*- coding: UTF-8 -*-

"""PFE Component Tests - System.

* TC-43952 - System GET:

  Verify that user is able to GET the details of build info using  GET system/buildInfo without providing any parameter.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/system/buildInfo"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/system/buildInfo"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('System')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE System test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43952')
    @pytest.mark.System
    @pytest.mark.GET
    def test_TC_43952_GET_System_Systembuild_Info_Without_Parameter(self, context):
        """TC-43952 - System-GET
           Verify that user is able to GET the details of build info using  GET system/buildInfo without providing any parameter."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of build info using  GET system/buildInfo without providing any parameter."""):

            # getBuildInfo the System.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.System.getBuildInfo()
            )

