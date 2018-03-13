# -*- coding: UTF-8 -*-

"""PFE Component Tests - Clients.

* TC-42889 - Clients GET:

  Verify that user is able to GET the details of clients using request GET /clients with parameters page,sort=name;dsc and prefix.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients?page=0;3 &sort=name;dsc
       &prefix=c"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/clients?page=0;3 &sort=name;dsc
       &prefix=c"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Clients')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Clients test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42889')
    @pytest.mark.Clients
    @pytest.mark.GET
    def test_TC_42889_GET_Clients_Page_Sort_Dsc_Prefix(self, context):
        """TC-42889 - Clients-GET
           Verify that user is able to GET the details of clients using request GET /clients with parameters page,sort=name;dsc and prefix."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of clients using request GET /clients with parameters page,sort=name;dsc and prefix."""):

            # listEntities the Clients.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Clients.listEntities(
                    page='0;3', 
                    sort='name;dsc', 
                    prefix='p'
                )
            )
