# -*- coding: UTF-8 -*-

"""PFE Component Tests - Distributions.

* TC-43766 - Distributions PATCH:

  Verify that user is able to update streaming parameters(name,expiration date,sourceurl,stream metadata,tags) media file for public delivery service using request PATCH "/distributions/{Id}" with VideoNet.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/distributions/distributionUpdate"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/distributions/distributionUpdate"

JSON data sent to PathFinder in this test:

  {'activationDate': '2017-09-04T07:36:46.542Z',
   'distributionPolicy': 'REQUIRED',
   'expirationDate': '2017-09-12T07:36:46.542Z',
   'files': [{'id': 'flv1',
              'sourceUrl': 'qedorigin://Auto_storage/trsFLV.flv',
              'streamMetadata': {'bitrateKbps': 164,
                                 'contentType': 'UNSPECIFIED',
                                 'height': 50,
                                 'mimeType': 'Video/flv',
                                 'tag': {'id': 'nametag'},
                                 'width': 100}}],
   'name': 'Updated Distribution with VNET '
           'Name_Date_SourceURL_Stream_metadataTag',
   'targetAudiences': [{'id': 'Broadcast_Videonet_Audience'}]}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Distributions')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Distributions test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43766')
    @pytest.mark.Distributions
    @pytest.mark.PATCH
    def test_TC_43766_PATCH_Distributions_Vnet_Name_Expiration_Date_Source_Url_Stream_Metadata_Tag(self, context):
        """TC-43766 - Distributions-PATCH
           Verify that user is able to update streaming parameters(name,expiration date,sourceurl,stream metadata,tags) media file for public delivery service using request PATCH "/distributions/{Id}" with VideoNet."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to update streaming parameters(name,expiration date,sourceurl,stream metadata,tags) media file for public delivery service using request PATCH "/distributions/{Id}" with VideoNet."""):

            ### Positive test example

            # Test case configuration
            distributionDetails = context.sc.DistributionDetails(
                activationDate='2017-09-04T07:36:46.542Z',
                distributionPolicy='REQUIRED',
                expirationDate='2017-09-12T07:36:46.542Z',
                files=[{
                    'id': 'flv1',
                    'sourceUrl': 'qedorigin://Auto_storage/trsFLV.flv',
                    'streamMetadata': {
                        'bitrateKbps': 164,
                        'width': 100,
                        'height': 50,
                        'mimeType': 'Video/flv',
                        'tag': {
                            'id': 'nametag'
                        },
                        'contentType': 'UNSPECIFIED'
                    }
                }],
                id=None,
                name=
                'Updated Distribution with VNET Name_Date_SourceURL_Stream_metadataTag',
                status=None,
                tags=None,
                targetAudiences=[{
                    'id': 'Broadcast_Videonet_Audience'
                }])


            # updateEntity the Distributions.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Distributions.updateEntity(
                    body=distributionDetails
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is able to update streaming parameters(name,expiration date,sourceurl,stream metadata,tags) media file for public delivery service using request PATCH "/distributions/{Id}" with VideoNet."""):

            ### Negative test example

            # Test case configuration
            distributionDetails = context.sc.DistributionDetails(
                activationDate='2017-09-04T07:36:46.542Z',
                distributionPolicy='REQUIRED',
                expirationDate='2017-09-12T07:36:46.542Z',
                files=[{
                    'id': 'flv1',
                    'sourceUrl': 'qedorigin://Auto_storage/trsFLV.flv',
                    'streamMetadata': {
                        'bitrateKbps': 164,
                        'width': 100,
                        'height': 50,
                        'mimeType': 'Video/flv',
                        'tag': {
                            'id': 'nametag'
                        },
                        'contentType': 'UNSPECIFIED'
                    }
                }],
                id=None,
                name=
                'Updated Distribution with VNET Name_Date_SourceURL_Stream_metadataTag',
                status=None,
                tags=None,
                targetAudiences=[{
                    'id': 'Broadcast_Videonet_Audience'
                }])


            # prepare the request, so we can modify it
            request = context.cl.Distributions.updateEntity(
                    body=distributionDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateEntity the Distributions, and check we got the error we expect
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
