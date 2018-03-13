# -*- coding: UTF-8 -*-

"""PFE Component Tests - Distributions.

* TC-43217 - Distributions POST:

  Verify that user is able to send adaptive streaming media file(HLS) for distribution  with "streamMetadata"using request POST "/distributions" with VideoNet.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/distributions"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/distributions"

JSON data sent to PathFinder in this test:

  {'activationDate': '2017-09-04T07:36:46.542Z',
   'distributionPolicy': 'REQUIRED',
   'files': [{'auxiliaryFiles': [{'relativeUrl': 'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_1.m3u8',
                                  'streamMetadata': {'bitrateKbps': 2185,
                                                     'contentType': 'UNSPECIFIED',
                                                     'height': 250,
                                                     'lang': None,
                                                     'mimeType': 'application/vnd.apple.mpegurl',
                                                     'tags': {},
                                                     'width': 300},
                                  'usage': 'STREAMMANIFEST'},
                                 {'relativeUrl': 'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_1/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_10.ts',
                                  'streamMetadata': {'bitrateKbps': 2185,
                                                     'contentType': 'UNSPECIFIED',
                                                     'height': 250,
                                                     'lang': None,
                                                     'mimeType': None,
                                                     'tags': {},
                                                     'width': 300},
                                  'usage': None},
                                 {'relativeUrl': 'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_1/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_11.ts',
                                  'streamMetadata': {'bitrateKbps': 2185,
                                                     'contentType': 'UNSPECIFIED',
                                                     'height': 250,
                                                     'lang': None,
                                                     'mimeType': None,
                                                     'tags': {},
                                                     'width': 300},
                                  'usage': None},
                                 {'relativeUrl': 'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_1/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_12.ts',
                                  'streamMetadata': {'bitrateKbps': 2185,
                                                     'contentType': 'UNSPECIFIED',
                                                     'height': 250,
                                                     'lang': None,
                                                     'mimeType': None,
                                                     'tags': {},
                                                     'width': 300},
                                  'usage': None},
                                 {'relativeUrl': 'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2.m3u8',
                                  'streamMetadata': {'bitrateKbps': 3185,
                                                     'contentType': 'UNSPECIFIED',
                                                     'height': 250,
                                                     'lang': None,
                                                     'mimeType': 'application/vnd.apple.mpegurl',
                                                     'tags': {},
                                                     'width': 600},
                                  'usage': 'STREAMMANIFEST'},
                                 {'relativeUrl': 'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_20.ts',
                                  'streamMetadata': {'bitrateKbps': 2185,
                                                     'contentType': 'UNSPECIFIED',
                                                     'height': 250,
                                                     'lang': None,
                                                     'mimeType': None,
                                                     'tags': {},
                                                     'width': 300},
                                  'usage': None},
                                 {'relativeUrl': 'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_21.ts',
                                  'streamMetadata': {'bitrateKbps': 2185,
                                                     'contentType': 'UNSPECIFIED',
                                                     'height': 250,
                                                     'lang': None,
                                                     'mimeType': None,
                                                     'tags': {},
                                                     'width': 300},
                                  'usage': None},
                                 {'relativeUrl': 'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_22.ts',
                                  'streamMetadata': {'bitrateKbps': 2185,
                                                     'contentType': 'UNSPECIFIED',
                                                     'height': 250,
                                                     'lang': None,
                                                     'mimeType': None,
                                                     'tags': {},
                                                     'width': 300},
                                  'usage': None}],
              'id': 'HLS2',
              'sourceUrl': 'qedorigin://Auto_storage/HLS2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_Master.m3u8',
              'streamMetadata': {'mimeType': 'application/vnd.apple.mpegurl'}}],
   'id': 'adaptiveHLSStreamMetaData',
   'name': 'Distribution with stream meta data',
   'targetAudiences': [{'id': 'Broadcast_Videonet_Audience'}]}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Distributions')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Distributions test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43217')
    @pytest.mark.Distributions
    @pytest.mark.POST
    def test_TC_43217_POST_Distributions_Vnet_Stream_Meta_Hls(self, context):
        """TC-43217 - Distributions-POST
           Verify that user is able to send adaptive streaming media file(HLS) for distribution  with "streamMetadata"using request POST "/distributions" with VideoNet."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to send adaptive streaming media file(HLS) for distribution  with "streamMetadata"using request POST "/distributions" with VideoNet."""):

            ### Positive test example

            # Test case configuration
            distributionDetails = context.sc.DistributionDetails(
                activationDate='2017-09-04T07:36:46.542Z',
                distributionPolicy='REQUIRED',
                expirationDate=None,
                files=[{
                    'id':
                    'HLS2',
                    'sourceUrl':
                    'qedorigin://Auto_storage/HLS2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_Master.m3u8',
                    'streamMetadata': {
                        'mimeType': 'application/vnd.apple.mpegurl'
                    },
                    'auxiliaryFiles': [{
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_1.m3u8',
                        'usage':
                        'STREAMMANIFEST',
                        'streamMetadata': {
                            'bitrateKbps': 2185,
                            'width': 300,
                            'height': 250,
                            'mimeType': 'application/vnd.apple.mpegurl',
                            'lang': None,
                            'tags': {},
                            'contentType': 'UNSPECIFIED'
                        }
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_1/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_10.ts',
                        'usage':
                        None,
                        'streamMetadata': {
                            'bitrateKbps': 2185,
                            'width': 300,
                            'height': 250,
                            'mimeType': None,
                            'lang': None,
                            'tags': {},
                            'contentType': 'UNSPECIFIED'
                        }
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_1/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_11.ts',
                        'usage':
                        None,
                        'streamMetadata': {
                            'bitrateKbps': 2185,
                            'width': 300,
                            'height': 250,
                            'mimeType': None,
                            'lang': None,
                            'tags': {},
                            'contentType': 'UNSPECIFIED'
                        }
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_1/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_12.ts',
                        'usage':
                        None,
                        'streamMetadata': {
                            'bitrateKbps': 2185,
                            'width': 300,
                            'height': 250,
                            'mimeType': None,
                            'lang': None,
                            'tags': {},
                            'contentType': 'UNSPECIFIED'
                        }
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2.m3u8',
                        'usage':
                        'STREAMMANIFEST',
                        'streamMetadata': {
                            'bitrateKbps': 3185,
                            'width': 600,
                            'height': 250,
                            'mimeType': 'application/vnd.apple.mpegurl',
                            'lang': None,
                            'tags': {},
                            'contentType': 'UNSPECIFIED'
                        }
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_20.ts',
                        'usage':
                        None,
                        'streamMetadata': {
                            'bitrateKbps': 2185,
                            'width': 300,
                            'height': 250,
                            'mimeType': None,
                            'lang': None,
                            'tags': {},
                            'contentType': 'UNSPECIFIED'
                        }
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_21.ts',
                        'usage':
                        None,
                        'streamMetadata': {
                            'bitrateKbps': 2185,
                            'width': 300,
                            'height': 250,
                            'mimeType': None,
                            'lang': None,
                            'tags': {},
                            'contentType': 'UNSPECIFIED'
                        }
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_22.ts',
                        'usage':
                        None,
                        'streamMetadata': {
                            'bitrateKbps': 2185,
                            'width': 300,
                            'height': 250,
                            'mimeType': None,
                            'lang': None,
                            'tags': {},
                            'contentType': 'UNSPECIFIED'
                        }
                    }]
                }],
                id='adaptiveHLSStreamMetaData',
                name='Distribution with stream meta data',
                status=None,
                tags=None,
                targetAudiences=[{
                    'id': 'Broadcast_Videonet_Audience'
                }])


            # createEntity the Distributions.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Distributions.createEntity(
                    body=distributionDetails
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is able to send adaptive streaming media file(HLS) for distribution  with "streamMetadata"using request POST "/distributions" with VideoNet."""):

            ### Negative test example

            # Test case configuration
            distributionDetails = context.sc.DistributionDetails(
                activationDate='2017-09-04T07:36:46.542Z',
                distributionPolicy='REQUIRED',
                expirationDate=None,
                files=[{
                    'id':
                    'HLS2',
                    'sourceUrl':
                    'qedorigin://Auto_storage/HLS2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_Master.m3u8',
                    'streamMetadata': {
                        'mimeType': 'application/vnd.apple.mpegurl'
                    },
                    'auxiliaryFiles': [{
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_1.m3u8',
                        'usage':
                        'STREAMMANIFEST',
                        'streamMetadata': {
                            'bitrateKbps': 2185,
                            'width': 300,
                            'height': 250,
                            'mimeType': 'application/vnd.apple.mpegurl',
                            'lang': None,
                            'tags': {},
                            'contentType': 'UNSPECIFIED'
                        }
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_1/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_10.ts',
                        'usage':
                        None,
                        'streamMetadata': {
                            'bitrateKbps': 2185,
                            'width': 300,
                            'height': 250,
                            'mimeType': None,
                            'lang': None,
                            'tags': {},
                            'contentType': 'UNSPECIFIED'
                        }
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_1/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_11.ts',
                        'usage':
                        None,
                        'streamMetadata': {
                            'bitrateKbps': 2185,
                            'width': 300,
                            'height': 250,
                            'mimeType': None,
                            'lang': None,
                            'tags': {},
                            'contentType': 'UNSPECIFIED'
                        }
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_1/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_12.ts',
                        'usage':
                        None,
                        'streamMetadata': {
                            'bitrateKbps': 2185,
                            'width': 300,
                            'height': 250,
                            'mimeType': None,
                            'lang': None,
                            'tags': {},
                            'contentType': 'UNSPECIFIED'
                        }
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2.m3u8',
                        'usage':
                        'STREAMMANIFEST',
                        'streamMetadata': {
                            'bitrateKbps': 3185,
                            'width': 600,
                            'height': 250,
                            'mimeType': 'application/vnd.apple.mpegurl',
                            'lang': None,
                            'tags': {},
                            'contentType': 'UNSPECIFIED'
                        }
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_20.ts',
                        'usage':
                        None,
                        'streamMetadata': {
                            'bitrateKbps': 2185,
                            'width': 300,
                            'height': 250,
                            'mimeType': None,
                            'lang': None,
                            'tags': {},
                            'contentType': 'UNSPECIFIED'
                        }
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_21.ts',
                        'usage':
                        None,
                        'streamMetadata': {
                            'bitrateKbps': 2185,
                            'width': 300,
                            'height': 250,
                            'mimeType': None,
                            'lang': None,
                            'tags': {},
                            'contentType': 'UNSPECIFIED'
                        }
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_22.ts',
                        'usage':
                        None,
                        'streamMetadata': {
                            'bitrateKbps': 2185,
                            'width': 300,
                            'height': 250,
                            'mimeType': None,
                            'lang': None,
                            'tags': {},
                            'contentType': 'UNSPECIFIED'
                        }
                    }]
                }],
                id='adaptiveHLSStreamMetaData',
                name='Distribution with stream meta data',
                status=None,
                tags=None,
                targetAudiences=[{
                    'id': 'Broadcast_Videonet_Audience'
                }])


            # prepare the request, so we can modify it
            request = context.cl.Distributions.createEntity(
                    body=distributionDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # createEntity the Distributions, and check we got the error we expect
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
