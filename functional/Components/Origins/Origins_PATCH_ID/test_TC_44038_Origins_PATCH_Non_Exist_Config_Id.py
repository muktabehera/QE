# -*- coding: UTF-8 -*-

"""PFE Component Tests - Origins.

* TC-44038 - Origins PATCH:

  Verify that correct message is displayed in response on modifying origin with non-existing 'id' in 'configuration' parameter using request PATCH '/origins'.


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
   'configurations': [{'id': 'default123'}],
   'name': 'Origin Updated with Non Exist Config Id',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44038')
    @pytest.mark.Origins
    @pytest.mark.PATCH
    def test_TC_44038_PATCH_Origins_Non_Exist_Config_Id(self, context):
        """TC-44038 - Origins-PATCH
           Verify that correct message is displayed in response on modifying origin with non-existing 'id' in 'configuration' parameter using request PATCH '/origins'."""
        # Define a test step
        with pytest.allure.step("""Verify that correct message is displayed in response on modifying origin with non-existing 'id' in 'configuration' parameter using request PATCH '/origins'."""):

            # Test case configuration
            originDetails = context.sc.OriginDetails(
                baseUris=[{
                    'uri': 'file://172.30.2.150/storagee',
                    'roles': ['common.filesystemfetch']
                }],
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'default123'
                }],
                id=None,
                name='Origin Updated with Non Exist Config Id',
                tokenGenerator=None,
                visibleInAllConfigurations=False)


            # prepare the request, so we can modify it
            request = context.cl.Origins.updateEntity(
                    id='OriginForPatch',
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
                    should.start_with('Invalid configuration identifier')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
