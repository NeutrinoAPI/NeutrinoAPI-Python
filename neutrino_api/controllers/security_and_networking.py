# -*- coding: utf-8 -*-

"""
    neutrino_api.controllers.security_and_networking

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.custom_query_auth import CustomQueryAuth
from ..models.host_reputation_response import HostReputationResponse
from ..models.url_info_response import URLInfoResponse
from ..models.ip_probe_response import IPProbeResponse
from ..models.ip_blocklist_response import IPBlocklistResponse
from ..models.email_verify_response import EmailVerifyResponse

class SecurityAndNetworking(BaseController):

    """A Controller to access Endpoints in the neutrino_api API."""


    def host_reputation(self,
                        host):
        """Does a POST request to /host-reputation.

        Check the reputation of an IP address or domain against a
        comprehensive list of blacklists and blocklists (DNSBLs)

        Args:
            host (string): An IPv4 address or a domain name. If you supply a
                domain name it will be checked against the URI DNSBL list

        Returns:
            HostReputationResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/host-reputation'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'output-case': 'camel',
            'host': host
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, HostReputationResponse.from_dictionary)

    def url_info(self,
                 url,
                 fetch_content):
        """Does a POST request to /url-info.

        Parse, analyze and retrieve content from the supplied URL

        Args:
            url (string): The URL to process
            fetch_content (bool): If this URL responds with html, text, json
                or xml then return the response. This option is useful if you
                want to perform further processing on the URL content

        Returns:
            URLInfoResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/url-info'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'output-case': 'camel',
            'url': url,
            'fetch-content': fetch_content
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, URLInfoResponse.from_dictionary)

    def ip_probe(self,
                 ip):
        """Does a POST request to /ip-probe.

        Analyze and extract provider information for an IP address

        Args:
            ip (string): IPv4 or IPv6 address

        Returns:
            IPProbeResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/ip-probe'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'output-case': 'camel',
            'ip': ip
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, IPProbeResponse.from_dictionary)

    def ip_blocklist(self,
                     ip):
        """Does a POST request to /ip-blocklist.

        The IP Blocklist API will detect potentially malicious or dangerous IP
        addresses

        Args:
            ip (string): An IPv4 address

        Returns:
            IPBlocklistResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/ip-blocklist'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'output-case': 'camel',
            'ip': ip
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, IPBlocklistResponse.from_dictionary)

    def email_verify(self,
                     email,
                     fix_typos=None):
        """Does a POST request to /email-verify.

        SMTP based email address verification

        Args:
            email (string): An email address
            fix_typos (bool, optional): Automatically attempt to fix typos in
                the address

        Returns:
            EmailVerifyResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/email-verify'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'email': email,
            'fix-typos': fix_typos
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, EmailVerifyResponse.from_dictionary)
