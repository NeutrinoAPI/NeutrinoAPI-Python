# -*- coding: utf-8 -*-

"""
   NeutrinoAPILib.Controllers.ECommerceController

   This file was automatically generated for NeutrinoAPI.com by APIMATIC BETA v2.0 on 01/07/2016
"""
import unirest

from NeutrinoAPILib.APIHelper import APIHelper
from NeutrinoAPILib.Configuration import Configuration
from NeutrinoAPILib.APIException import APIException
from NeutrinoAPILib.Models.BINLookupResponse import BINLookupResponse


class ECommerceController(object):


    """A Controller to access Endpoints in the NeutrinoAPILib API."""

    def __init__(self,
                 user_id,
                 api_key):
        """
        Constructor with authentication and configuration parameters
        """
        self.__user_id = user_id
        self.__api_key = api_key

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
            customer_ip (string, optional): Pass in a customers remote IP
                address. The API will then determine the country of the IP
                address and match it against the BIN country. This feature is
                designed for fraud prevention and detection checks.

        Returns:
            BINLookupResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/bin-lookup"

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
            "bin-number": bin_number,
            "output-case": output_case,
            "customer-ip": customer_ip
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
            return BINLookupResponse(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 
