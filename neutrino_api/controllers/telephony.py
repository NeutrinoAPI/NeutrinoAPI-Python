# -*- coding: utf-8 -*-

"""
    neutrino_api.controllers.telephony

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.custom_query_auth import CustomQueryAuth
from ..models.hlr_lookup_response import HLRLookupResponse
from ..models.phone_playback_response import PhonePlaybackResponse
from ..models.verify_security_code_response import VerifySecurityCodeResponse
from ..models.sms_verify_response import SMSVerifyResponse
from ..models.phone_verify_response import PhoneVerifyResponse

class Telephony(BaseController):

    """A Controller to access Endpoints in the neutrino_api API."""


    def hlr_lookup(self,
                   number,
                   country_code=None):
        """Does a POST request to /hlr-lookup.

        Connect to the global mobile cellular network and retrieve the status
        of a mobile device

        Args:
            number (string): A phone number
            country_code (string, optional): ISO 2-letter country code, assume
                numbers are based in this country. If not set numbers are
                assumed to be in international format (with or without the
                leading + sign)

        Returns:
            HLRLookupResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/hlr-lookup'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'output-case': 'camel',
            'number': number,
            'country-code': country_code
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, HLRLookupResponse.from_dictionary)

    def phone_playback(self,
                       number,
                       audio_url):
        """Does a POST request to /phone-playback.

        Make an automated call to any valid phone number and playback an audio
        message

        Args:
            number (string): The phone number to call. Must be valid
                international format
            audio_url (string): A URL to a valid audio file. Accepted audio
                formats are: MP3, WAV, OGG

        Returns:
            PhonePlaybackResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/phone-playback'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'output-case': 'camel',
            'number': number,
            'audio-url': audio_url
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, PhonePlaybackResponse.from_dictionary)

    def verify_security_code(self,
                             security_code):
        """Does a POST request to /verify-security-code.

        Check if a security code from one of the verify APIs is valid

        Args:
            security_code (int): The security code to verify

        Returns:
            VerifySecurityCodeResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/verify-security-code'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'output-case': 'camel',
            'security-code': security_code
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, VerifySecurityCodeResponse.from_dictionary)

    def sms_verify(self,
                   number,
                   code_length=5,
                   security_code=None,
                   country_code=None,
                   language_code='en'):
        """Does a POST request to /sms-verify.

        Send a unique security code to any mobile device via SMS

        Args:
            number (string): The phone number to send a verification code to
            code_length (int, optional): The number of digits to use in the
                security code (must be between 4 and 12)
            security_code (int, optional): ass in your own security code. This
                is useful if you have implemented TOTP or similar 2FA methods.
                If not set then we will generate a secure random code (only
                numerical security codes are currently supported)
            country_code (string, optional): ISO 2-letter country code, assume
                numbers are based in this country. If not set numbers are
                assumed to be in international format (with or without the
                leading + sign)
            language_code (string, optional): The language to send the
                verification code in, available languages are: de - German, en
                - English, es - Spanish, fr - Fench, it - Italian, pt -
                Portuguese, ru - Russian

        Returns:
            SMSVerifyResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/sms-verify'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'output-case': 'camel',
            'number': number,
            'code-length': code_length,
            'security-code': security_code,
            'country-code': country_code,
            'language-code': language_code
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, SMSVerifyResponse.from_dictionary)

    def phone_verify(self,
                     number,
                     code_length=6,
                     security_code=None,
                     playback_delay=800,
                     country_code=None,
                     language_code='en'):
        """Does a POST request to /phone-verify.

        Make an automated call to any valid phone number and playback a unique
        security code

        Args:
            number (string): The phone number to send the verification code
                to
            code_length (int, optional): The number of digits to use in the
                security code (between 4 and 12)
            security_code (int, optional): Pass in your own security code.
                This is useful if you have implemented TOTP or similar 2FA
                methods. If not set then we will generate a secure random code
                (only numerical security codes are currently supported)
            playback_delay (int, optional): The delay in milliseconds between
                the playback of each security code
            country_code (string, optional): ISO 2-letter country code, assume
                numbers are based in this country. If not set numbers are
                assumed to be in international format (with or without the
                leading + sign)
            language_code (string, optional): The language to playback the
                verification code in, available languages are: de - German, en
                - English, es - Spanish, fr - Fench, it - Italian, pt -
                Portuguese, ru - Russian

        Returns:
            PhoneVerifyResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/phone-verify'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'output-case': 'camel',
            'number': number,
            'code-length': code_length,
            'security-code': security_code,
            'playback-delay': playback_delay,
            'country-code': country_code,
            'language-code': language_code
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, PhoneVerifyResponse.from_dictionary)
