# -*- coding: UTF-8 -*-

"""PFE Component Tests - Distributions.

* TC-44459 - Distributions PATCH:

  Verify that user is unable to create group on providing invalid values in parameter 'deliveryLoadBalancePolicy' using request POST '/groups'.


Equivalent test CURL command:

  curl -k -H "Host: <client_host>" -H "Authorization: Bearer
       <valid_token>" -X PATCH -d @<JSON_data_file> -H "Content-Type:
       application/json"
       "<PF_host>://<client_host>/distributions/<data_ID1_under_test>"

Same, with test data:

  curl -k -H "Host: <client_host>" -H "Authorization: Bearer
       <valid_token>" -X PATCH -d @<JSON_data_file> -H "Content-Type:
       application/json"
       "<PF_host>://<client_host>/distributions/simpleMediaMP4"

JSON data sent to PathFinder in this test:

  {'activationDate': '2016-03-08T07:36:46Z',
   'creationDate': '2016-05-12T10:44:11Z',
   'distributionPolicy': 'REQUIRED',
   'expirationDate': None,
   'files': [{'auxiliaryFiles': [],
              'id': 'mp4',
              'sourceUrl': 'qedorigin://OriginQA/MP4File.mp4',
              'status': 'PUSH_COMPLETE',
              'statusDetails': [],
              'streamMetadata': {'bitrateKbps': 100,
                                 'contentType': 'UNSPECIFIED',
                                 'height': 5,
                                 'lang': None,
                                 'mimeType': 'video/mp4',
                                 'tags': {},
                                 'width': 10}}],
   'id': 'simpleMediaMP4',
   'modificationDate': '2016-05-12T10:44:11Z',
   'name': 'Distribution with MP41 simple Media',
   'protectedContent': False,
   'status': 'PUSH_COMPLETE',
   'tags': None,
   'targetAudiences': [{'id': 'autoAud', 'name': 'autoAudVNE'}]}

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44459')
    @pytest.mark.Distributions
    @pytest.mark.PATCH
    def test_TC_44459_PATCH_Distributions_Group_Invalid_Del_Load_Balance_Policy(self, context):
        """TC-44459 - Distributions-PATCH
           Verify that user is unable to create group on providing invalid values in parameter 'deliveryLoadBalancePolicy' using request POST '/groups'."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to create group on providing invalid values in parameter 'deliveryLoadBalancePolicy' using request POST '/groups'."""):

            ### Positive test example

            # Test case configuration
            distributionDetails = context.sc.DistributionDetails(
                activationDate='2016-03-08T07:36:46Z',
                creationDate='2016-05-12T10:44:11Z',
                distributionPolicy='REQUIRED',
                expirationDate=None,
                files=[{
                    'id': 'mp4',
                    'sourceUrl': 'qedorigin://OriginQA/MP4File.mp4',
                    'streamMetadata': {
                        'bitrateKbps': 100,
                        'width': 10,
                        'height': 5,
                        'mimeType': 'video/mp4',
                        'lang': None,
                        'tags': {},
                        'contentType': 'UNSPECIFIED'
                    },
                    'auxiliaryFiles': [],
                    'status': 'PUSH_COMPLETE',
                    'statusDetails': []
                }],
                id='simpleMediaMP4',
                modificationDate='2016-05-12T10:44:11Z',
                name='Distribution with MP41 simple Media',
                status='PUSH_COMPLETE',
                tags=None,
                targetAudiences=[{
                    'id': 'autoAud',
                    'name': 'autoAudVNE'
                }])


            # updateEntity the Distributions.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Distributions.updateEntity(
                    body=distributionDetails, 
                    id='simpleMediaMP4'
                
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is unable to create group on providing invalid values in parameter 'deliveryLoadBalancePolicy' using request POST '/groups'."""):

            ### Negative test example

            # Test case configuration
            distributionDetails = context.sc.DistributionDetails(
                activationDate='2016-03-08T07:36:46Z',
                creationDate='2016-05-12T10:44:11Z',
                distributionPolicy='REQUIRED',
                expirationDate=None,
                files=[{
                    'id': 'mp4',
                    'sourceUrl': 'qedorigin://OriginQA/MP4File.mp4',
                    'streamMetadata': {
                        'bitrateKbps': 100,
                        'width': 10,
                        'height': 5,
                        'mimeType': 'video/mp4',
                        'lang': None,
                        'tags': {},
                        'contentType': 'UNSPECIFIED'
                    },
                    'auxiliaryFiles': [],
                    'status': 'PUSH_COMPLETE',
                    'statusDetails': []
                }],
                id='simpleMediaMP4',
                modificationDate='2016-05-12T10:44:11Z',
                name='Distribution with MP41 simple Media',
                status='PUSH_COMPLETE',
                tags=None,
                targetAudiences=[{
                    'id': 'autoAud',
                    'name': 'autoAudVNE'
                }])


            # prepare the request, so we can modify it
            request = context.cl.Distributions.updateEntity(
                    body=distributionDetails, 
                    id='simpleMediaMP4'
                
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
