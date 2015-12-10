# -*- coding: utf-8 -*-

"""
   NeutrinoAPILib.Controllers.GeolocationController

   This file was automatically generated for NeutrinoAPI.com by APIMATIC BETA v2.0 on 12/10/2015
"""
import unirest

from NeutrinoAPILib.APIHelper import APIHelper
from NeutrinoAPILib.Configuration import Configuration
from NeutrinoAPILib.APIException import APIException
from NeutrinoAPILib.Models.IPInfoResponse import IPInfoResponse
from NeutrinoAPILib.Models.GeocodeAddressResponse import GeocodeAddressResponse
from NeutrinoAPILib.Models.GeocodeReverseResponse import GeocodeReverseResponse


class GeolocationController(object):


    """A Controller to access Endpoints in the NeutrinoAPILib API."""

    def __init__(self,
                 user_id,
                 api_key):
        """
        Constructor with authentication and configuration parameters
        """
        self.__user_id = user_id
        self.__api_key = api_key

    def create_ip_info(self,
                       ip,
                       reverse_lookup=None):
        """Does a POST request to /ip-info.

        Get location information about an IP address and do reverse DNS (PTR)
        lookups. See: https://www.neutrinoapi.com/api/ip-info/

        Args:
            ip (string): The IP address
            reverse_lookup (bool, optional): Do reverse DNS (PTR) lookup. This
                option can add extra delay to the request so only use it if
                you need it

        Returns:
            IPInfoResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/ip-info"

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
            "ip": ip,
            "output-case": output_case,
            "reverse-lookup":  reverse_lookup if reverse_lookup is not None else False
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
            return IPInfoResponse(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def create_geocode_address(self,
                               address,
                               country_code=None,
                               language_code=None):
        """Does a POST request to /geocode-address.

        Geocode an address or partial address. See:
        https://www.neutrinoapi.com/api/geocode-address/

        Args:
            address (string): The address or partial address to try and
                locate
            country_code (string, optional): The ISO 2-letter country code to
                be biased towards (default is no country bias)
            language_code (string, optional): The language to display results
                in

        Returns:
            GeocodeAddressResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/geocode-address"

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
            "address": address,
            "output-case": output_case,
            "country-code": country_code,
            "language-code":  language_code if language_code is not None else "en"
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
            return GeocodeAddressResponse(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def create_geocode_reverse(self,
                               latitude,
                               longitude,
                               language_code=None):
        """Does a POST request to /geocode-reverse.

        Reverse geocoding is the process of taking a coordinate (latitude and
        longitude) and mapping this to a real world address or location. See:
        https://www.neutrinoapi.com/api/geocode-reverse/

        Args:
            latitude (double): The location latitude
            longitude (double): The location longitude
            language_code (string, optional): The language to display results
                in

        Returns:
            GeocodeReverseResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/geocode-reverse"

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
            "latitude": latitude,
            "longitude": longitude,
            "output-case": output_case,
            "language-code":  language_code if language_code is not None else "en"
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
            return GeocodeReverseResponse(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 
