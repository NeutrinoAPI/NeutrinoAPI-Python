# -*- coding: utf-8 -*-

"""
   NeutrinoAPILib.Controllers.DataToolsController

   This file was automatically generated for NeutrinoAPI.com by APIMATIC BETA v2.0 on 01/07/2016
"""
import unirest

from NeutrinoAPILib.APIHelper import APIHelper
from NeutrinoAPILib.Configuration import Configuration
from NeutrinoAPILib.APIException import APIException
from NeutrinoAPILib.Models.PhoneValidateResponse import PhoneValidateResponse
from NeutrinoAPILib.Models.UserAgentInfoResponse import UserAgentInfoResponse
from NeutrinoAPILib.Models.BadWordFilterResponse import BadWordFilterResponse
from NeutrinoAPILib.Models.ConvertResponse import ConvertResponse
from NeutrinoAPILib.Models.EmailValidateResponse import EmailValidateResponse
from NeutrinoAPILib.Models.HTMLExtractResponse import HTMLExtractResponse


class DataToolsController(object):


    """A Controller to access Endpoints in the NeutrinoAPILib API."""

    def __init__(self,
                 user_id,
                 api_key):
        """
        Constructor with authentication and configuration parameters
        """
        self.__user_id = user_id
        self.__api_key = api_key

    def phone_validate(self,
                       number,
                       country_code=None):
        """Does a POST request to /phone-validate.

        Parse, validate and get location information about a phone number.
        See: https://www.neutrinoapi.com/api/phone-validate/

        Args:
            number (string): The phone number
            country_code (string, optional): ISO 2-letter country code, assume
                numbers are based in this country. If not set numbers are
                assumed to be in international format (with or without the
                leading + sign)

        Returns:
            PhoneValidateResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/phone-validate"

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
            return PhoneValidateResponse(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def user_agent_info(self,
                        user_agent):
        """Does a POST request to /user-agent-info.

        Parse, validate and get detailed user-agent information from a
        user-agent string. See:
        https://www.neutrinoapi.com/api/user-agent-info/

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
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/user-agent-info"

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
            "user-agent": user_agent
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
            return UserAgentInfoResponse(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def code_highlight(self,
                       content,
                       mtype,
                       add_keyword_links=None):
        """Does a POST request to /code-highlight.

        Code highlight will take raw source code and convert into nicely
        formatted HTML with syntax and keyword highlighting. See:
        https://www.neutrinoapi.com/api/code-highlight/

        Args:
            content (string): The source content. This can be either a URL to
                load from or an actual content string
            mtype (string): The code type. See the API docs for all supported
                types
            add_keyword_links (bool, optional): Add links on source code
                keywords to the relevant language documentation

        Returns:
            binary: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/code-highlight"

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
            "user-agent": "APIMATIC 2.0"
        }

        # Prepare parameters
        parameters = {
            "content": content,
            "type": mtype,
            "add-keyword-links":  add_keyword_links if add_keyword_links is not None else False
        }
        # The body will be multipart data, so set the header
        headers['Content-Type'] = 'multipart/form-data'

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers, params=parameters)

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def bad_word_filter(self,
                        content,
                        censor_character=None):
        """Does a POST request to /bad-word-filter.

        Detect bad words, swear words and profanity in a given text. See:
        https://www.neutrinoapi.com/api/bad-word-filter/

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
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/bad-word-filter"

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
            "content": content,
            "output-case": output_case,
            "censor-character": censor_character
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
            return BadWordFilterResponse(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def convert(self,
                from_type,
                from_value,
                to_type):
        """Does a POST request to /convert.

        A powerful unit and currency conversion tool. See:
        https://www.neutrinoapi.com/api/convert/

        Args:
            from_type (string): The type of the value to convert from
            from_value (string): The value to convert from
            to_type (string): The type to convert to

        Returns:
            ConvertResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/convert"

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
            "from-type": from_type,
            "from-value": from_value,
            "output-case": output_case,
            "to-type": to_type
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
            return ConvertResponse(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def email_validate(self,
                       email,
                       fix_typos=None):
        """Does a POST request to /email-validate.

        Parse, validate and clean an email address. See:
        https://www.neutrinoapi.com/api/email-validate/

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
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/email-validate"

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
            "email": email,
            "output-case": output_case,
            "fix-typos":  fix_typos if fix_typos is not None else False
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
            return EmailValidateResponse(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

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
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/html-clean"

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
            "user-agent": "APIMATIC 2.0"
        }

        # Prepare parameters
        parameters = {
            "content": content,
            "output-type": output_type
        }
        # The body will be multipart data, so set the header
        headers['Content-Type'] = 'multipart/form-data'

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers, params=parameters)

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def html_extract(self,
                     content,
                     tag,
                     attribute=None,
                     base_url=None):
        """Does a POST request to /html-extract-tags.

        Extract HTML tag contents or attributes from complex HTML or XHTML
        content. See: https://www.neutrinoapi.com/api/html-extract-tags/

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
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/html-extract-tags"

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
            "content": content,
            "output-case": output_case,
            "tag": tag,
            "attribute": attribute,
            "base-url": base_url
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
            return HTMLExtractResponse(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 
