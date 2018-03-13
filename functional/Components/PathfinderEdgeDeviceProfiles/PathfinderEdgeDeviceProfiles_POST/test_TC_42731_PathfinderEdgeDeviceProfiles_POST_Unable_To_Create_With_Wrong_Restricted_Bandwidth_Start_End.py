# -*- coding: UTF-8 -*-

"""PFE Component Tests - Pathfinder_Edge_Device_Profiles.

* TC-42731 - Pathfinder_Edge_Device_Profiles POST:

  Verify that correct message is displayed while creating VideoEdge device profile  using wrong inputs for (Start and End time)  using POST /devices/veProfiles  .


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
   'configurations': [],
   'description': '',
   'enablePrepositioning': False,
   'enableTokenAuthentication': False,
   'httpService': {'httpPort': 80,
                   'httpsPort': 443,
                   'protocol': 'http',
                   'serviceActive': True,
                   'vodPublishingPoints': []},
   'id': 'NO_PROXY_WrongRestrictedBandwidthStart',
   'manifestRequestFrequency': 600,
   'maximumDownloadTime': 54000,
   'name': 'NO_PROXY_WrongRestrictedBandwidthStart',
   'nonRestrictedPeriodDownloadBandwidth': 500,
   'proxyMode': 'NO_PROXY',
   'restrictedBandwidthEnd': 258,
   'restrictedBandwidthStart': 1232,
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42731')
    @pytest.mark.Pathfinder_Edge_Device_Profiles
    @pytest.mark.POST
    def test_TC_42731_POST_Pathfinder_Edge_Device_Profiles_Unable_To_Create_With_Wrong_Restricted_Bandwidth_Start_End(self, context):
        """TC-42731 - Pathfinder_Edge_Device_Profiles-POST
           Verify that correct message is displayed while creating VideoEdge device profile  using wrong inputs for (Start and End time)  using POST /devices/veProfiles  ."""
        # Define a test step
        with pytest.allure.step("""Verify that correct message is displayed while creating VideoEdge device profile  using wrong inputs for (Start and End time)  using POST /devices/veProfiles  ."""):

            ### Positive test example

            # Test case configuration
            videoEdgeDevicePropertyDetails = context.sc.VideoEdgeDevicePropertyDetails(
                configAdminCanEdit=False,
                configurations=[],
                enablePrepositioning=False,
                enableTokenAuthentication=False,
                httpService={
                    'serviceActive': True,
                    'protocol': 'http',
                    'httpPort': 80,
                    'httpsPort': 443,
                    'vodPublishingPoints': []
                },
                id='NO_PROXY_WrongRestrictedBandwidthStart',
                manifestRequestFrequency=600,
                maximumDownloadTime=54000,
                name='NO_PROXY_WrongRestrictedBandwidthStart',
                nonRestrictedPeriodDownloadBandwidth=500,
                proxyMode='NO_PROXY',
                restrictedBandwidthEnd=258,
                restrictedBandwidthStart=1232,
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

        with pytest.allure.step("""Verify that correct message is displayed while creating VideoEdge device profile  using wrong inputs for (Start and End time)  using POST /devices/veProfiles  ."""):

            ### Negative test example

            # Test case configuration
            videoEdgeDevicePropertyDetails = context.sc.VideoEdgeDevicePropertyDetails(
                configAdminCanEdit=False,
                configurations=[],
                enablePrepositioning=False,
                enableTokenAuthentication=False,
                httpService={
                    'serviceActive': True,
                    'protocol': 'http',
                    'httpPort': 80,
                    'httpsPort': 443,
                    'vodPublishingPoints': []
                },
                id='NO_PROXY_WrongRestrictedBandwidthStart',
                manifestRequestFrequency=600,
                maximumDownloadTime=54000,
                name='NO_PROXY_WrongRestrictedBandwidthStart',
                nonRestrictedPeriodDownloadBandwidth=500,
                proxyMode='NO_PROXY',
                restrictedBandwidthEnd=258,
                restrictedBandwidthStart=1232,
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
