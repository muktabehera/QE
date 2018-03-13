# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44113 - Routes POST:

  Verify that user is able to create route with allowed special characters in ID parameter using POST "/routes".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': True,
   'configurations': [],
   'creationDate': '2016-02-24T10:51:17Z',
   'hops': [{'hops': [],
             'member': {'id': '172.30.3.24', 'name': 'Windows Edge 172.30.3.24'},
             'memberRoles': ['EDGE'],
             'memberType': 'EDGE_DEVICE'}],
   'id': '12BS-s_:x.gh',
   'modificationDate': '2016-02-24T10:51:17Z',
   'name': 'BSRoute11',
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Routes')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Routes test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44113')
    @pytest.mark.Routes
    @pytest.mark.POST
    def test_TC_44113_POST_Routes_Able_To_Create_With_Allowed_Special_Char_Id_Field(self, context):
        """TC-44113 - Routes-POST
           Verify that user is able to create route with allowed special characters in ID parameter using POST "/routes"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create route with allowed special characters in ID parameter using POST "/routes"."""):

            # Test case configuration
            #  ID can be start with number and alphabets
            routeDetails = context.sc.RouteDetails(
                configAdminCanEdit=True,
                configurations=[],
                hops=[],
                id='a-.:123assdsd',
                name='Route9',
                visibleInAllConfigurations=True)


            # createHop the Routes.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Routes.createRoute(
                    body=routeDetails,
                )
            )

