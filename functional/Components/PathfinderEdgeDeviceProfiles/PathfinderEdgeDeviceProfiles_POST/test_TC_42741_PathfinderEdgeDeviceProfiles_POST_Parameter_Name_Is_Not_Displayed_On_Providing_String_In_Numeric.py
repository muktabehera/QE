# -*- coding: UTF-8 -*-

"""PFE Component Tests - Pathfinder_Edge_Device_Profiles.

* TC-42741 - Pathfinder_Edge_Device_Profiles POST:

  Verify that  Error message with parameter name is displayed in the response body on providing string values in numeric parameters using POST /devices/veProfiles.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veProfiles"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/veProfiles"

JSON data sent to PathFinder in this test:

  {
  "visibleInAllConfigurations": true,
  "configAdminCanEdit": true,
  "configurations": [],
  "name": "StringInNumeric",
  "id": "StringInNumeric",
  "description": "NoProxy",
  "proxyMode": "NO_PROXY",
  "enablePrepositioning": true,
  "enableTokenAuthentication": true,
  "tokenExpirationTime": 180,
  "restrictedBandwidthStart": 8,
  "restrictedBandwidthEnd": 17,
  "restrictedPeriodDownloadBandwidth": asas,
  "nonRestrictedPeriodDownloadBandwidth": asas,
  "maximumDownloadTime": asas,
  "manifestRequestFrequency": saasa,
  "httpService":
  { "serviceActive": true, "protocol": "http", "httpPort": sasa, "httpsPort": sasas, "vodPublishingPoints": null }

  ,
  "rtspService":
  { "serviceActive": true, "rtspStreamingPort": sasas, "multicastEnabled": true, "multicastAddress": "asasa", "multicastTtl": sasa, "unicastFailoverEnabled": true }

  }

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42741')
    @pytest.mark.Pathfinder_Edge_Device_Profiles
    @pytest.mark.POST
    def test_TC_42741_POST_Pathfinder_Edge_Device_Profiles_Parameter_Name_Is_Not_Displayed_On_Providing_String_In_Numeric(self, context):
        """TC-42741 - Pathfinder_Edge_Device_Profiles-POST
           Verify that  Error message with parameter name is displayed in the response body on providing string values in numeric parameters using POST /devices/veProfiles."""
        # Define a test step
        with pytest.allure.step("""Verify that  Error message with parameter name is displayed in the response body on providing string values in numeric parameters using POST /devices/veProfiles."""):

            ### Positive test example

            # Test case configuration
            videoEdgeDevicePropertyDetails = context.sc.UNKNOWN

                        ### =!!==>> Could not parse test data.
                        ###         Please fix the following manually:

            unknownJSON= """{
            "visibleInAllConfigurations": true,
            "configAdminCanEdit": true,
            "configurations": [],
            "name": "StringInNumeric",
            "id": "StringInNumeric",
            "description": "NoProxy",
            "proxyMode": "NO_PROXY",
            "enablePrepositioning": true,
            "enableTokenAuthentication": true,
            "tokenExpirationTime": 180,
            "restrictedBandwidthStart": 8,
            "restrictedBandwidthEnd": 17,
            "restrictedPeriodDownloadBandwidth": asas,
            "nonRestrictedPeriodDownloadBandwidth": asas,
            "maximumDownloadTime": asas,
            "manifestRequestFrequency": saasa,
            "httpService":
            { "serviceActive": true, "protocol": "http", "httpPort": sasa, "httpsPort": sasas, "vodPublishingPoints": null }

            ,
            "rtspService":
            { "serviceActive": true, "rtspStreamingPort": sasas, "multicastEnabled": true, "multicastAddress": "asasa", "multicastTtl": sasa, "unicastFailoverEnabled": true }

            }"""
            

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

        with pytest.allure.step("""Verify that  Error message with parameter name is displayed in the response body on providing string values in numeric parameters using POST /devices/veProfiles."""):

            ### Negative test example

            # Test case configuration
            videoEdgeDevicePropertyDetails = context.sc.UNKNOWN

                        ### =!!==>> Could not parse test data.
                        ###         Please fix the following manually:

            unknownJSON= """{
            "visibleInAllConfigurations": true,
            "configAdminCanEdit": true,
            "configurations": [],
            "name": "StringInNumeric",
            "id": "StringInNumeric",
            "description": "NoProxy",
            "proxyMode": "NO_PROXY",
            "enablePrepositioning": true,
            "enableTokenAuthentication": true,
            "tokenExpirationTime": 180,
            "restrictedBandwidthStart": 8,
            "restrictedBandwidthEnd": 17,
            "restrictedPeriodDownloadBandwidth": asas,
            "nonRestrictedPeriodDownloadBandwidth": asas,
            "maximumDownloadTime": asas,
            "manifestRequestFrequency": saasa,
            "httpService":
            { "serviceActive": true, "protocol": "http", "httpPort": sasa, "httpsPort": sasas, "vodPublishingPoints": null }

            ,
            "rtspService":
            { "serviceActive": true, "rtspStreamingPort": sasas, "multicastEnabled": true, "multicastAddress": "asasa", "multicastTtl": sasa, "unicastFailoverEnabled": true }

            }"""
            

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
