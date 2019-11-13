# -*- coding: utf-8 -*-

"""
    neutrino_api

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""

from neutrino_api.api_helper import APIHelper
from neutrino_api.configuration import Configuration
from neutrino_api.controllers.base_controller import BaseController
from neutrino_api.http.auth.custom_query_auth import CustomQueryAuth
from neutrino_api.models.email_validate_response import EmailValidateResponse
from neutrino_api.models.user_agent_info_response import UserAgentInfoResponse
from neutrino_api.models.bad_word_filter_response import BadWordFilterResponse
from neutrino_api.models.convert_response import ConvertResponse
from neutrino_api.models.phone_validate_response import PhoneValidateResponse

class DataTools(BaseController):

    """A Controller to access Endpoints in the neutrino_api API."""


    def email_validate(self,
                       email,
                       fix_typos=False):
        """Does a POST request to /email-validate.

        Parse, validate and clean an email address. See:
        https://www.neutrinoapi.com/api/email-validate/

        Args:
            email (string): An email address
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
        _url_path = '/email-validate'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
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

    def user_agent_info(self,
                        user_agent):
        """Does a POST request to /user-agent-info.

        Parse, validate and get detailed user-agent information from a user
        agent string. See: https://www.neutrinoapi.com/api/user-agent-info/

        Args:
            user_agent (string): A user agent string

        Returns:
            UserAgentInfoResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/user-agent-info'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
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

    def bad_word_filter(self,
                        content,
                        censor_character=None):
        """Does a POST request to /bad-word-filter.

        Detect bad words, swear words and profanity in a given text. See:
        https://www.neutrinoapi.com/api/bad-word-filter/

        Args:
            content (string): The content to scan. This can be either a URL to
                load content from or an actual content string
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
        _url_path = '/bad-word-filter'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
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

        A powerful unit conversion tool. See:
        https://www.neutrinoapi.com/api/convert/

        Args:
            from_value (string): The value to convert from (e.g. 10.95)
            from_type (string): The type of the value to convert from (e.g.
                USD)
            to_type (string): The type to convert to (e.g. EUR)

        Returns:
            ConvertResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/convert'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
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

        Parse, validate and get location information about a phone number.
        See: https://www.neutrinoapi.com/api/phone-validate/

        Args:
            number (string): A phone number. This can be in international
                format (E.164) or local format. If passing local format you
                should use the 'country-code' or 'ip' options as well
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
        _url_path = '/phone-validate'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
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
