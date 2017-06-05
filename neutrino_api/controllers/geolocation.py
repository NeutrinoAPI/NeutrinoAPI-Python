# -*- coding: utf-8 -*-

"""
    neutrino_api.controllers.geolocation

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.custom_query_auth import CustomQueryAuth
from ..models.geocode_reverse_response import GeocodeReverseResponse
from ..models.geocode_address_response import GeocodeAddressResponse
from ..models.ip_info_response import IPInfoResponse

class Geolocation(BaseController):

    """A Controller to access Endpoints in the neutrino_api API."""


    def geocode_reverse(self,
                        latitude,
                        longitude,
                        language_code='en'):
        """Does a POST request to /geocode-reverse.

        Convert a geographic coordinate (latitude and longitude) into a real
        world address or location.

        Args:
            latitude (float): The location latitude
            longitude (float): The location longitude
            language_code (string, optional): The language to display results
                in, available languages are: de, en, es, fr, it, pt, ru

        Returns:
            GeocodeReverseResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/geocode-reverse'
        _query_parameters = {

        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
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
            'language-code': language_code
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters,
            Configuration.array_serialization)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GeocodeReverseResponse.from_dictionary)

    def geocode_address(self,
                        address,
                        country_code=None,
                        language_code='en',
                        fuzzy_search=False):
        """Does a POST request to /geocode-address.

        Geocode an address, partial address or the name of a location

        Args:
            address (string): The address or partial address to try and
                locate
            country_code (string, optional): The ISO 2-letter country code to
                be biased towards (default is no country bias)
            language_code (string, optional): The language to display results
                in, available languages are: de, en, es, fr, it, pt, ru
            fuzzy_search (bool, optional): If no matches are found for the
                given address, start performing a recursive fuzzy search until
                a geolocation is found. We use a combination of approximate
                string matching and data cleansing to find possible location
                matches

        Returns:
            GeocodeAddressResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/geocode-address'
        _query_parameters = {

        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
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
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters,
            Configuration.array_serialization)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GeocodeAddressResponse.from_dictionary)

    def ip_info(self,
                ip,
                reverse_lookup=False):
        """Does a POST request to /ip-info.

        Get location information about an IP address and do reverse DNS (PTR)
        lookups.

        Args:
            ip (string): The IP address
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
        _query_builder = Configuration.base_uri
        _query_builder += '/ip-info'
        _query_parameters = {

        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
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
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters,
            Configuration.array_serialization)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, IPInfoResponse.from_dictionary)
