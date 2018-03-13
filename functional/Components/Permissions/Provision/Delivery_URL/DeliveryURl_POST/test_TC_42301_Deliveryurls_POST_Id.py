# -*- coding: UTF-8 -*-

"""PFE Component Tests - Delivery_Urls.

* TC-42301 - Delivery_Urls POST:

  Verify that User is unable to Create/Edit/View/Delete, any entity on any page of the QED, using token with "Provision" permission within the token expiration time.


Equivalent test CURL command:

  curl -k -H "Host: <client_host>" -H "Authorization: Bearer
       <valid_token>" -X POST -d @<JSON_data_file> -H "Content-Type:
       application/json" "<PF_host>://<client_host>/deliveryUrls"

Same, with test data:

  curl -k -H "Host: <client_host>" -H "Authorization: Bearer
       <valid_token>" -X POST -d @<JSON_data_file> -H "Content-Type:
       application/json" "<PF_host>://<client_host>/deliveryUrls"

JSON data sent to PathFinder in this test:

  {'networkContext': {'headers': [{'name': 'CONNECTION', 'value': 'keep-alive'},
                                  {'name': 'ACCEPT', 'value': '*/*'},
                                  {'name': 'ACCEPT-ENCODING',
                                   'value': 'gzip, deflate, sdch'},
                                  {'name': 'HOST', 'value': 'localhost:8080'},
                                  {'name': 'AUTHORIZATION',
                                   'value': 'Bearer '
                                            'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJkZWZhdWx0Iiwic3ViIjoiYWRtaW5AMTcyLjMwLjIuMTQ5OjgwODAuY29tIiwiYXVkIjoicWVkOmRlZmF1bHQiLCJxZWRwIjpbInMiLCJjIiwiZyIsInAiLCJkIiwibSIsImEiXX0.uh1W0Hs2nemsjiRFRSiyiZgo4io5bUmmCSJqrYyIM0A'}],
                      'query': [],
                      'remoteAddress': '127.0.0.1',
                      'remoteHost': '127.0.0.1',
                      'serverHost': 'localhost',
                      'serverPort': 8080,
                      'tags': []},
   'sources': [{'alternateAudios': [{'lang': '', 'relativeUrl': ''}],
                'alternateBitrates': [{'bitrate': 170,
                                       'height': 0,
                                       'relativeUrl': 'qedorigin://VNEhttp/MP4File.mp4',
                                       'width': 0},
                                      {'bitrate': 80,
                                       'height': 0,
                                       'relativeUrl': 'qedorigin://VNEhttp/MP4File.mp4',
                                       'width': 0},
                                      {'bitrate': 90,
                                       'height': 0,
                                       'relativeUrl': 'qedorigin://VNEhttp/MP4File.mp4',
                                       'width': 0}],
                'bitrate': 100,
                'captions': [{'lang': '', 'relativeUrl': ''}],
                'height': 0,
                'mimetype': 'video/mp4',
                'sourceUrl': 'qedorigin://VNEhttp/MP4File.mp4',
                'width': 0}]}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Delivery_Urls')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Delivery_Urls test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-42301')
    @pytest.mark.Delivery_Urls
    @pytest.mark.POST
    def test_TC_42301_POST_Delivery_Urls_Id(self, context):
        """TC-42301 - Delivery_Urls-POST
           Verify that User is unable to Create/Edit/View/Delete, any entity on any page of the QED, using token with "Provision" permission within the token expiration time."""
        # Define a test step
        with pytest.allure.step("""Verify that User is unable to Create/Edit/View/Delete, any entity on any page of the QED, using token with "Provision" permission within the token expiration time."""):

            ### Positive test example

            # Test case configuration
            networkContextAndSourceGroupDetails = context.sc.NetworkContextAndSourceGroupDetails(
                networkContext={
                    'headers': [{
                        'name': 'CONNECTION',
                        'value': 'keep-alive'
                    }, {
                        'name': 'ACCEPT',
                        'value': '*/*'
                    }, {
                        'name': 'ACCEPT-ENCODING',
                        'value': 'gzip, deflate, sdch'
                    }, {
                        'name': 'HOST',
                        'value': 'localhost:8080'
                    }, {
                        'name':
                        'AUTHORIZATION',
                        'value':
                        'Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJkZWZhdWx0Iiwic3ViIjoiYWRtaW5AMTcyLjMwLjIuMTQ5OjgwODAuY29tIiwiYXVkIjoicWVkOmRlZmF1bHQiLCJxZWRwIjpbInMiLCJjIiwiZyIsInAiLCJkIiwibSIsImEiXX0.uh1W0Hs2nemsjiRFRSiyiZgo4io5bUmmCSJqrYyIM0A'
                    }],
                    'remoteAddress':
                    '127.0.0.1',
                    'remoteHost':
                    '127.0.0.1',
                    'serverHost':
                    'localhost',
                    'serverPort':
                    8080,
                    'query': [],
                    'tags': []
                },
                sources=[{
                    'sourceUrl':
                    'qedorigin://VNEhttp/MP4File.mp4',
                    'bitrate':
                    100,
                    'width':
                    0,
                    'height':
                    0,
                    'mimetype':
                    'video/mp4',
                    'alternateBitrates': [{
                        'relativeUrl':
                        'qedorigin://VNEhttp/MP4File.mp4',
                        'bitrate':
                        170,
                        'width':
                        0,
                        'height':
                        0
                    }, {
                        'relativeUrl':
                        'qedorigin://VNEhttp/MP4File.mp4',
                        'bitrate':
                        80,
                        'width':
                        0,
                        'height':
                        0
                    }, {
                        'relativeUrl':
                        'qedorigin://VNEhttp/MP4File.mp4',
                        'bitrate':
                        90,
                        'width':
                        0,
                        'height':
                        0
                    }],
                    'alternateAudios': [{
                        'relativeUrl': '',
                        'lang': ''
                    }],
                    'captions': [{
                        'relativeUrl': '',
                        'lang': ''
                    }]
                }])


            # deliveryUrlsPost the Delivery_Urls.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Delivery_Urls.deliveryUrlsPost(
                    body=networkContextAndSourceGroupDetails
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that User is unable to Create/Edit/View/Delete, any entity on any page of the QED, using token with "Provision" permission within the token expiration time."""):

            ### Negative test example

            # Test case configuration
            networkContextAndSourceGroupDetails = context.sc.NetworkContextAndSourceGroupDetails(
                networkContext={
                    'headers': [{
                        'name': 'CONNECTION',
                        'value': 'keep-alive'
                    }, {
                        'name': 'ACCEPT',
                        'value': '*/*'
                    }, {
                        'name': 'ACCEPT-ENCODING',
                        'value': 'gzip, deflate, sdch'
                    }, {
                        'name': 'HOST',
                        'value': 'localhost:8080'
                    }, {
                        'name':
                        'AUTHORIZATION',
                        'value':
                        'Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJkZWZhdWx0Iiwic3ViIjoiYWRtaW5AMTcyLjMwLjIuMTQ5OjgwODAuY29tIiwiYXVkIjoicWVkOmRlZmF1bHQiLCJxZWRwIjpbInMiLCJjIiwiZyIsInAiLCJkIiwibSIsImEiXX0.uh1W0Hs2nemsjiRFRSiyiZgo4io5bUmmCSJqrYyIM0A'
                    }],
                    'remoteAddress':
                    '127.0.0.1',
                    'remoteHost':
                    '127.0.0.1',
                    'serverHost':
                    'localhost',
                    'serverPort':
                    8080,
                    'query': [],
                    'tags': []
                },
                sources=[{
                    'sourceUrl':
                    'qedorigin://VNEhttp/MP4File.mp4',
                    'bitrate':
                    100,
                    'width':
                    0,
                    'height':
                    0,
                    'mimetype':
                    'video/mp4',
                    'alternateBitrates': [{
                        'relativeUrl':
                        'qedorigin://VNEhttp/MP4File.mp4',
                        'bitrate':
                        170,
                        'width':
                        0,
                        'height':
                        0
                    }, {
                        'relativeUrl':
                        'qedorigin://VNEhttp/MP4File.mp4',
                        'bitrate':
                        80,
                        'width':
                        0,
                        'height':
                        0
                    }, {
                        'relativeUrl':
                        'qedorigin://VNEhttp/MP4File.mp4',
                        'bitrate':
                        90,
                        'width':
                        0,
                        'height':
                        0
                    }],
                    'alternateAudios': [{
                        'relativeUrl': '',
                        'lang': ''
                    }],
                    'captions': [{
                        'relativeUrl': '',
                        'lang': ''
                    }]
                }])


            # prepare the request, so we can modify it
            request = context.cl.Delivery_Urls.deliveryUrlsPost(
                    body=networkContextAndSourceGroupDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # deliveryUrlsPost the Delivery_Urls, and check we got the error we expect
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
