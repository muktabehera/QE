# -*- coding: UTF-8 -*-

"""PFE Component Tests - Origins.

* TC-44014 - Origins POST:

  Verify that user is able to create origin with valid values for parameters 'id' using request POST /origins.


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
   'id': 'PostID',
   'name': 'Valid ID1',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44014')
    @pytest.mark.Origins
    @pytest.mark.POST
    def test_TC_44014_POST_Origins_Origin_Valid_Id(self, context):
        """TC-44014 - Origins-POST
           Verify that user is able to create origin with valid values for parameters 'id' using request POST /origins."""
        # Define a test step
        with pytest.allure.step("""Test1: Verify that user is able to create origin with valid values for parameters 'id' using request POST /origins."""):

            # Test case configuration
            originDetails = context.sc.OriginDetails(
                baseUris=[{
                    'uri': 'ftp://172.30.2.149/FTP',
                    'roles': ['common.ftpfetch']
                }],
                configAdminCanEdit=True,
                configurations=[],
                id='PostID',
                name='Valid ID1',
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
        with pytest.allure.step("""Test2: Verify that user is able to create origin with valid values for parameters 'id' using request POST /origins."""):

            # Test case configuration
            originDetails = context.sc.OriginDetails(
                baseUris=[{
                    'uri': 'ftp://172.30.2.149/FTP',
                    'roles': ['common.ftpfetch']
                }],
                configAdminCanEdit=True,
                configurations=[],
                id='P2OST123',
                name='Valid ID2',
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
        with pytest.allure.step("""Test3: Verify that user is able to create origin with valid values for parameters 'id' using request POST /origins."""):

            # Test case configuration
            originDetails = context.sc.OriginDetails(
                baseUris=[{
                    'uri': 'ftp://172.30.2.149/FTP',
                    'roles': ['common.ftpfetch']
                }],
                configAdminCanEdit=True,
                configurations=[],
                id='123456',
                name='Valid ID3',
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
        with pytest.allure.step("""Test4: Verify that user is able to create origin with valid values for parameters 'id' using request POST /origins."""):

            # Test case configuration
            originDetails = context.sc.OriginDetails(
                baseUris=[{
                    'uri': 'ftp://172.30.2.149/FTP',
                    'roles': ['common.ftpfetch']
                }],
                configAdminCanEdit=True,
                configurations=[],
                id='POST_123:-.',
                name='Valid ID4',
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
        with pytest.allure.step("""Test5: Verify that user is able to create origin with valid values for parameters 'id' using request POST /origins."""):

            # Test case configuration
            originDetails = context.sc.OriginDetails(
                baseUris=[{
                    'uri': 'ftp://172.30.2.149/FTP',
                    'roles': ['common.ftpfetch']
                }],
                configAdminCanEdit=True,
                configurations=[],
                id='A_:-.',
                name='Valid ID5',
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
        with pytest.allure.step("""Test6: Verify that user is able to create origin with valid values for parameters 'id' using request POST /origins."""):

            # Test case configuration
            originDetails = context.sc.OriginDetails(
                baseUris=[{
                    'uri': 'ftp://172.30.2.149/FTP',
                    'roles': ['common.ftpfetch']
                }],
                configAdminCanEdit=True,
                configurations=[],
                id='12Client',
                name='Valid ID6',
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
