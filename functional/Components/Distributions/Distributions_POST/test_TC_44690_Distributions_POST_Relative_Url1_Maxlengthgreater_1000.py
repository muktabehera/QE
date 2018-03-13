# -*- coding: UTF-8 -*-

"""PFE Component Tests - Distributions.

* TC-44690 - Distributions POST:

  Verify that user is unable to create Distribution for Adaptive streaming on providing length greater than 1000 character for 'relativeUrl' parameter  using request POST /distributions .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/distributions"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/distributions"

JSON data sent to PathFinder in this test:

  {'activationDate': '2017-09-06T07:36:46.542Z',
   'distributionPolicy': 'REQUIRED',
   'files': [{'auxiliaryFiles': [{'relativeUrl': 'lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreat5'},
                                 {'relativeUrl': 'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_1/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_10.ts'},
                                 {'relativeUrl': 'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_1/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_11.ts'},
                                 {'relativeUrl': 'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_1/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_12.ts'},
                                 {'relativeUrl': 'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2.m3u8'},
                                 {'relativeUrl': 'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_20.ts'},
                                 {'relativeUrl': 'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_21.ts'},
                                 {'relativeUrl': 'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_22.ts'}],
              'id': 'HLS2',
              'sourceUrl': 'qedorigin://Auto_storage/HLS2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_Master.m3u8',
              'streamMetadata': {'bitrateKbps': 100,
                                 'contentType': 'UNSPECIFIED',
                                 'height': 5,
                                 'mimeType': 'video/mp4',
                                 'width': 10}}],
   'id': 'TC_44690_POST_distributions_relativeUrl1_Maxlengthgreater1000',
   'name': 'TC_44690_POST_distributions_relativeUrl1_Maxlengthgreater1000',
   'targetAudiences': [{'id': 'Broadcast_Standalone_Audience'}]}

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44690')
    @pytest.mark.Distributions
    @pytest.mark.POST
    def test_TC_44690_POST_Distributions_Relative_Url1_Maxlengthgreater_1000(self, context):
        """TC-44690 - Distributions-POST
           Verify that user is unable to create Distribution for Adaptive streaming on providing length greater than 1000 character for 'relativeUrl' parameter  using request POST /distributions ."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to create Distribution for Adaptive streaming on providing length greater than 1000 character for 'relativeUrl' parameter  using request POST /distributions ."""):

            ### Positive test example

            # Test case configuration
            distributionDetails = context.sc.DistributionDetails(
                activationDate='2017-09-06T07:36:46.542Z',
                distributionPolicy='REQUIRED',
                expirationDate=None,
                files=[{
                    'id':
                    'HLS2',
                    'sourceUrl':
                    'qedorigin://Auto_storage/HLS2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_Master.m3u8',
                    'auxiliaryFiles': [{
                        'relativeUrl':
                        'lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreat5'
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_1/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_10.ts'
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_1/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_11.ts'
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_1/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_12.ts'
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2.m3u8'
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_20.ts'
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_21.ts'
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_22.ts'
                    }],
                    'streamMetadata': {
                        'bitrateKbps': 100,
                        'width': 10,
                        'height': 5,
                        'mimeType': 'video/mp4',
                        'contentType': 'UNSPECIFIED'
                    }
                }],
                id='TC_44690_POST_distributions_relativeUrl1_Maxlengthgreater1000',
                name='TC_44690_POST_distributions_relativeUrl1_Maxlengthgreater1000',
                status=None,
                tags=None,
                targetAudiences=[{
                    'id': 'Broadcast_Standalone_Audience'
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

        with pytest.allure.step("""Verify that user is unable to create Distribution for Adaptive streaming on providing length greater than 1000 character for 'relativeUrl' parameter  using request POST /distributions ."""):

            ### Negative test example

            # Test case configuration
            distributionDetails = context.sc.DistributionDetails(
                activationDate='2017-09-06T07:36:46.542Z',
                distributionPolicy='REQUIRED',
                expirationDate=None,
                files=[{
                    'id':
                    'HLS2',
                    'sourceUrl':
                    'qedorigin://Auto_storage/HLS2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_Master.m3u8',
                    'auxiliaryFiles': [{
                        'relativeUrl':
                        'lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreaterthan1000lenghthgreat5'
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_1/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_10.ts'
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_1/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_11.ts'
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_1/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_12.ts'
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2.m3u8'
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_20.ts'
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_21.ts'
                    }, {
                        'relativeUrl':
                        'qumu_4e322c4a016e4f698783f006065468df_HLS_time1_2/qumu_4e322c4a016e4f698783f006065468df_HLS_time1_22.ts'
                    }],
                    'streamMetadata': {
                        'bitrateKbps': 100,
                        'width': 10,
                        'height': 5,
                        'mimeType': 'video/mp4',
                        'contentType': 'UNSPECIFIED'
                    }
                }],
                id='TC_44690_POST_distributions_relativeUrl1_Maxlengthgreater1000',
                name='TC_44690_POST_distributions_relativeUrl1_Maxlengthgreater1000',
                status=None,
                tags=None,
                targetAudiences=[{
                    'id': 'Broadcast_Standalone_Audience'
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
