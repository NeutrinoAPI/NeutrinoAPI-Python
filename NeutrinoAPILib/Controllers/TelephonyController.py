# -*- coding: utf-8 -*-

"""
   NeutrinoAPILib.Controllers.TelephonyController

   This file was automatically generated for NeutrinoAPI.com by APIMATIC BETA v2.0 on 01/07/2016
"""
import unirest

from NeutrinoAPILib.APIHelper import APIHelper
from NeutrinoAPILib.Configuration import Configuration
from NeutrinoAPILib.APIException import APIException
from NeutrinoAPILib.Models.PhonePlaybackResponse import PhonePlaybackResponse
from NeutrinoAPILib.Models.VerifySecurityCodeResponse import VerifySecurityCodeResponse
from NeutrinoAPILib.Models.HLRLookupResponse import HLRLookupResponse
from NeutrinoAPILib.Models.PhoneVerifyResponse import PhoneVerifyResponse
from NeutrinoAPILib.Models.SMSVerifyResponse import SMSVerifyResponse


class TelephonyController(object):


    """A Controller to access Endpoints in the NeutrinoAPILib API."""

    def __init__(self,
                 user_id,
                 api_key):
        """
        Constructor with authentication and configuration parameters
        """
        self.__user_id = user_id
        self.__api_key = api_key

    def phone_playback(self,
                       audio_url,
                       number):
        """Does a POST request to /phone-playback.

        Make an automated call to any valid phone number and playback an audio
        message. See: https://www.neutrinoapi.com/api/phone-playback/

        Args:
            audio_url (string): A URL to a valid audio file. Accepted audio
                formats are: MP3, WAV, OGG
            number (string): The phone number to call. Must be valid
                international format

        Returns:
            PhonePlaybackResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/phone-playback"

        # Process optional query parameters
        query_parameters = {
            "user-id": self.__user_id,
            "api-key": self.__api_key
        }
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, query_parameters)

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "APIMATIC 2.0",
            "accept": "application/json"
        }

        # Prepare parameters
        parameters = {
            "audio-url": audio_url,
            "number": number,
            "output-case": output_case
        }
        # The body will be multipart data, so set the header
        headers['Content-Type'] = 'multipart/form-data'

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers, params=parameters)

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return PhonePlaybackResponse(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def verify_security_code(self,
                             security_code):
        """Does a POST request to /verify-security-code.

        Check if a security code from one of the verify APIs is valid. See:
        https://www.neutrinoapi.com/api/verify-security-code/

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
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/verify-security-code"

        # Process optional query parameters
        query_parameters = {
            "user-id": self.__user_id,
            "api-key": self.__api_key
        }
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, query_parameters)

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "APIMATIC 2.0",
            "accept": "application/json"
        }

        # Prepare parameters
        parameters = {
            "output-case": output_case,
            "security-code": security_code
        }
        # The body will be multipart data, so set the header
        headers['Content-Type'] = 'multipart/form-data'

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers, params=parameters)

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return VerifySecurityCodeResponse(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def hlr_lookup(self,
                   number,
                   country_code=None):
        """Does a POST request to /hlr-lookup.

        Mobile network HLR lookup service. See:
        https://www.neutrinoapi.com/api/hlr-lookup/

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
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/hlr-lookup"

        # Process optional query parameters
        query_parameters = {
            "user-id": self.__user_id,
            "api-key": self.__api_key
        }
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, query_parameters)

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "APIMATIC 2.0",
            "accept": "application/json"
        }

        # Prepare parameters
        parameters = {
            "number": number,
            "output-case": output_case,
            "country-code": country_code
        }
        # The body will be multipart data, so set the header
        headers['Content-Type'] = 'multipart/form-data'

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers, params=parameters)

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return HLRLookupResponse(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def phone_verify(self,
                     number,
                     code_length=None,
                     country_code=None,
                     language_code=None,
                     playback_delay=None,
                     security_code=None):
        """Does a POST request to /phone-verify.

        Make an automated call to any valid phone number and playback a unique
        security code. See: https://www.neutrinoapi.com/api/phone-verify/

        Args:
            number (string): The phone number to send the verification code
                to
            code_length (int, optional): The number of digits to use in the
                security code (between 4 and 12)
            country_code (string, optional): ISO 2-letter country code, assume
                numbers are based in this country. If not set numbers are
                assumed to be in international format (with or without the
                leading + sign)
            language_code (string, optional): The language to playback the
                verification code in, available languages are: de - German, en
                - English, es - Spanish, fr - Fench, it - Italian, pt -
                Portuguese, ru - Russian
            playback_delay (int, optional): The delay in milliseconds between
                the playback of each security code
            security_code (int, optional): Pass in your own security code.
                This is useful if you have implemented TOTP or similar 2FA
                methods. If not set then we will generate a secure random code
                (only numerical security codes are currently supported)

        Returns:
            PhoneVerifyResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/phone-verify"

        # Process optional query parameters
        query_parameters = {
            "user-id": self.__user_id,
            "api-key": self.__api_key
        }
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, query_parameters)

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "APIMATIC 2.0",
            "accept": "application/json"
        }

        # Prepare parameters
        parameters = {
            "number": number,
            "output-case": output_case,
            "code-length":  code_length if code_length is not None else 6,
            "country-code": country_code,
            "language-code":  language_code if language_code is not None else "en",
            "playback-delay":  playback_delay if playback_delay is not None else 800,
            "security-code": security_code
        }
        # The body will be multipart data, so set the header
        headers['Content-Type'] = 'multipart/form-data'

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers, params=parameters)

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return PhoneVerifyResponse(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def sms_verify(self,
                   number,
                   code_length=None,
                   country_code=None,
                   language_code=None,
                   security_code=None):
        """Does a POST request to /sms-verify.

        Send a unique security code to any mobile device via SMS. See:
        https://www.neutrinoapi.com/api/sms-verify/

        Args:
            number (string): The phone number to send a verification code to
            code_length (int, optional): The number of digits to use in the
                security code (must be between 4 and 12)
            country_code (string, optional): ISO 2-letter country code, assume
                numbers are based in this country. If not set numbers are
                assumed to be in international format (with or without the
                leading + sign)
            language_code (string, optional): The language to send the
                verification code in, available languages are: de - German, en
                - English, es - Spanish, fr - Fench, it - Italian, pt -
                Portuguese, ru - Russian
            security_code (int, optional): ass in your own security code. This
                is useful if you have implemented TOTP or similar 2FA methods.
                If not set then we will generate a secure random code (only
                numerical security codes are currently supported)

        Returns:
            SMSVerifyResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/sms-verify"

        # Process optional query parameters
        query_parameters = {
            "user-id": self.__user_id,
            "api-key": self.__api_key
        }
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, query_parameters)

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "APIMATIC 2.0",
            "accept": "application/json"
        }

        # Prepare parameters
        parameters = {
            "number": number,
            "output-case": output_case,
            "code-length":  code_length if code_length is not None else 5,
            "country-code": country_code,
            "language-code":  language_code if language_code is not None else "en",
            "security-code": security_code
        }
        # The body will be multipart data, so set the header
        headers['Content-Type'] = 'multipart/form-data'

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers, params=parameters)

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return SMSVerifyResponse(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 
