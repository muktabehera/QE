# -*- coding: UTF-8 -*-

"""PFE Component Tests - Authorization_Systems.

* TC-43336 - Authorization_Systems POST:

  Verify that user is able to create Authorization System having Max length of 100 characters in ID with using request POST /authorizationSystems.


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
   'grantablePermissions': ['manageSystem',
                            'matchAny',
                            'provision',
                            'match',
                            'distribute',
                            'generate',
                            'manageConfiguration'],
   'id': 'POST_authorizationSystem_withLengthMax100ForIDfieldPOST_authorizationSystem_withLengthMax100ForIDfie',
   'macKey': '12345689713265487923156234497813265489712654897',
   'name': 'POST_authorizationSystem_withLengthMax100ForIDfield',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43336')
    @pytest.mark.Authorization_Systems
    @pytest.mark.POST
    def test_TC_43336_POST_Authorization_Systems_With_Length_Max_100_For_Idfield(self, context):
        """TC-43336 - Authorization_Systems-POST
           Verify that user is able to create Authorization System having Max length of 100 characters in ID with using request POST /authorizationSystems."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create Authorization System having Max length of 100 characters in ID with using request POST /authorizationSystems."""):

            # Test case configuration
            authorizationSystemDetails = context.sc.AuthorizationSystemDetails(
                configAdminCanEdit=True,
                configurations=[],
                grantablePermissions=[
                    'manageSystem', 'matchAny', 'provision', 'match', 'distribute',
                    'generate', 'manageConfiguration'
                ],
                id=
                'POST_authorizationSystem_withLengthMax100ForIDfieldPOST_authorizationSystem_withLengthMax100ForIDfie',
                macKey='12345689713265487923156234497813265489712654897',
                name='POST_authorizationSystem_withLengthMax100ForIDfield',
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

