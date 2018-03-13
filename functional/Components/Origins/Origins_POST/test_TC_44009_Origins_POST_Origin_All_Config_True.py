# -*- coding: UTF-8 -*-

"""PFE Component Tests - Origins.

* TC-44009 - Origins POST:

  Verify that user is able to create origin on providing 'visibleInAllConfigurations' parameter as 'true/false/null' using request POST '/origins'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins"

JSON data sent to PathFinder in this test:

  {'baseUris': [{'roles': ['common.ftpfetch'], 'uri': 'ftp://172.30.2.149/FTP'}],
   'configAdminCanEdit': True,
   'configurations': [],
   'id': 'AllConfigTrue',
   'name': 'Origin with All Configuration True',
   'tokenGenerator': None,
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Origins')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Origins test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44009')
    @pytest.mark.Origins
    @pytest.mark.POST
    def test_TC_44009_POST_Origins_Origin_All_Config_True(self, context):
        """TC-44009 - Origins-POST
           Verify that user is able to create origin on providing 'visibleInAllConfigurations' parameter as 'true/false/null' using request POST '/origins'."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create origin on providing 'visibleInAllConfigurations' parameter as 'true' using request POST '/origins'."""):

            # Test case configuration
            originDetails = context.sc.OriginDetails(
                baseUris=[{
                    'uri': 'ftp://172.30.2.149/FTP',
                    'roles': ['common.ftpfetch']
                }],
                configAdminCanEdit=True,
                configurations=[],
                id='AllConfigTrue',
                name='Origin with All Configuration True',
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
        with pytest.allure.step("""Verify that user is able to create origin on providing 'visibleInAllConfigurations' parameter as 'false' using request POST '/origins'."""):

            # Test case configuration
            originDetails = context.sc.OriginDetails(
                baseUris=[{
                    'uri': 'ftp://172.30.2.149/FTP',
                    'roles': ['common.ftpfetch']
                }],
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'default'
                }],
                id='AllConfigFalse',
                name='Origin with All Configuration False',
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
        with pytest.allure.step("""Verify that user is able to create origin on providing 'visibleInAllConfigurations' parameter as 'null' using request POST '/origins'."""):

            # Test case configuration
            originDetails = context.sc.OriginDetails(
                baseUris=[{
                    'uri': 'ftp://172.30.2.149/FTP',
                    'roles': ['common.ftpfetch']
                }],
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'default'
                }],
                id='AllConfigNull',
                name='Origin with All Configuration Null',
                tokenGenerator=None,
                visibleInAllConfigurations=None)


            # createEntity the Origins.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Origins.createEntity(
                    body=originDetails
                )
            )
