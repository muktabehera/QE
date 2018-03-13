# -*- coding: UTF-8 -*-

"""PFE Component Tests - Origins.

* TC-43976 - Origins GET:

  Verify that error message is displayed on providing non existing 'Id' in 'Id' parameter using request GET /origins{id}.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins/InvalidID"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins/InvalidID"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Origins')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Origins test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43976')
    @pytest.mark.Origins
    @pytest.mark.GET
    def test_TC_43976_GET_Origins_Non_Exist_Id(self, context):
        """TC-43976 - Origins-GET
           Verify that error message is displayed on providing non existing 'Id' in 'Id' parameter using request GET /origins{id}."""

        # Define a test step
        with pytest.allure.step("""Verify that error message is displayed on providing non existing 'Id' in 'Id' parameter using request GET /origins{id}."""):

            # getEntity the Origins, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Origins.getEntity(
                        id='nonexisting'
                    ),
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden, HTTPNotFound) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Delivery Service entity not found')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
