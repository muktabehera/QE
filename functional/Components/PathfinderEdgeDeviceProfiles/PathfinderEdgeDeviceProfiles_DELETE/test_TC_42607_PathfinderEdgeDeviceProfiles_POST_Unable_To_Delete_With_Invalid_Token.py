# -*- coding: UTF-8 -*-

"""PFE Component Tests - Pathfinder_Edge_Device_Profiles.

* TC-42607 - Pathfinder_Edge_Device_Profiles POST:

  Verify that user unable to DELETE VideoEdge Profile in the application for DELETE request "/devices/veProfiles/{id}" with invalid token.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veProfiles"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veProfiles"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': False,
   'configurations': [{'host': '172.30.3.174', 'id': 'default'}],
   'description': 'Proxy_profile_Delete Proxy_profile_Delete '
                  'Proxy_profile_Delete Proxy_profile_Delete '
                  'Proxy_profile_Delete Proxy_profile_Delete Proxy_profile '
                  'Proxy_profile_Delete',
   'enablePrepositioning': False,
   'enableTokenAuthentication': False,
   'httpService': {'httpPort': 80,
                   'httpsPort': 443,
                   'protocol': 'http',
                   'serviceActive': True,
                   'vodPublishingPoints': None},
   'id': 'Proxy_profileDelete1',
   'manifestRequestFrequency': 600,
   'maximumDownloadTime': 54000,
   'name': 'Proxy_profileDelete1',
   'nonRestrictedPeriodDownloadBandwidth': 500,
   'proxyMode': 'PROXY',
   'restrictedBandwidthEnd': 17,
   'restrictedBandwidthStart': 8,
   'restrictedPeriodDownloadBandwidth': 100,
   'rtspService': {'multicastAddress': '',
                   'multicastEnabled': False,
                   'multicastTtl': 5,
                   'rtspStreamingPort': 554,
                   'serviceActive': True,
                   'unicastFailoverEnabled': True},
   'tokenExpirationTime': 180,
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Pathfinder_Edge_Device_Profiles')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Pathfinder_Edge_Device_Profiles test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42607')
    @pytest.mark.Pathfinder_Edge_Device_Profiles
    @pytest.mark.POST
    def test_TC_42607_POST_Pathfinder_Edge_Device_Profiles_Unable_To_Delete_With_Invalid_Token(self, context):
        """TC-42607 - Pathfinder_Edge_Device_Profiles-POST
           Verify that user unable to DELETE VideoEdge Profile in the application for DELETE request "/devices/veProfiles/{id}" with invalid token."""
        # Define a test step
        with pytest.allure.step("""Verify that user unable to DELETE VideoEdge Profile in the application for DELETE request "/devices/veProfiles/{id}" with invalid token."""):

            ### Positive test example

            # Test case configuration
            videoEdgeDevicePropertyDetails = context.sc.VideoEdgeDevicePropertyDetails(
                configAdminCanEdit=False,
                configurations=[{
                    'id': 'default',
                    'host': '172.30.3.174'
                }],
                enablePrepositioning=False,
                enableTokenAuthentication=False,
                httpService={
                    'serviceActive': True,
                    'protocol': 'http',
                    'httpPort': 80,
                    'httpsPort': 443,
                    'vodPublishingPoints': None
                },
                id='Proxy_profileDelete1',
                manifestRequestFrequency=600,
                maximumDownloadTime=54000,
                name='Proxy_profileDelete1',
                nonRestrictedPeriodDownloadBandwidth=500,
                proxyMode='PROXY',
                restrictedBandwidthEnd=17,
                restrictedBandwidthStart=8,
                restrictedPeriodDownloadBandwidth=100,
                rtspService={
                    'serviceActive': True,
                    'rtspStreamingPort': 554,
                    'multicastEnabled': False,
                    'multicastAddress': '',
                    'multicastTtl': 5,
                    'unicastFailoverEnabled': True
                },
                tokenExpirationTime=180,
                visibleInAllConfigurations=True)


            # createEntity the Pathfinder_Edge_Device_Profiles.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Pathfinder_Edge_Device_Profiles.createEntity(
                    body=videoEdgeDevicePropertyDetails
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user unable to DELETE VideoEdge Profile in the application for DELETE request "/devices/veProfiles/{id}" with invalid token."""):

            ### Negative test example

            # Test case configuration
            videoEdgeDevicePropertyDetails = context.sc.VideoEdgeDevicePropertyDetails(
                configAdminCanEdit=False,
                configurations=[{
                    'id': 'default',
                    'host': '172.30.3.174'
                }],
                enablePrepositioning=False,
                enableTokenAuthentication=False,
                httpService={
                    'serviceActive': True,
                    'protocol': 'http',
                    'httpPort': 80,
                    'httpsPort': 443,
                    'vodPublishingPoints': None
                },
                id='Proxy_profileDelete1',
                manifestRequestFrequency=600,
                maximumDownloadTime=54000,
                name='Proxy_profileDelete1',
                nonRestrictedPeriodDownloadBandwidth=500,
                proxyMode='PROXY',
                restrictedBandwidthEnd=17,
                restrictedBandwidthStart=8,
                restrictedPeriodDownloadBandwidth=100,
                rtspService={
                    'serviceActive': True,
                    'rtspStreamingPort': 554,
                    'multicastEnabled': False,
                    'multicastAddress': '',
                    'multicastTtl': 5,
                    'unicastFailoverEnabled': True
                },
                tokenExpirationTime=180,
                visibleInAllConfigurations=True)


            # prepare the request, so we can modify it
            request = context.cl.Pathfinder_Edge_Device_Profiles.createEntity(
                    body=videoEdgeDevicePropertyDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # createEntity the Pathfinder_Edge_Device_Profiles, and check we got the error we expect
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
