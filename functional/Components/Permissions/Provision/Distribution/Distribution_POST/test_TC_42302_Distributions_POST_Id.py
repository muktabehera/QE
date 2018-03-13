# -*- coding: UTF-8 -*-

"""PFE Component Tests - Distributions.

* TC-42302 - Distributions POST:

  Verify that User is unable to Create/Edit/View/Delete, any Distribution/Delivery URL from QED, using token with "Provision" permission within the token expiration time.


Equivalent test CURL command:

  curl -k -H "Host: <client_host>" -H "Authorization: Bearer
       <valid_token>" -X POST -d @<JSON_data_file> -H "Content-Type:
       application/json" "<PF_host>://<client_host>/distributions"

Same, with test data:

  curl -k -H "Host: <client_host>" -H "Authorization: Bearer
       <valid_token>" -X POST -d @<JSON_data_file> -H "Content-Type:
       application/json" "<PF_host>://<client_host>/distributions"

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
   'id': 'provision_notAbleToCreateDistribution',
   'modificationDate': '2016-05-12T10:44:11Z',
   'name': 'provision_notAbleToCreateDistribution',
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
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Distributions test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42302')
    @pytest.mark.Distributions
    @pytest.mark.POST
    def test_TC_42302_POST_Distributions_Id(self, context):
        """TC-42302 - Distributions-POST
           Verify that User is unable to Create/Edit/View/Delete, any Distribution/Delivery URL from QED, using token with "Provision" permission within the token expiration time."""
        # Define a test step
        with pytest.allure.step("""Verify that User is unable to Create/Edit/View/Delete, any Distribution/Delivery URL from QED, using token with "Provision" permission within the token expiration time."""):

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
                id='provision_notAbleToCreateDistribution',
                modificationDate='2016-05-12T10:44:11Z',
                name='provision_notAbleToCreateDistribution',
                status='PUSH_COMPLETE',
                tags=None,
                targetAudiences=[{
                    'id': 'autoAud',
                    'name': 'autoAudVNE'
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

        with pytest.allure.step("""Verify that User is unable to Create/Edit/View/Delete, any Distribution/Delivery URL from QED, using token with "Provision" permission within the token expiration time."""):

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
                id='provision_notAbleToCreateDistribution',
                modificationDate='2016-05-12T10:44:11Z',
                name='provision_notAbleToCreateDistribution',
                status='PUSH_COMPLETE',
                tags=None,
                targetAudiences=[{
                    'id': 'autoAud',
                    'name': 'autoAudVNE'
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
