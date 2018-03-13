"""PFE Component Tests - Proximity_Zones.
# coding: utf-8
* TC-43788 - Proximity_Zones GET:

  Verify that user is unable to GET the details of  proximities using request “/proximities “  with invalid values in  page and sort parameter .


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities?page=10;200 &sort=abcd"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/proximities?page=10;200 &sort=abcd"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Proximity_Zones')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Proximity_Zones test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43788')
    @pytest.mark.Proximity_Zones
    @pytest.mark.GET
    def test_TC_43788_GET_Proximity_Zones_Unable_To_Get_Details_With_Invalid_Page_And_Sort_Parameter(self, context):
        """TC-43788 - Proximity_Zones-GET
           Verify that user is unable to GET the details of  proximities using request “/proximities “  with invalid values in  page and sort parameter ."""
        # Define a test step
        with pytest.allure.step("""Verify that user is unable to GET the details of  proximities using request “/proximities “  with invalid values in  page and sort parameter ."""):


            # listEntities the Proximity_Zones, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Proximity_Zones.listEntities(
                        page='10;200', # example : sdasd , 2;@@
                        sort='abcd' # example : ad:hj , abcd , 1234
                    ),
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('Invalid sort parameter specified. No seperator'),
                    should.start_with('Invalid sort parameter specified. Invalid sort order, should be asc or dsc'),
                    should.contain('Invalid page parameter specified. No seperator'),
                    should.contain('Invalid page parameter specified. Invalid page size')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
