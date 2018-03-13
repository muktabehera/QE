# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-42886 - Clients GET:

  Verify that user is able to GET the details of clients using request GET /clients with parameters page,sort=name;dsc.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients?page=0;3 &sort=name;dsc"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients?page=0;3 &sort=name;dsc"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42886')
    @pytest.mark.Clients
    @pytest.mark.GET
    def test_TC_42886_GET_Clients_Page_Sort_Dsc(self, context):
        """TC-42886 - Clients-GET
           Verify that user is able to GET the details of clients using request GET /clients with parameters page,sort=name;dsc."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of clients using request GET /clients with parameters page,sort=name;dsc."""):


            # listEntities the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Clients.listEntities(
                    page='0;3', 
                    sort='name;dsc'
                )
            )

