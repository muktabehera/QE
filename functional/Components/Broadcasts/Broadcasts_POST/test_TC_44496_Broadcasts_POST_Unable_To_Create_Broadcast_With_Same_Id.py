# -*- coding: UTF-8 -*-

"""PFE Component Tests - Broadcasts.

* TC-44496 - Broadcasts POST:

    Verify that user is unable to create broadcast with same ID using request POST "/broadcasts".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/broadcasts"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/broadcasts"

JSON data sent to PathFinder in this test:

  {'id': 'Broadcast_StandaloneVNE_HLS',
   'name': 'Broadcast_StandaloneVNE_HLS',
   'streams': [{'connectionPoints': [{'maxConnections': 10000,
                                      'mode': 'PULL',
                                      'url': 'http://media.blacktrash.org/stsp.m3u8'}],
                'id': 'streheham',
                'streamMetadata': {'mimeType': 'application/vnd.apple.mpegurl'},
                'substreams': [{'relativeUrl': 'stsp/5/288p-lo/pl.m3u8',
                                'usage': 'VARIANTMANIFEST'}]}],
   'targetAudiences': [{'id': 'Broadcast_Standalone_Audience'}]}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Broadcasts')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Broadcasts test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44496')
    @pytest.mark.Broadcasts
    @pytest.mark.POST
    def test_TC_44496_POST_Broadcasts_Unable_To_Create_Broadcast_With_Same_Id(self, context):
        """TC-44496 - Broadcasts-POST
             Verify that user is unable to create broadcast with same ID using request POST "/broadcasts"."""
        # Define a test step
        with pytest.allure.step("""  Verify that user is unable to create broadcast with same ID using request POST "/broadcasts"."""):

            ### Positive test example

            # Test case configuration
            broadcastCreate = context.sc.BroadcastCreate(
                id='Broadcast_StandaloneVNE_HLS',
                name='Broadcast_StandaloneVNE_HLS',
                protectedContent=None,
                sourceGroups=None,
                streamGroups=None,
                streams=[{
                    'id':
                    'streheham',
                    'streamMetadata': {
                        'mimeType': 'application/vnd.apple.mpegurl'
                    },
                    'connectionPoints': [{
                        'mode': 'PULL',
                        'maxConnections': 10000,
                        'url': 'http://media.blacktrash.org/stsp.m3u8'
                    }],
                    'substreams': [{
                        'relativeUrl': 'stsp/5/288p-lo/pl.m3u8',
                        'usage': 'VARIANTMANIFEST'
                    }]
                }],
                tags=None,
                targetAudiences=[{
                    'id': 'Broadcast_Standalone_Audience'
                }])


            # createEntity the Broadcasts.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Broadcasts.createEntity(
                    body=broadcastCreate
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""  Verify that user is unable to create broadcast with same ID using request POST "/broadcasts"."""):

            ### Negative test example

            # Test case configuration
            broadcastCreate = context.sc.BroadcastCreate(
                id='Broadcast_StandaloneVNE_HLS',
                name='Broadcast_StandaloneVNE_HLS',
                protectedContent=None,
                sourceGroups=None,
                streamGroups=None,
                streams=[{
                    'id':
                    'streheham',
                    'streamMetadata': {
                        'mimeType': 'application/vnd.apple.mpegurl'
                    },
                    'connectionPoints': [{
                        'mode': 'PULL',
                        'maxConnections': 10000,
                        'url': 'http://media.blacktrash.org/stsp.m3u8'
                    }],
                    'substreams': [{
                        'relativeUrl': 'stsp/5/288p-lo/pl.m3u8',
                        'usage': 'VARIANTMANIFEST'
                    }]
                }],
                tags=None,
                targetAudiences=[{
                    'id': 'Broadcast_Standalone_Audience'
                }])


            # prepare the request, so we can modify it
            request = context.cl.Broadcasts.createEntity(
                    body=broadcastCreate
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # createEntity the Broadcasts, and check we got the error we expect
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
