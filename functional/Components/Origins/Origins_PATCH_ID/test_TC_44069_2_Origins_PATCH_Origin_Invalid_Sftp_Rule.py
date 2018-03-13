# -*- coding: UTF-8 -*-

"""PFE Component Tests - Origins.

* TC-44069 - Origins PATCH:

  Verify that user is unable to modify origin with 'Secure FTP Download' role on providing invalid 'uri'(file://, http://, ftp://) in parameter 'baseUris' using request PATCH '/origins'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins/PostOriginsUpdate"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins/PostOriginsUpdate"

JSON data sent to PathFinder in this test:

  {'baseUris': [{'roles': ['common.sftpfetch'],
                 'uri': 'ftp://172.30.2.149/storage'}],
   'configAdminCanEdit': True,
   'configurations': [{'id': 'default'}],
   'name': 'Updated Origin with invalid SFTP Rule',
   'tokenGenerator': None,
   'visibleInAllConfigurations': False}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Origins')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Origins test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44069')
    @pytest.mark.Origins
    @pytest.mark.PATCH
    def test_TC_44069_PATCH_Origins_Origin_Invalid_Sftp_Rule(self, context):
        """TC-44069 - Origins-PATCH
           Verify that user is unable to modify origin with 'Secure FTP Download' role on providing invalid 'uri'(file://, http://, ftp://) in parameter 'baseUris' using request PATCH '/origins'."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to modify origin with 'Secure FTP Download' role on providing invalid 'uri'(file://, http://, ftp://) in parameter 'baseUris' using request PATCH '/origins'."""):

            ### Positive test example

            # Test case configuration
            originDetails = context.sc.OriginDetails(
                baseUris=[{
                    'uri': 'ftp://172.30.2.149/storage',
                    'roles': ['common.sftpfetch']
                }],
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'default'
                }],
                id=None,
                name='Updated Origin with invalid SFTP Rule',
                tokenGenerator=None,
                visibleInAllConfigurations=False)


            # updateEntity the Origins.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Origins.updateEntity(
                    body=originDetails
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is unable to modify origin with 'Secure FTP Download' role on providing invalid 'uri'(file://, http://, ftp://) in parameter 'baseUris' using request PATCH '/origins'."""):

            ### Negative test example

            # Test case configuration
            originDetails = context.sc.OriginDetails(
                baseUris=[{
                    'uri': 'ftp://172.30.2.149/storage',
                    'roles': ['common.sftpfetch']
                }],
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'default'
                }],
                id=None,
                name='Updated Origin with invalid SFTP Rule',
                tokenGenerator=None,
                visibleInAllConfigurations=False)


            # prepare the request, so we can modify it
            request = context.cl.Origins.updateEntity(
                    body=originDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateEntity the Origins, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('may not be empty'),
                    should.start_with('Invalid page parameter specified'),
                    should.contain('Invalid Authorization Token')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
