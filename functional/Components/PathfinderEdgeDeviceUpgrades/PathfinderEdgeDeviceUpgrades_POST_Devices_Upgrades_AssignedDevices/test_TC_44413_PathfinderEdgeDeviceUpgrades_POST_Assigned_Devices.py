# -*- coding: UTF-8 -*-

"""PFE Component Tests - Pathfinder_Edge_Device_Upgrades.

* TC-44413 - Pathfinder_Edge_Device_Upgrades POST:

  Verify that user is unable to get the details of Video Edge Device Upgrade assigned devices with invalid upgrade ID using request  POST "/devices/upgrades/{upgradeId}/assignedDevice".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/upgrades/InvalidUpgradeID/assignedDevices?effectiveDate=1503656870000"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/devices/upgrades/InvalidUpgradeID/assignedDevices?effectiveDate=1503656870000"

JSON data sent to PathFinder in this test:

  {'deviceIds': [{'id': 'Linux172.30.3.29'}]}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Pathfinder_Edge_Device_Upgrades')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Pathfinder_Edge_Device_Upgrades test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44413')
    @pytest.mark.Pathfinder_Edge_Device_Upgrades
    @pytest.mark.POST
    def test_TC_44413_POST_Pathfinder_Edge_Device_Upgrades_Assigned_Devices(self, context):
        """TC-44413 - Pathfinder_Edge_Device_Upgrades-POST
           Verify that user is unable to get the details of Video Edge Device Upgrade assigned devices with invalid upgrade ID using request  POST "/devices/upgrades/{upgradeId}/assignedDevice"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to get the details of Video Edge Device Upgrade assigned devices with invalid upgrade ID using request  POST "/devices/upgrades/{upgradeId}/assignedDevice"."""):

            ### Positive test example

            # Test case configuration
            upgradeDeviceDetails = context.sc.UpgradeDeviceDetails(deviceIds=[{'id': 'Linux172.30.3.29'}])


            # addUpgrade the Pathfinder_Edge_Device_Upgrades.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Pathfinder_Edge_Device_Upgrades.addUpgrade(
                    body=upgradeDeviceDetails, 
                    id='InvalidUpgradeID', 
                    effectiveDate='1503656870000'
                
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is unable to get the details of Video Edge Device Upgrade assigned devices with invalid upgrade ID using request  POST "/devices/upgrades/{upgradeId}/assignedDevice"."""):

            ### Negative test example

            # Test case configuration
            upgradeDeviceDetails = context.sc.UpgradeDeviceDetails(deviceIds=[{'id': 'Linux172.30.3.29'}])


            # prepare the request, so we can modify it
            request = context.cl.Pathfinder_Edge_Device_Upgrades.addUpgrade(
                    body=upgradeDeviceDetails, 
                    id='InvalidUpgradeID', 
                    effectiveDate='1503656870000'
                
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # addUpgrade the Pathfinder_Edge_Device_Upgrades, and check we got the error we expect
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
