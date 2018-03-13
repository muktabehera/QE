# -*- coding: UTF-8 -*-

"""PFE Component Tests - Authorization_Systems.

* TC-43276 - Authorization_Systems GET:

  Verify that user is able to GET the details of  Authorization system having id with 100 characters using request  /authorizationSystems/{id} .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/authorizationSystems/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/authorizationSystems/Authorizationsystem_getID1_with100CharactersValueinIDfieldAuthorizationsystem_getID1_with100Characte"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Authorization_Systems')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Authorization_Systems test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43276')
    @pytest.mark.Authorization_Systems
    @pytest.mark.GET
    def test_TC_43276_GET_Authorization_Systems_Authorization_System_With_Id_Value_100_Characters(self, context):
        """TC-43276 - Authorization_Systems-GET
           Verify that user is able to GET the details of  Authorization system having id with 100 characters using request  /authorizationSystems/{id} ."""
        # Define a test step
        with pytest.allure.step("""First Create Authorization System With 100 Characters In Id Field."""):

            # Test case configuration
            authorizationSystemDetails = context.sc.AuthorizationSystemDetails(
                configAdminCanEdit=True,
                configurations=[],
                grantablePermissions=['manageSystem', 'generate', 'manageConfiguration'],
id='TESTAuthorizationsystem_getID1_with100CharactersValueinIDfieldAuthorizationsystem_getID1_with100Char',
                macKey='12345679-89012345678901234566790123456789920000588',
                name='Authorizationsystem_getID1_with100Characters',
                visibleInAllConfigurations=True)


            # createEntity the Authorization_Systems.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Authorization_Systems.createEntity(
                    body=authorizationSystemDetails
                )
            )

        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of  Authorization system having id with 100 characters using request  /authorizationSystems/{id} ."""):

            # getEntity the Authorization_Systems.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Authorization_Systems.getEntity(
                    id='TESTAuthorizationsystem_getID1_with100CharactersValueinIDfieldAuthorizationsystem_getID1_with100Char')
            )

