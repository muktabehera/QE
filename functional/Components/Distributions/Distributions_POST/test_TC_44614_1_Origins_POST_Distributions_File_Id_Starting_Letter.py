# -*- coding: UTF-8 -*-

"""PFE Component Tests - Origins.

* TC-44614 - Origins POST:

  Verify that user is able to create Distribution on providing valid value (Starting with  letter or number) in file 'ID' parameter using request POST /distributions .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/origins"

JSON data sent to PathFinder in this test:

  {'baseUris': [{'roles': ['common.httpfetch'],
                 'uri': 'http://10.1.189.27/auto-content/'}],
   'configAdminCanEdit': True,
   'configurations': [{'id': 'default'}],
   'id': 'Auto_storage',
   'name': 'Auto_storage',
   'tokenGenerator': None,
   'visibleInAllConfigurations': False}

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44614')
    @pytest.mark.Origins
    @pytest.mark.POST
    def test_TC_44614_POST_Origins_Distributions_File_Id_Starting_Letter(self, context):
        """TC-44614 - Origins-POST
           Verify that user is able to create Distribution on providing valid value (Starting with  letter or number) in file 'ID' parameter using request POST /distributions ."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create Distribution on providing valid value (Starting with  letter or number) in file 'ID' parameter using request POST /distributions ."""):

            ### Positive test example

            # Test case configuration
            originDetails = context.sc.OriginDetails(
                baseUris=[{
                    'uri': 'http://10.1.189.27/auto-content/',
                    'roles': ['common.httpfetch']
                }],
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'default'
                }],
                id='Auto_storage',
                name='Auto_storage',
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

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is able to create Distribution on providing valid value (Starting with  letter or number) in file 'ID' parameter using request POST /distributions ."""):

            ### Negative test example

            # Test case configuration
            originDetails = context.sc.OriginDetails(
                baseUris=[{
                    'uri': 'http://10.1.189.27/auto-content/',
                    'roles': ['common.httpfetch']
                }],
                configAdminCanEdit=True,
                configurations=[{
                    'id': 'default'
                }],
                id='Auto_storage',
                name='Auto_storage',
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
                    should.start_with('may not be empty'),
                    should.start_with('Invalid page parameter specified'),
                    should.contain('Invalid Authorization Token')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
