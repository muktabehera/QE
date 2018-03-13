# -*- coding: UTF-8 -*-

"""PFE Component Tests - Pathfinder_Edge_Device_Profiles.

* TC-42502 - Pathfinder_Edge_Device_Profiles PATCH:

  Verify that user is unable to modify(PATCH)VideoEdge Profile using parameter [visibleInAllConfigurations: false,   configAdminCanEdit: false] for request "/devices/veProfiles/{id}" .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veProfiles/<data_ID1_under_test>"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veProfiles/PATCH_Proxy_profile"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': False,
   'configurations': [],
   'description': '',
   'enablePrepositioning': True,
   'enableTokenAuthentication': False,
   'httpService': {'httpPort': 80,
                   'httpsPort': 443,
                   'protocol': 'http',
                   'serviceActive': True,
                   'vodPublishingPoints': [{'guid': '2ac6540a-9785-4c49-8d09-eefc3dd409f2',
                                            'name': 'test1',
                                            'originId': '123456'},
                                           {'guid': 'feec407c-fc6f-4f0b-9486-477b2ef6d884',
                                            'name': 'test2',
                                            'originId': '12Client'}]},
   'id': 'PATCH_Proxy_profile',
   'manifestRequestFrequency': 60,
   'maximumDownloadTime': 54000,
   'name': 'PATCH_Proxy_profile',
   'nonRestrictedPeriodDownloadBandwidth': 500,
   'proxyMode': 'NO_PROXY',
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
   'visibleInAllConfigurations': False}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Pathfinder_Edge_Device_Profiles')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Pathfinder_Edge_Device_Profiles test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42502')
    @pytest.mark.Pathfinder_Edge_Device_Profiles
    @pytest.mark.PATCH
    def test_TC_42502_PATCH_Pathfinder_Edge_Device_Profiles_Unable_To_Modify_With_Visible_In_All_And_Config_Admin_As_False(self, context):
        """TC-42502 - Pathfinder_Edge_Device_Profiles-PATCH
           Verify that user is unable to modify(PATCH)VideoEdge Profile using parameter [visibleInAllConfigurations: false,   configAdminCanEdit: false] for request "/devices/veProfiles/{id}" ."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to modify(PATCH)VideoEdge Profile using parameter [visibleInAllConfigurations: false,   configAdminCanEdit: false] for request "/devices/veProfiles/{id}" ."""):

            ### Positive test example

            # Test case configuration
            videoEdgeDevicePropertyDetails = context.sc.VideoEdgeDevicePropertyDetails(
                configAdminCanEdit=False,
                configurations=[],
                enablePrepositioning=True,
                enableTokenAuthentication=False,
                httpService={
                    'serviceActive':
                    True,
                    'protocol':
                    'http',
                    'httpPort':
                    80,
                    'httpsPort':
                    443,
                    'vodPublishingPoints': [{
                        'guid':
                        '2ac6540a-9785-4c49-8d09-eefc3dd409f2',
                        'originId':
                        '123456',
                        'name':
                        'test1'
                    }, {
                        'guid':
                        'feec407c-fc6f-4f0b-9486-477b2ef6d884',
                        'originId':
                        '12Client',
                        'name':
                        'test2'
                    }]
                },
                id='PATCH_Proxy_profile',
                manifestRequestFrequency=60,
                maximumDownloadTime=54000,
                name='PATCH_Proxy_profile',
                nonRestrictedPeriodDownloadBandwidth=500,
                proxyMode='NO_PROXY',
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
                visibleInAllConfigurations=False)


            # updateEntity the Pathfinder_Edge_Device_Profiles.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Pathfinder_Edge_Device_Profiles.updateEntity(
                    body=videoEdgeDevicePropertyDetails, 
                    id='PATCH_Proxy_profile'
                
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is unable to modify(PATCH)VideoEdge Profile using parameter [visibleInAllConfigurations: false,   configAdminCanEdit: false] for request "/devices/veProfiles/{id}" ."""):

            ### Negative test example

            # Test case configuration
            videoEdgeDevicePropertyDetails = context.sc.VideoEdgeDevicePropertyDetails(
                configAdminCanEdit=False,
                configurations=[],
                enablePrepositioning=True,
                enableTokenAuthentication=False,
                httpService={
                    'serviceActive':
                    True,
                    'protocol':
                    'http',
                    'httpPort':
                    80,
                    'httpsPort':
                    443,
                    'vodPublishingPoints': [{
                        'guid':
                        '2ac6540a-9785-4c49-8d09-eefc3dd409f2',
                        'originId':
                        '123456',
                        'name':
                        'test1'
                    }, {
                        'guid':
                        'feec407c-fc6f-4f0b-9486-477b2ef6d884',
                        'originId':
                        '12Client',
                        'name':
                        'test2'
                    }]
                },
                id='PATCH_Proxy_profile',
                manifestRequestFrequency=60,
                maximumDownloadTime=54000,
                name='PATCH_Proxy_profile',
                nonRestrictedPeriodDownloadBandwidth=500,
                proxyMode='NO_PROXY',
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
                visibleInAllConfigurations=False)


            # prepare the request, so we can modify it
            request = context.cl.Pathfinder_Edge_Device_Profiles.updateEntity(
                    body=videoEdgeDevicePropertyDetails, 
                    id='PATCH_Proxy_profile'
                
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # updateEntity the Pathfinder_Edge_Device_Profiles, and check we got the error we expect
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
