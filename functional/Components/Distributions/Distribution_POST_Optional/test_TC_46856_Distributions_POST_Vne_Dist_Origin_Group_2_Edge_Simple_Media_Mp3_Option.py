# -*- coding: UTF-8 -*-

"""PFE Component Tests - Distributions.

* TC-46856 - Distributions POST:

  Verify that VOD program having MP3 file is played successfully using VNE Route (Origin as VNE Group Distribution VNEGroupEdge 2 Standalone VNEs) Delivery System in QED.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/distributions"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/distributions"

JSON data sent to PathFinder in this test:

  {'activationDate': '2017-09-20T07:36:46.542Z',
   'distributionPolicy': 'OPTIONAL',
   'files': [{'id': 'mp3opt',
              'sourceUrl': 'qedorigin://Auto_storage/BachGavotte.mp3',
              'streamMetadata': {'bitrateKbps': 100,
                                 'contentType': 'UNSPECIFIED',
                                 'height': 5,
                                 'mimeType': 'video/mp3',
                                 'width': 10}}],
   'id': 'simpleMediaMP3DistOriginGroup_2EdgeOpt',
   'name': 'MP3 Distribution with Dist Origin Group and 2 EdgeOpt',
   'targetAudiences': [{'id': 'Audience_distOriginGroup_2EdgeVNE'}]}

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-46856')
    @pytest.mark.Distributions
    @pytest.mark.POST
    def test_TC_46856_POST_Distributions_Vne_Dist_Origin_Group_2_Edge_Simple_Media_Mp3(self, context):
        """TC-46856 - Distributions-POST
           Verify that VOD program having MP3 file is played successfully using VNE Route (Origin as VNE Group Distribution VNEGroupEdge 2 Standalone VNEs) Delivery System in QED."""
        # Define a test step
        with pytest.allure.step("""Verify that VOD program having MP3 file is played successfully using VNE Route (Origin as VNE Group Distribution VNEGroupEdge 2 Standalone VNEs) Delivery System in QED."""):

            ### Positive test example

            # Test case configuration
            distributionDetails = context.sc.DistributionDetails(
                activationDate='2017-09-20T07:36:46.542Z',
                distributionPolicy='OPTIONAL',
                expirationDate=None,
                files=[{
                    'id': 'mp3opt',
                    'sourceUrl': 'qedorigin://Auto_storage/BachGavotte.mp3',
                    'streamMetadata': {
                        'bitrateKbps': 100,
                        'width': 10,
                        'height': 5,
                        'mimeType': 'video/mp3',
                        'contentType': 'UNSPECIFIED'
                    }
                }],
                id='simpleMediaMP3DistOriginGroup_2EdgeOpt',
                name='MP3 Distribution with Dist Origin Group and 2 EdgeOpt',
                status=None,
                tags=None,
                targetAudiences=[{
                    'id': 'Audience_distOriginGroup_2EdgeVNE'
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

        with pytest.allure.step("""Verify that VOD program having MP3 file is played successfully using VNE Route (Origin as VNE Group Distribution VNEGroupEdge 2 Standalone VNEs) Delivery System in QED."""):

            ### Negative test example

            # Test case configuration
            distributionDetails = context.sc.DistributionDetails(
                activationDate='2017-09-20T07:36:46.542Z',
                distributionPolicy='OPTIONAL',
                expirationDate=None,
                files=[{
                    'id': 'mp3opt',
                    'sourceUrl': 'qedorigin://Auto_storage/BachGavotte.mp3',
                    'streamMetadata': {
                        'bitrateKbps': 100,
                        'width': 10,
                        'height': 5,
                        'mimeType': 'video/mp3',
                        'contentType': 'UNSPECIFIED'
                    }
                }],
                id='simpleMediaMP3DistOriginGroup_2EdgeOpt',
                name='MP3 Distribution with Dist Origin Group and 2 EdgeOpt',
                status=None,
                tags=None,
                targetAudiences=[{
                    'id': 'Audience_distOriginGroup_2EdgeVNE'
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
