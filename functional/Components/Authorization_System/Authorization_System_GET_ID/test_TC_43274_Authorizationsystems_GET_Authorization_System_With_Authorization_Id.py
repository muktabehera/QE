# -*- coding: UTF-8 -*-

"""PFE Component Tests - Authorization_Systems.

* TC-43274 - Authorization_Systems GET:

  Verify that user is able to GET the details of Authorization system using request  /authorizationSystems/{id} using Authorization ID.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/authorizationSystems/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/authorizationSystems/Authorizationsystem_getID1"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Authorization_Systems')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Authorization_Systems test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43274')
    @pytest.mark.Authorization_Systems
    @pytest.mark.GET
    def test_TC_43274_GET_Authorization_Systems_Authorization_System_With_Authorization_Id(self, context):
        """TC-43274 - Authorization_Systems-GET
           Verify that user is able to GET the details of Authorization system using request  /authorizationSystems/{id} using Authorization ID."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of Authorization system using request  /authorizationSystems/{id} using Authorization ID."""):


            # getEntity the Authorization_Systems.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Authorization_Systems.getEntity(
                    id='Authorizationsystem_getID1')
            )

