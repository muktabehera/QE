# -*- coding: UTF-8 -*-

"""PFE Component Tests - Origins.

* TC-44028 - Origins POST:

  Verify that user is able to create origin with 'FTP Download' role only after providing valid 'uri'(ftp://) in parameter 'baseUris' using request POST '/origins'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins"

JSON data sent to PathFinder in this test:

  {'baseUris': [{'roles': ['common.ftpfetch'],
                 'uri': 'ftp://172.30.2.149/storage'}],
   'configAdminCanEdit': True,
   'configurations': [{'id': 'default'}],
   'id': 'roleFTP',
   'name': 'Origin with FTP Role',
   'tokenGenerator': None,
   'visibleInAllConfigurations': False}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Origins')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Origins test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44028')
    @pytest.mark.Origins
    @pytest.mark.POST
    def test_TC_44028_POST_Origins_Role_Ftp(self, context):
        """TC-44028 - Origins-POST
           Verify that user is able to create origin with 'FTP Download' role only after providing valid 'uri'(ftp://) in parameter 'baseUris' using request POST '/origins'."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create origin with 'FTP Download' role only after providing valid 'uri'(ftp://) in parameter 'baseUris' using request POST '/origins'."""):

            # Test case configuration
            originDetails = context.sc.OriginDetails(
                baseUris=[{
                    'uri': 'ftp://172.30.2.149/storage',
                    'roles': ['common.ftpfetch']
                }],
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'default'
                }],
                id='roleFTP',
                name='Origin with FTP Role',
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

