# -*- coding: UTF-8 -*-

"""PFE Component Tests - Authorization_Systems.

* TC-POST - Authorization_Systems POST:

  Id.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/authorizationSystems"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/authorizationSystems"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': True,
   'configurations': [],
   'grantablePermissions': ['manageSystem', 'generate', 'manageConfiguration'],
   'id': 'Authorizationsystem_getID1',
   'macKey': '12345679-89012345678901234566790123456789920000588',
   'name': 'Authorizationsystem_getID1',
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Authorization_Systems')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Authorization_Systems test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-POST')
    @pytest.mark.Authorization_Systems
    @pytest.mark.POST
    def test_TC_POST_POST_Authorization_Systems_Id(self, context):
        """TC-POST - Authorization_Systems-POST
           Id."""
        # Define a test step
        with pytest.allure.step("""Id."""):

            # Test case configuration
            authorizationSystemDetails = context.sc.AuthorizationSystemDetails(
                configAdminCanEdit=True,
                configurations=[],
                grantablePermissions=['manageSystem', 'generate', 'manageConfiguration'],
                id='Authorizationsystem_getID1',
                macKey='12345679-89012345678901234566790123456789920000588',
                name='Authorizationsystem_getID1',
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
