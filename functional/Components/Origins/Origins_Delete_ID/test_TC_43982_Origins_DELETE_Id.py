# -*- coding: UTF-8 -*-

"""PFE Component Tests - Origins.

* TC-43982 - Origins DELETE:

  Verify that user is able to delete the origin on providing 'Id' parameter using request DELETE /origins{id}.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins/originDeletee"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X DELETE -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins/originDeletee"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Origins')
@pytest.allure.feature('DELETE')
class Test_PFE_Components(object):
    """PFE Origins test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43982')
    @pytest.mark.Origins
    @pytest.mark.DELETE
    def test_TC_43982_DELETE_Origins_Id(self, context):
        """TC-43982 - Origins-DELETE
           Verify that user is able to delete the origin on providing 'Id' parameter using request DELETE /origins{id}."""

        # Define a test step
        with pytest.allure.step("""First create origin with valid 'Id' parameter using request POST/origins."""):

            # Test case configuration
            originDetails = context.sc.OriginDetails(
                baseUris=[{
                    'uri': 'ftp://172.30.2.149/FTP',
                    'roles': ['common.ftpfetch']
                }],
                configAdminCanEdit=True,
                configurations=[],
                id='originDeletee',
                name='Delete Origin',
                tokenGenerator=None,
                visibleInAllConfigurations=True)

            # createEntity the Origins.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Origins.createEntity(
                    body=originDetails
                )
            )

        # Define a test step
        with pytest.allure.step("""Now verify that user is able to delete the origin on providing 'Id' parameter using request DELETE /origins{id}."""):

            # deleteEntity the Origins.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Origins.deleteEntity(
                    id='originDeletee'
                )
            )

