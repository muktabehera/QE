# -*- coding: UTF-8 -*-

"""PFE Component Tests - Delivery_Urls.

* TC-43478 - Delivery_Urls POST:

  Verify that user is able to GET the details of network location using request GET /networkLocation with parameters page,sort=name;asc and prefix.


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/deliveryUrls?audience=Broadcast_Videonet_Audience"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/deliveryUrls?audience=Broadcast_Videonet_Audience"

JSON data sent to PathFinder in this test:

  {'networkContext': {'headers': [{'name': 'CONNECTION', 'value': 'keep-alive'},
                                  {'name': 'ACCEPT', 'value': '*/*'},
                                  {'name': 'ACCEPT-ENCODING',
                                   'value': 'gzip, deflate, sdch'},
                                  {'name': 'HOST', 'value': 'localhost:8080'},
                                  {'name': 'AUTHORIZATION',
                                   'value': 'Bearer '
                                            'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJkZWZhdWx0Iiwic3ViIjoiYWRtaW5AMTcyLjMwLjUuMjA0LmNvbSIsImF1ZCI6InFlZDpkZWZhdWx0IiwicWVkcCI6WyJzIiwiYyIsImciLCJwIiwiZCIsIm0iLCJhIl19.9NHxI87dGXSG5UYRj-fj2NagTiv8wR-nRgI4-NY4ZPI'}],
                      'query': [],
                      'remoteAddress': '127.0.0.1',
                      'remoteHost': '127.0.0.1',
                      'serverHost': 'localhost',
                      'serverPort': 8080,
                      'tags': []},
   'sources': [{'alternateAudios': [{'lang': '', 'relativeUrl': ''}],
                'alternateBitrates': [{'bitrate': 170,
                                       'height': 0,
                                       'relativeUrl': 'qedorigin://Auto_storage/MP4File.mp4',
                                       'width': 0},
                                      {'bitrate': 80,
                                       'height': 0,
                                       'relativeUrl': 'qedorigin://Auto_storage/MP4File.mp4',
                                       'width': 0},
                                      {'bitrate': 90,
                                       'height': 0,
                                       'relativeUrl': 'qedorigin://Auto_storage/MP4File.mp4',
                                       'width': 0}],
                'bitrate': 100,
                'captions': [{'lang': '', 'relativeUrl': ''}],
                'height': 0,
                'mimetype': 'video/mp4',
                'sourceUrl': 'qedorigin://Auto_storage/MP4File.mp4',
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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-43478')
    @pytest.mark.Delivery_Urls
    @pytest.mark.POST
    def test_TC_43478_POST_Delivery_Urls_Page_Sort_Asc_Prefix(self, context):
        """TC-43478 - Delivery_Urls-POST
           Verify that user is able to GET the details of network location using request GET /networkLocation with parameters page,sort=name;asc and prefix."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to GET the details of network location using request GET /networkLocation with parameters page,sort=name;asc and prefix."""):

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
                        'Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJkZWZhdWx0Iiwic3ViIjoiYWRtaW5AMTcyLjMwLjUuMjA0LmNvbSIsImF1ZCI6InFlZDpkZWZhdWx0IiwicWVkcCI6WyJzIiwiYyIsImciLCJwIiwiZCIsIm0iLCJhIl19.9NHxI87dGXSG5UYRj-fj2NagTiv8wR-nRgI4-NY4ZPI'
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
                    'qedorigin://Auto_storage/MP4File.mp4',
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
                        'qedorigin://Auto_storage/MP4File.mp4',
                        'bitrate':
                        170,
                        'width':
                        0,
                        'height':
                        0
                    }, {
                        'relativeUrl':
                        'qedorigin://Auto_storage/MP4File.mp4',
                        'bitrate':
                        80,
                        'width':
                        0,
                        'height':
                        0
                    }, {
                        'relativeUrl':
                        'qedorigin://Auto_storage/MP4File.mp4',
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
                    body=networkContextAndSourceGroupDetails, 
                    audience='Broadcast_Videonet_Audience'
                
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is able to GET the details of network location using request GET /networkLocation with parameters page,sort=name;asc and prefix."""):

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
                        'Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJkZWZhdWx0Iiwic3ViIjoiYWRtaW5AMTcyLjMwLjUuMjA0LmNvbSIsImF1ZCI6InFlZDpkZWZhdWx0IiwicWVkcCI6WyJzIiwiYyIsImciLCJwIiwiZCIsIm0iLCJhIl19.9NHxI87dGXSG5UYRj-fj2NagTiv8wR-nRgI4-NY4ZPI'
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
                    'qedorigin://Auto_storage/MP4File.mp4',
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
                        'qedorigin://Auto_storage/MP4File.mp4',
                        'bitrate':
                        170,
                        'width':
                        0,
                        'height':
                        0
                    }, {
                        'relativeUrl':
                        'qedorigin://Auto_storage/MP4File.mp4',
                        'bitrate':
                        80,
                        'width':
                        0,
                        'height':
                        0
                    }, {
                        'relativeUrl':
                        'qedorigin://Auto_storage/MP4File.mp4',
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
                    body=networkContextAndSourceGroupDetails, 
                    audience='Broadcast_Videonet_Audience'
                
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
