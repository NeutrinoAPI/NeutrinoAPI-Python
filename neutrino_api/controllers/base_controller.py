# -*- coding: utf-8 -*-

"""
    neutrino_api

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""

from neutrino_api.api_helper import APIHelper
from neutrino_api.http.http_context import HttpContext
from neutrino_api.http.requests_client import RequestsClient
from neutrino_api.exceptions.api_error_exception import APIErrorException
from neutrino_api.exceptions.api_exception import APIException

class BaseController(object):

    """All controllers inherit from this base class.

    Attributes:
        http_client (HttpClient): The HttpClient which a specific controller
            instance will use. By default all the controller objects share
            the same HttpClient. A user can use his own custom HttpClient
            as well.
        http_call_back (HttpCallBack): An object which holds call back
            methods to be called before and after the execution of an HttpRequest.
        global_headers (dict): The global headers of the API which are sent with
            every request.

    """

    http_client = RequestsClient(timeout=45)

    http_call_back = None

    global_headers = {
        'user-agent': 'APIMATIC 2.0'
    }

    def __init__(self, client=None, call_back=None):
        if client != None:
            self.http_client = client
        if call_back != None:
            self.http_call_back = call_back

    def validate_parameters(self, **kwargs):
        """Validates required parameters of an endpoint.

        Args:
            kwargs (dict): A dictionary of the required parameters.

        """
        for name, value in kwargs.items():
            if value is None:
                raise ValueError("Required parameter {} cannot be None.".format(name))

    def execute_request(self, request, binary=False):
        """Executes an HttpRequest.

        Args:
            request (HttpRequest): The HttpRequest to execute.
            binary (bool): A flag which should be set to True if
                a binary response is expected.

        Returns:
            HttpContext: The HttpContext of the request. It contains,
                both, the request itself and the HttpResponse object.

        """
        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(request)

        # Add global headers to request
        request.headers = APIHelper.merge_dicts(self.global_headers, request.headers)

        # Invoke the API call to fetch the response.
        func = self.http_client.execute_as_binary if binary else self.http_client.execute_as_string
        response = func(request)
        context = HttpContext(request, response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(context)

        return context

    def validate_response(self, context):
        """Validates an HTTP response by checking for global errors.

        Args:
            context (HttpContext): The HttpContext of the API call.

        """
        if context.response.status_code == 400:
            raise APIErrorException('Your API request has been rejected. Check the error code for details', context)
        elif context.response.status_code == 403:
            raise APIException('You have failed to authenticate or are using an invalid API path', context)
        elif context.response.status_code == 500:
            raise APIException('We messed up, sorry! Your request has caused a fatal exception', context)
        elif (context.response.status_code < 200) or (context.response.status_code > 208): #[200,208] = HTTP OK
            raise APIException('HTTP response not OK.', context)
