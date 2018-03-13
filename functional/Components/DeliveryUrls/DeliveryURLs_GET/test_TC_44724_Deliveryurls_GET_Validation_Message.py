# -*- coding: UTF-8 -*-

"""PFE Component Tests - Delivery_Urls.

* TC-44724 - Delivery_Urls GET:

  Verify that validation message is displayed if user doesn't provide the value in "contentType-protected","sourceUrl", "client", "networklocation", "mimeType", "audience","possibleAudiences"  using request "/deliveryUrls".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/deliveryUrls?sourceUrl="

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X GET -H "Content-Type: application/json"
       "<PF_host>://<client_host>/deliveryUrls?sourceUrl="

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44724')
    @pytest.mark.Delivery_Urls
    @pytest.mark.GET
    def test_TC_44724_GET_Delivery_Urls_Validation_Message(self, context):
        """TC-44724 - Delivery_Urls-GET
           Verify that validation message is displayed if user doesn't provide the value in "contentType-protected","sourceUrl", "client", "networklocation", "mimeType", "audience","possibleAudiences"  using request "/deliveryUrls"."""
        # Define a test step
        with pytest.allure.step("""Verify that validation message is displayed if user doesn't provide the value in "contentType-protected","sourceUrl", "client", "networklocation", "mimeType", "audience","possibleAudiences"  using request "/deliveryUrls"."""):

            ### Positive test example

            # deliveryUrlsGet the Delivery_Urls.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            check(
                context.cl.Delivery_Urls.deliveryUrlsGet()
            )

        with pytest.allure.step("""Verify that validation message is displayed if user doesn't provide the value in "contentType-protected","sourceUrl", "client", "networklocation", "mimeType", "audience","possibleAudiences"  using request "/deliveryUrls"."""):

            ### Negative test example

            # deliveryUrlsGet the Delivery_Urls, and check we got the error we expect
            try:
                client, response = check(
                    context.cl.Delivery_Urls.deliveryUrlsGet(),
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
