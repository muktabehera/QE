# -*- coding: UTF-8 -*-

"""PFE Component Tests - Delivery_Urls.

* TC-42301 - Delivery_Urls GET:

  Verify that User is unable to Create/Edit/View/Delete, any entity on any page of the QED, using token with "Provision" permission within the token expiration time.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/deliveryUrls?sourceUrl=qeddistribution%3A%2F%2FsimpleMediaMP4"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/deliveryUrls?sourceUrl=qeddistribution%3A%2F%2FsimpleMediaMP4"

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Delivery_Urls')
@pytest.allure.feature('GET')
class Test_PFE_Components(object):
    """PFE Delivery_Urls test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42301')
    @pytest.mark.Delivery_Urls
    @pytest.mark.GET
    def test_TC_42301_GET_Delivery_Urls_Id(self, context):
        """TC-42301 - Delivery_Urls-GET
           Verify that User is unable to Create/Edit/View/Delete, any entity on any page of the QED, using token with "Provision" permission within the token expiration time."""
        # Define a test step
        with pytest.allure.step("""Verify that User is unable to Create/Edit/View/Delete, any entity on any page of the QED, using token with "Provision" permission within the token expiration time."""):

            ### Positive test example

            # deliveryUrlsGet the Delivery_Urls.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Delivery_Urls.deliveryUrlsGet(
                    sourceUrl='qeddistribution://simpleMediaMP4')
            )

        with pytest.allure.step("""Verify that User is unable to Create/Edit/View/Delete, any entity on any page of the QED, using token with "Provision" permission within the token expiration time."""):

            ### Negative test example

            # deliveryUrlsGet the Delivery_Urls, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Delivery_Urls.deliveryUrlsGet(
                        sourceUrl='qeddistribution://simpleMediaMP4'),
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
