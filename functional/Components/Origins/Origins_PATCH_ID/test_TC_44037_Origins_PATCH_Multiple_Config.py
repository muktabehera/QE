# -*- coding: UTF-8 -*-

"""PFE Component Tests - Origins.

* TC-44037 - Origins PATCH:

  Verify that user is able to modify origin on providing multiple configurations in parameter 'configurations' using request PATCH '/origins'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins/PostOriginsUpdate"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins/PostOriginsUpdate"

JSON data sent to PathFinder in this test:

  {'baseUris': [{'roles': ['common.filesystemfetch'],
                 'uri': 'file://172.30.2.149/storage'}],
   'configAdminCanEdit': True,
   'configurations': [{'id': 'default'}, {'id': 'QA_Test'}],
   'name': 'Origin Updated with multiple config',
   'tokenGenerator': None,
   'visibleInAllConfigurations': False}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Origins')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Origins test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44037')
    @pytest.mark.Origins
    @pytest.mark.PATCH
    def test_TC_44037_PATCH_Origins_Multiple_Config(self, context):
        """TC-44037 - Origins-PATCH
           Verify that user is able to modify origin on providing multiple configurations in parameter 'configurations' using request PATCH '/origins'."""
        # Define a test step
        with pytest.allure.step("""First create origin with valid 'Id' using request POST /origins."""):
            # Test case configuration
            originDetails = context.sc.OriginDetails(
                baseUris=[{
                    'uri': 'ftp://172.30.2.149/FTP',
                    'roles': ['common.ftpfetch']
                }],
                configAdminCanEdit=True,
                configurations=[],
                id='OriginForPatch3',
                name='OriginForPatch3',
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
        with pytest.allure.step("""Then verify that user is able to modify origin on providing multiple configurations in parameter 'configurations' using request PATCH '/origins'."""):

            # Test case configuration
            originDetails = context.sc.OriginDetails(
                baseUris=[{
                    'uri': 'ftp://172.30.2.149/FTP',
                    'roles': ['common.ftpfetch']
                }],
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'default'
                }, {
                    'id': 'QA_Test'
                }],
                id=None,
                name='OriginForPatch3 Origin Updated with multiple config',
                tokenGenerator=None,
                visibleInAllConfigurations=False)


            # updateEntity the Origins.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Origins.updateEntity(
                    id='OriginForPatch3',
                    body=originDetails
                )
            )

