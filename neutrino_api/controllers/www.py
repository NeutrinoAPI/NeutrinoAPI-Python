# -*- coding: utf-8 -*-

"""
    neutrino_api

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""

from neutrino_api.api_helper import APIHelper
from neutrino_api.configuration import Configuration
from neutrino_api.controllers.base_controller import BaseController
from neutrino_api.http.auth.custom_query_auth import CustomQueryAuth
from neutrino_api.models.url_info_response import URLInfoResponse
from neutrino_api.models.browser_bot_response import BrowserBotResponse

class WWW(BaseController):

    """A Controller to access Endpoints in the neutrino_api API."""


    def url_info(self,
                 url,
                 fetch_content=False):
        """Does a POST request to /url-info.

        Parse, analyze and retrieve content from the supplied URL. See:
        https://www.neutrinoapi.com/api/url-info/

        Args:
            url (string): The URL to probe
            fetch_content (bool, optional): If this URL responds with html,
                text, json or xml then return the response. This option is
                useful if you want to perform further processing on the URL
                content (e.g. with the HTML Extract or HTML Clean APIs)

        Returns:
            URLInfoResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/url-info'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'output-case': 'camel',
            'url': url,
            'fetch-content': fetch_content
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, URLInfoResponse.from_dictionary)

    def browser_bot(self,
                    url,
                    timeout=30,
                    delay=2,
                    selector=None,
                    mexec=,
                    user_agent=None,
                    ignore_certificate_errors=False):
        """Does a POST request to /browser-bot.

        Browser bot can extract content, interact with keyboard and mouse
        events, and execute JavaScript on a website. See:
        https://www.neutrinoapi.com/api/browser-bot/

        Args:
            url (string): The URL to load
            timeout (int, optional): Timeout in seconds. Give up if still
                trying to load the page after this number of seconds
            delay (int, optional): Delay in seconds to wait before executing
                any selectors or JavaScript
            selector (string, optional): Extract content from the page DOM
                using this selector. Commonly known as a CSS selector, you can
                find a good reference <a
                href="https://www.w3schools.com/cssref/css_selectors.asp"
                target="_blank">here</a>
            mexec (list of string, optional): Execute JavaScript on the page.
                Each array element should contain a valid JavaScript statement
                in string form. If a statement returns any kind of value it
                will be returned in the 'exec-results' response.<br/><br/>For
                your convenience you can also use the following special
                shortcut functions:<br/><div style='padding-left:32px;
                font-family:inherit; font-size:inherit;'>sleep(seconds); Just
                wait/sleep for the specified number of
                seconds.<br/>click('selector'); Click on the first element
                matching the given selector.<br/>focus('selector'); Focus on
                the first element matching the given
                selector.<br/>keys('characters'); Send the specified keyboard
                characters. Use click() or focus() first to send keys to a
                specific element.<br/>enter(); Send the Enter key.<br/>tab();
                Send the Tab key.<br/></div><br/>Example:<br/><div
                style='padding-left:32px; font-family:inherit;
                font-size:inherit;'>[ "click('#button-id')", "sleep(1)",
                "click('.field-class')", "keys('1234')", "enter()" ]</div>
            user_agent (string, optional): Override the browsers default
                user-agent string with this one
            ignore_certificate_errors (bool, optional): Ignore any TLS/SSL
                certificate errors and load the page anyway

        Returns:
            BrowserBotResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/browser-bot'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'output-case': 'camel',
            'url': url,
            'timeout': timeout,
            'delay': delay,
            'selector': selector,
            'exec': mexec,
            'user-agent': user_agent,
            'ignore-certificate-errors': ignore_certificate_errors
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, BrowserBotResponse.from_dictionary)

    def html_clean(self,
                   content,
                   output_type):
        """Does a POST request to /html-clean.

        Clean and sanitize untrusted HTML. See:
        https://www.neutrinoapi.com/api/html-clean/

        Args:
            content (string): The HTML content. This can be either a URL to
                load HTML from or an actual HTML content string
            output_type (string): The level of sanitization, possible values
                are:<br/><b>plain-text</b>: reduce the content to plain text
                only (no HTML tags at all)<br/><br/><b>simple-text</b>: allow
                only very basic text formatting tags like b, em, i, strong,
                u<br/><br/><b>basic-html</b>: allow advanced text formatting
                and hyper links<br/><br/><b>basic-html-with-images</b>: same
                as basic html but also allows image
                tags<br/><br/><b>advanced-html</b>: same as basic html with
                images but also allows many more common HTML tags like table,
                ul, dl, pre<br/>

        Returns:
            binary: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/html-clean'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'content': content,
            'output-type': output_type
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request, binary = True)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body
