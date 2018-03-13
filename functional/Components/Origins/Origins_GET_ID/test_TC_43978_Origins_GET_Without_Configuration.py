# -*- coding: UTF-8 -*-

"""PFE Component Tests - Origins.

* TC-43978 - Origins GET:

  Verify that user is unable to get the details of 'Configurations' if not provided in origin using request GET /origins{id}.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins/originFTP"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins/originFTP"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Origins')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Origins test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43978')
    @pytest.mark.Origins
    @pytest.mark.GET
    def test_TC_43978_GET_Origins_Without_Configuration(self, context):
        """TC-43978 - Origins-GET
           Verify that user is unable to get the details of 'Configurations' if not provided in origin using request GET /origins{id}."""

        # Define a test step
        with pytest.allure.step("""First create origin with valid 'Id' parameter and no 'Configurations' using request POST/origins."""):
            # Test case configuration
            originDetails = context.sc.OriginDetails(
                baseUris=[{
                    'uri': 'ftp://172.30.2.149/FTP',
                    'roles': ['common.ftpfetch']
                }],
                configAdminCanEdit=True,
                configurations=[],
                id='originGet1',
                name='originGet1',
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
        with pytest.allure.step("""Then verify that user is unable to get the details of 'Configurations' if not provided in origin using request GET /origins{id}."""):

            # listEntities the Origins.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Origins.getEntity(
                    id='originGet1'
                )
            )
