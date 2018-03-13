# -*- coding: UTF-8 -*-

"""PFE Component Tests - Origins.

* TC-44004 - Origins POST:

  Verify that correct message is displayed in response on providing non-existing "Configuration" id in parameter 'configurations' using request POST '/origins'.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins"

JSON data sent to PathFinder in this test:

  {'baseUris': [{'roles': ['common.filesystemfetch'],
                 'uri': 'file://172.30.2.149/storage'}],
   'configAdminCanEdit': True,
   'configurations': [{'id': 'idnotExists'}],
   'id': 'confnotExists',
   'name': 'Origin with configuration id Not Exist',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44004')
    @pytest.mark.Origins
    @pytest.mark.POST
    def test_TC_44004_POST_Origins_Configuration_Idnot_Exist(self, context):
        """TC-44004 - Origins-POST
           Verify that correct message is displayed in response on providing non-existing "Configuration" id in parameter 'configurations' using request POST '/origins'."""
        # Define a test step
        with pytest.allure.step("""Verify that correct message is displayed in response on providing non-existing "Configuration" id in parameter 'configurations' using request POST '/origins'."""):

            # Test case configuration
            originDetails = context.sc.OriginDetails(
                baseUris=[{
                    'uri': 'file://172.30.2.149/storage',
                    'roles': ['common.filesystemfetch']
                }],
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'idnotExists'
                }],
                id='confnotExists',
                name='Origin with configuration id Not Exist',
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
                    should.start_with('Invalid configuration identifier')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
