# -*- coding: utf-8 -*-

"""
    neutrino_api

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""

from neutrino_api.api_helper import APIHelper
from neutrino_api.configuration import Configuration
from neutrino_api.controllers.base_controller import BaseController
from neutrino_api.http.auth.custom_query_auth import CustomQueryAuth
from neutrino_api.models.bin_lookup_response import BINLookupResponse

class ECommerce(BaseController):

    """A Controller to access Endpoints in the neutrino_api API."""


    def bin_lookup(self,
                   bin_number,
                   customer_ip=None):
        """Does a POST request to /bin-lookup.

        Perform a BIN (Bank Identification Number) or IIN (Issuer
        Identification Number) lookup. See:
        https://www.neutrinoapi.com/api/bin-lookup/

        Args:
            bin_number (string): The BIN or IIN number (the first 6 digits of
                a credit card number)
            customer_ip (string, optional): Pass in the customers IP address
                and we will return some extra information about them

        Returns:
            BINLookupResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/bin-lookup'
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
            'bin-number': bin_number,
            'customer-ip': customer_ip
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, BINLookupResponse.from_dictionary)
