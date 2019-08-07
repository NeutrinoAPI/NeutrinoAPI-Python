# -*- coding: utf-8 -*-

"""
    neutrino_api

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""

from neutrino_api.api_helper import APIHelper
from neutrino_api.configuration import Configuration
from neutrino_api.controllers.base_controller import BaseController
from neutrino_api.http.auth.custom_query_auth import CustomQueryAuth
from neutrino_api.models.geocode_reverse_response import GeocodeReverseResponse
from neutrino_api.models.ip_info_response import IPInfoResponse
from neutrino_api.models.geocode_address_response import GeocodeAddressResponse

class Geolocation(BaseController):

    """A Controller to access Endpoints in the neutrino_api API."""


    def geocode_reverse(self,
                        latitude,
                        longitude,
                        language_code='en',
                        zoom='address'):
        """Does a POST request to /geocode-reverse.

        Convert a geographic coordinate (latitude and longitude) into a real
        world address. See: https://www.neutrinoapi.com/api/geocode-reverse/

        Args:
            latitude (string): The location latitude in decimal degrees
                format
            longitude (string): The location longitude in decimal degrees
                format
            language_code (string, optional): The language to display results
                in, available languages are: <ul> <li>de, en, es, fr, it, pt,
                ru</li> </ul>
            zoom (string, optional): The zoom level to respond with: <ul>
                <li>address - the most precise address available</li>
                <li>street - the street level</li> <li>city - the city
                level</li> <li>state - the state level</li> <li>country - the
                country level</li> </ul>

        Returns:
            GeocodeReverseResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/geocode-reverse'
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
            'latitude': latitude,
            'longitude': longitude,
            'language-code': language_code,
            'zoom': zoom
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GeocodeReverseResponse.from_dictionary)

    def ip_info(self,
                ip,
                reverse_lookup=False):
        """Does a POST request to /ip-info.

        Get location information about an IP address and do reverse DNS (PTR)
        lookups. See: https://www.neutrinoapi.com/api/ip-info/

        Args:
            ip (string): IPv4 or IPv6 address
            reverse_lookup (bool, optional): Do a reverse DNS (PTR) lookup.
                This option can add extra delay to the request so only use it
                if you need it

        Returns:
            IPInfoResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/ip-info'
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
            'ip': ip,
            'reverse-lookup': reverse_lookup
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, IPInfoResponse.from_dictionary)

    def geocode_address(self,
                        address,
                        country_code=None,
                        language_code='en',
                        fuzzy_search=False):
        """Does a POST request to /geocode-address.

        Geocode an address, partial address or just the name of a place. See:
        https://www.neutrinoapi.com/api/geocode-address/

        Args:
            address (string): The address, partial address or name of a place
                to try and locate
            country_code (string, optional): The ISO 2-letter country code to
                be biased towards (the default is no country bias)
            language_code (string, optional): The language to display results
                in, available languages are: <ul> <li>de, en, es, fr, it, pt,
                ru</li> </ul>
            fuzzy_search (bool, optional): If no matches are found for the
                given address, start performing a recursive fuzzy search until
                a geolocation is found. This option is recommended for
                processing user input or implementing auto-complete. We use a
                combination of approximate string matching and data cleansing
                to find possible location matches

        Returns:
            GeocodeAddressResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/geocode-address'
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
            'address': address,
            'country-code': country_code,
            'language-code': language_code,
            'fuzzy-search': fuzzy_search
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GeocodeAddressResponse.from_dictionary)
