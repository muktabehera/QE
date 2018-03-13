# -*- coding: UTF-8 -*-

"""PFE Component Tests - Origins.

* TC-44007 - Origins POST:

  Verify that correct message is displayed in response on providing 'Configurations' parameter as empty and 'visibleInAllConfigurations' parameter as 'false' using request POST '/origins'.


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
   'id': 'empty',
   'name': 'Origin without config and AllConfig',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44007')
    @pytest.mark.Origins
    @pytest.mark.POST
    def test_TC_44007_POST_Origins_Config_Empty_All_Config_False(self, context):
        """TC-44007 - Origins-POST
           Verify that correct message is displayed in response on providing 'Configurations' parameter as empty and 'visibleInAllConfigurations' parameter as 'false' using request POST '/origins'."""
        # Define a test step
        with pytest.allure.step("""Verify that correct message is displayed in response on providing 'Configurations' parameter as empty and 'visibleInAllConfigurations' parameter as 'false' using request POST '/origins'."""):

            # Test case configuration
            originDetails = context.sc.OriginDetails(
                baseUris=[{
                    'uri': 'ftp://172.30.2.149/FTP',
                    'roles': ['common.ftpfetch']
                }],
                configAdminCanEdit=True,
                configurations=[],
                id='empty',
                name='Origin without config and AllConfig',
                tokenGenerator=None,
                visibleInAllConfigurations=False)


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
                    should.start_with('Either provide the configurations where the system resource is visible or mark it visible in all configurations')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
