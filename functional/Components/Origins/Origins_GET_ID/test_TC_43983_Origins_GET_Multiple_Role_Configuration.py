# -*- coding: UTF-8 -*-

"""PFE Component Tests - Origins.

* TC-43983 - Origins GET:

  Verify that user is able to get the origin with multiple 'Configurations' and 'Roles' using request GET /origins{id}.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins/multipleRoles_Configuration"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins/multipleRoles_Configuration"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Origins')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Origins test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43983')
    @pytest.mark.Origins
    @pytest.mark.GET
    def test_TC_43983_GET_Origins_Multiple_Role_Configuration(self, context):
        """TC-43983 - Origins-GET
           Verify that user is able to get the origin with multiple 'Configurations' and 'Roles' using request GET /origins{id}."""

        # Define a test step
        with pytest.allure.step("""First create origin with multiple roles(HTTP, FTP Download, FTP Secure Download, FSA) and multiple configurations using request POST '/origins'."""):

            # Test case configuration
            originDetails = context.sc.OriginDetails(
                baseUris=[{
                    'uri': 'file://172.30.2.149/storage',
                    'roles': ['common.filesystemfetch']
                }, {
                    'uri': 'sftp://172.30.2.149/storage',
                    'roles': ['common.sftpfetch']
                }, {
                    'uri': 'http://172.30.2.149/storage',
                    'roles': ['common.httpfetch']
                }, {
                    'uri': 'ftp://172.30.2.149/storage',
                    'roles': ['common.ftpfetch']
                }],
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'QA_Test'
                }, {
                    'id': 'default'
                }],
                id='multiRolesandconfig',
                name='multiRolesandconfig',
                tokenGenerator=None,
                visibleInAllConfigurations=False)

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
        with pytest.allure.step("""Verify that user is able to get the origin with multiple 'Configurations' and 'Roles' using request GET /origins{id}."""):

            # listEntities the Origins.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Origins.getEntity(
                    id='multiRolesandconfig'
                )
            )
