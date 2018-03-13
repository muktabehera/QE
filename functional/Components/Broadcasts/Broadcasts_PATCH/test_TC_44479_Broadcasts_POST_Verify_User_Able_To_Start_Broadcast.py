# -*- coding: UTF-8 -*-

"""PFE Component Tests - Broadcasts.

* TC-44479 - Broadcasts POST:

  Verify that user is able to start the broadcast for live program using request PATCH  "/broadcasts/{id}".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/broadcasts"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/broadcasts"

JSON data sent to PathFinder in this test:

  {'id': 'Broadcast_PatchByID',
   'name': 'Broadcast_PatchByID',
   'streams': [{'connectionPoints': [{'maxConnections': 10000,
                                      'mode': 'PULL',
                                      'url': 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov'}],
                'id': 'stream1',
                'streamMetadata': {'mimeType': 'video/mp4'}}],
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44479')
    @pytest.mark.Broadcasts
    @pytest.mark.POST
    def test_TC_44479_POST_Broadcasts_Verify_User_Able_To_Start_Broadcast(self, context):
        """TC-44479 - Broadcasts-POST
           Verify that user is able to start the broadcast for live program using request PATCH  "/broadcasts/{id}"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to start the broadcast for live program using request PATCH  "/broadcasts/{id}"."""):

            ### Positive test example

            # Test case configuration
            broadcastCreate = context.sc.BroadcastCreate(
                id='Broadcast_PatchByID',
                name='Broadcast_PatchByID',
                protectedContent=None,
                sourceGroups=None,
                streamGroups=None,
                streams=[{
                    'id':
                    'stream1',
                    'streamMetadata': {
                        'mimeType': 'video/mp4'
                    },
                    'connectionPoints': [{
                        'mode':
                        'PULL',
                        'maxConnections':
                        10000,
                        'url':
                        'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov'
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

        with pytest.allure.step("""Verify that user is able to start the broadcast for live program using request PATCH  "/broadcasts/{id}"."""):

            ### Negative test example

            # Test case configuration
            broadcastCreate = context.sc.BroadcastCreate(
                id='Broadcast_PatchByID',
                name='Broadcast_PatchByID',
                protectedContent=None,
                sourceGroups=None,
                streamGroups=None,
                streams=[{
                    'id':
                    'stream1',
                    'streamMetadata': {
                        'mimeType': 'video/mp4'
                    },
                    'connectionPoints': [{
                        'mode':
                        'PULL',
                        'maxConnections':
                        10000,
                        'url':
                        'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov'
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
