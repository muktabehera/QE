# -*- coding: UTF-8 -*-

"""PFE Component Tests - Origins.

* TC-43981 - Origins DELETE:

  Verify that correct error message is displayed on providing non existing 'Id' in 'id' parameter using request DELETE /origins{id}.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins/deleteNonExist"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins/deleteNonExist"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Origins')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Origins test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43981')
    @pytest.mark.Origins
    @pytest.mark.DELETE
    def test_TC_43981_DELETE_Origins_Non_Exist_Id(self, context):
        """TC-43981 - Origins-DELETE
           Verify that correct error message is displayed on providing non existing 'Id' in 'id' parameter using request DELETE /origins{id}."""
        # Define a test step
        with pytest.allure.step("""Verify that correct error message is displayed on providing non existing 'Id' in 'id' parameter using request DELETE /origins{id}."""):

            # deleteEntity the Origins, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Origins.deleteEntity(
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
