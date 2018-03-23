# -*- coding: utf-8 -*-

"""
    neutrino_api.controllers.data_tools

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.custom_query_auth import CustomQueryAuth
from ..models.email_validate_response import EmailValidateResponse
from ..models.bad_word_filter_response import BadWordFilterResponse
from ..models.convert_response import ConvertResponse
from ..models.phone_validate_response import PhoneValidateResponse
from ..models.user_agent_info_response import UserAgentInfoResponse
from ..models.html_extract_response import HTMLExtractResponse

class DataTools(BaseController):

    """A Controller to access Endpoints in the neutrino_api API."""


    def email_validate(self,
                       email,
                       fix_typos=False):
        """Does a POST request to /email-validate.

        Parse, validate and clean an email address

        Args:
            email (string): The email address
            fix_typos (bool, optional): Automatically attempt to fix typos in
                the address

        Returns:
            EmailValidateResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/email-validate'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'output-case': 'camel',
            'email': email,
            'fix-typos': fix_typos
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, EmailValidateResponse.from_dictionary)

    def bad_word_filter(self,
                        content,
                        censor_character=None):
        """Does a POST request to /bad-word-filter.

        Detect bad words, swear words and profanity in a given text

        Args:
            content (string): The text content to check. This can be either a
                URL to load content from or an actual content string
            censor_character (string, optional): The character to use to
                censor out the bad words found

        Returns:
            BadWordFilterResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/bad-word-filter'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'output-case': 'camel',
            'content': content,
            'censor-character': censor_character
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, BadWordFilterResponse.from_dictionary)

    def convert(self,
                from_value,
                from_type,
                to_type):
        """Does a POST request to /convert.

        A powerful unit and currency conversion tool

        Args:
            from_value (string): The value to convert from
            from_type (string): The type of the value to convert from
            to_type (string): The type to convert to

        Returns:
            ConvertResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/convert'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'output-case': 'camel',
            'from-value': from_value,
            'from-type': from_type,
            'to-type': to_type
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, ConvertResponse.from_dictionary)

    def phone_validate(self,
                       number,
                       country_code=None,
                       ip=None):
        """Does a POST request to /phone-validate.

        Parse, validate and get location information about a phone number

        Args:
            number (string): The phone number
            country_code (string, optional): ISO 2-letter country code, assume
                numbers are based in this country. If not set numbers are
                assumed to be in international format (with or without the
                leading + sign)
            ip (string, optional): Pass in a users IP address and we will
                assume numbers are based in the country of the IP address

        Returns:
            PhoneValidateResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/phone-validate'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'output-case': 'camel',
            'number': number,
            'country-code': country_code,
            'ip': ip
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, PhoneValidateResponse.from_dictionary)

    def user_agent_info(self,
                        user_agent):
        """Does a POST request to /user-agent-info.

        Parse, validate and get detailed user-agent information from a user
        agent string

        Args:
            user_agent (string): A user-agent string

        Returns:
            UserAgentInfoResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/user-agent-info'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'output-case': 'camel',
            'user-agent': user_agent
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, UserAgentInfoResponse.from_dictionary)

    def html_clean(self,
                   content,
                   output_type):
        """Does a POST request to /html-clean.

        Clean and sanitize untrusted HTML

        Args:
            content (string): The HTML content. This can be either a URL to
                load HTML from or an actual HTML content string
            output_type (string): The level of sanitization, possible values
                are: plain-text, simple-text, basic-html,
                basic-html-with-images, advanced-html

        Returns:
            binary: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/html-clean'
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

    def html_extract(self,
                     content,
                     tag,
                     attribute=None,
                     base_url=None):
        """Does a POST request to /html-extract-tags.

        Extract specific HTML tag contents or attributes from complex HTML or
        XHTML content

        Args:
            content (string): The HTML content. This can be either a URL to
                load HTML from or an actual HTML content string
            tag (string): The HTML tag(s) to extract data from. This can just
                be a simple tag name like 'img' OR a CSS/jQuery style
                selector
            attribute (string, optional): If set, then extract data from the
                specified tag attribute. If not set, then data will be
                extracted from the tags inner content
            base_url (string, optional): The base URL to replace into realive
                links

        Returns:
            HTMLExtractResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/html-extract-tags'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'output-case': 'camel',
            'content': content,
            'tag': tag,
            'attribute': attribute,
            'base-url': base_url
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, HTMLExtractResponse.from_dictionary)
