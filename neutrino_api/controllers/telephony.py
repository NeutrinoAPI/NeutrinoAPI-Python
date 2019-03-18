# -*- coding: utf-8 -*-

"""
    neutrino_api

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""

from neutrino_api.api_helper import APIHelper
from neutrino_api.configuration import Configuration
from neutrino_api.controllers.base_controller import BaseController
from neutrino_api.http.auth.custom_query_auth import CustomQueryAuth
from neutrino_api.models.phone_verify_response import PhoneVerifyResponse
from neutrino_api.models.sms_message_response import SMSMessageResponse
from neutrino_api.models.sms_verify_response import SMSVerifyResponse
from neutrino_api.models.verify_security_code_response import VerifySecurityCodeResponse
from neutrino_api.models.phone_playback_response import PhonePlaybackResponse
from neutrino_api.models.hlr_lookup_response import HLRLookupResponse

class Telephony(BaseController):

    """A Controller to access Endpoints in the neutrino_api API."""


    def phone_verify(self,
                     number,
                     code_length=6,
                     security_code=None,
                     playback_delay=800,
                     country_code=None,
                     language_code='en'):
        """Does a POST request to /phone-verify.

        Make an automated call to any valid phone number and playback a unique
        security code. See: https://www.neutrinoapi.com/api/phone-verify/

        Args:
            number (string): The phone number to send the verification code
                to
            code_length (int, optional): The number of digits to use in the
                security code (between 4 and 12)
            security_code (int, optional): Pass in your own security code.
                This is useful if you have implemented TOTP or similar 2FA
                methods. If not set then we will generate a secure random
                code
            playback_delay (int, optional): The delay in milliseconds between
                the playback of each security code
            country_code (string, optional): ISO 2-letter country code, assume
                numbers are based in this country.<br/>If not set numbers are
                assumed to be in international format (with or without the
                leading + sign)
            language_code (string, optional): The language to playback the
                verification code in, available languages are:<ul><li>de -
                German</li><li>en - English</li><li>es - Spanish</li><li>fr -
                French</li><li>it - Italian</li><li>pt - Portuguese</li><li>ru
                - Russian</li></ul>

        Returns:
            PhoneVerifyResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/phone-verify'
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

    def sms_message(self,
                    number,
                    message,
                    country_code=None):
        """Does a POST request to /sms-message.

        Send a free-form message to any mobile device via SMS. See:
        https://www.neutrinoapi.com/api/sms-message/

        Args:
            number (string): The phone number to send a message to
            message (string): The SMS message to send. Messages are truncated
                to a maximum of 150 characters for ASCII content OR 70
                characters for UTF content
            country_code (string, optional): ISO 2-letter country code, assume
                numbers are based in this country.<br/>If not set numbers are
                assumed to be in international format (with or without the
                leading + sign)

        Returns:
            SMSMessageResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/sms-message'
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
            'number': number,
            'message': message,
            'country-code': country_code
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, SMSMessageResponse.from_dictionary)

    def sms_verify(self,
                   number,
                   code_length=5,
                   security_code=None,
                   country_code=None,
                   language_code='en'):
        """Does a POST request to /sms-verify.

        Send a unique security code to any mobile device via SMS. See:
        https://www.neutrinoapi.com/api/sms-verify/

        Args:
            number (string): The phone number to send a verification code to
            code_length (int, optional): The number of digits to use in the
                security code (must be between 4 and 12)
            security_code (int, optional): Pass in your own security code.
                This is useful if you have implemented TOTP or similar 2FA
                methods. If not set then we will generate a secure random
                code
            country_code (string, optional): ISO 2-letter country code, assume
                numbers are based in this country.<br/>If not set numbers are
                assumed to be in international format (with or without the
                leading + sign)
            language_code (string, optional): The language to send the
                verification code in, available languages are:<ul><li>de -
                German</li><li>en - English</li><li>es - Spanish</li><li>fr -
                French</li><li>it - Italian</li><li>pt - Portuguese</li><li>ru
                - Russian</li></ul>

        Returns:
            SMSVerifyResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/sms-verify'
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

    def verify_security_code(self,
                             security_code):
        """Does a POST request to /verify-security-code.

        Check if a security code from one of the verify APIs is valid. See:
        https://www.neutrinoapi.com/api/verify-security-code/

        Args:
            security_code (string): The security code to verify

        Returns:
            VerifySecurityCodeResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/verify-security-code'
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
            'security-code': security_code
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, VerifySecurityCodeResponse.from_dictionary)

    def phone_playback(self,
                       number,
                       audio_url):
        """Does a POST request to /phone-playback.

        Make an automated call to any valid phone number and playback an audio
        message. See: https://www.neutrinoapi.com/api/phone-playback/

        Args:
            number (string): The phone number to call. Must be in valid
                international format
            audio_url (string): A URL to a valid audio file. Accepted audio
                formats are:<ul><li>MP3</li><li>WAV</li><li>OGG</ul></ul>You
                can use the following MP3 URL for
                testing:<br/>https://www.neutrinoapi.com/test-files/test1.mp3

        Returns:
            PhonePlaybackResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/phone-playback'
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

    def hlr_lookup(self,
                   number,
                   country_code=None):
        """Does a POST request to /hlr-lookup.

        Connect to the global mobile cellular network and retrieve the status
        of a mobile device. See: https://www.neutrinoapi.com/api/hlr-lookup/

        Args:
            number (string): A phone number
            country_code (string, optional): ISO 2-letter country code, assume
                numbers are based in this country.<br/>If not set numbers are
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
        _url_path = '/hlr-lookup'
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
