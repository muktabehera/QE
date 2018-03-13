"""PFE Component Tests - Proximity_Zones.
# coding: utf-8
* TC-43789 - Proximity_Zones GET:

  Verify that 20 records is displayed on providing 'page-size' value as 0 for 'page' parameter using request GET “/proximities “.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities?page=1;0"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities?page=1;0"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Proximity_Zones')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Proximity_Zones test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43789')
    @pytest.mark.Proximity_Zones
    @pytest.mark.GET
    def test_TC_43789_GET_Proximity_Zones_Verify_Error_Message_Is_Displayed_On_Providing_Page_Parameter_As_0(self, context):
        """TC-43789 - Proximity_Zones-GET
           Verify that 20 records is displayed on providing 'page-size' value as 0 for 'page' parameter using request GET “/proximities “."""
        # Define a test step
        with pytest.allure.step("""Verify that 20 records is displayed on providing 'page-size' value as 0 for 'page' parameter using request GET “/proximities “."""):

            ### Positive test example

            # listEntities the Proximity_Zones.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.

            proximitylist = check(
                context.cl.Proximity_Zones.listEntities(
                    page='1;0')
            )

       # test | should.be.true(len(proximitylist) == 20)
            'proximitylistcheck' | expect.to.be.true(len(proximitylist)== 20)

    # try:
    #     client, response = check(
    #         context.cl.Proximity_Zones.listEntities(
    #             page='10;200',  # example : sdasd , 2;@@
    #             sort='abcd'  # example : ad:hj , abcd , 1234
    #         ),
    #         quiet=True, returnResponse=True
    #     )
    # except (HTTPBadRequest, HTTPForbidden) as e:  # 400, 403 error
    #     get_error_message(e) | expect.any(
    #         should.start_with('Invalid sort parameter specified. No seperator'),
    #         should.start_with('Invalid sort parameter specified. Invalid sort order, should be asc or dsc'),
    #         should.contain('Invalid page parameter specified. No seperator'),
    #         should.contain('Invalid page parameter specified. Invalid page size')
    #     )
    # else:
    #     raise Exception(
    #         "Expected error message, got {} status code instead.".format(
    #             response.status_code))