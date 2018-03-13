# -*- coding: UTF-8 -*-

"""PFE Component Tests - Origins.

* TC-44035 - Origins PATCH:

  Verify that user is able to modify origin with parameters (name, configurations, baseUris) using request PATCH /origins.


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
                 'uri': 'file://172.30.2.150/storagee'}],
   'configAdminCanEdit': True,
   'configurations': [{'id': 'default'}],
   'name': 'Origin Updated with Name_Config_BaseUri',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44035')
    @pytest.mark.Origins
    @pytest.mark.PATCH
    def test_TC_44035_PATCH_Origins_Name_Config_Base_Uri(self, context):
        """TC-44035 - Origins-PATCH
           Verify that user is able to modify origin with parameters (name, configurations, baseUris) using request PATCH /origins."""

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
                id='OriginForPatch',
                name='OriginForPatch',
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
        with pytest.allure.step("""Verify that user is able to modify origin with parameters (name, configurations, baseUris) using request PATCH /origins."""):

            # Test case configuration
            originDetails = context.sc.OriginDetails(
                baseUris=[{
                    'uri': 'file://172.30.2.150/storagee',
                    'roles': ['common.filesystemfetch']
                }],
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'default'
                }],
                id=None,
                name='Origin Updated with Name_Config_BaseUri',
                tokenGenerator=None,
                visibleInAllConfigurations=False)


            # updateEntity the Origins.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Origins.updateEntity(
                    id='OriginForPatch',
                    body=originDetails
                )
            )
