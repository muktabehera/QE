# -*- coding: UTF-8 -*-

"""PFE Component Tests - Origins.

* TC-43980 - Origins POST:

  Verify that user is unable to get the details of disabled 'Configurations' using request GET /origins{id}.


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
   'configurations': [{'id': 'default'}],
   'id': 'disbledConfiguration',
   'name': 'Unable To Get Disabled Configuration',
   'tokenGenerator': None,
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Origins')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Origins test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43980')
    @pytest.mark.Origins
    @pytest.mark.POST
    def test_TC_43980_POST_Origins_Disabled_Configuration(self, context):
        """TC-43980 - Origins-POST
           Verify that user is unable to get the details of disabled 'Configurations' using request GET /origins{id}."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to get the details of disabled 'Configurations' using request GET /origins{id}."""):

            ### Positive test example

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
                id='disbledConfiguration',
                name='Unable To Get Disabled Configuration',
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

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is unable to get the details of disabled 'Configurations' using request GET /origins{id}."""):

            ### Negative test example

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
                id='disbledConfiguration',
                name='Unable To Get Disabled Configuration',
                tokenGenerator=None,
                visibleInAllConfigurations=True)


            # prepare the request, so we can modify it
            request = context.cl.Origins.createEntity(
                    body=originDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # createEntity the Origins, and check we got the error we expect
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
