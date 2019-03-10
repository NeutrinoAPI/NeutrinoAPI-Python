# -*- coding: utf-8 -*-

"""
    neutrino_api

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""

from neutrino_api.api_helper import APIHelper
from neutrino_api.configuration import Configuration
from neutrino_api.controllers.base_controller import BaseController
from neutrino_api.http.auth.custom_query_auth import CustomQueryAuth
from neutrino_api.models.host_reputation_response import HostReputationResponse
from neutrino_api.models.ip_probe_response import IPProbeResponse
from neutrino_api.models.ip_blocklist_response import IPBlocklistResponse
from neutrino_api.models.email_verify_response import EmailVerifyResponse

class SecurityAndNetworking(BaseController):

    """A Controller to access Endpoints in the neutrino_api API."""


    def host_reputation(self,
                        host,
                        list_rating=3):
        """Does a POST request to /host-reputation.

        Check the reputation of an IP address, domain name, FQDN or URL
        against a comprehensive list of blacklists and blocklists. See:
        https://www.neutrinoapi.com/api/host-reputation/

        Args:
            host (string): An IP address, domain name, FQDN or URL.<br/>If you
                supply a domain/URL it will be checked against the URI DNSBL
                lists
            list_rating (int, optional): Only check lists with this rating or
                better

        Returns:
            HostReputationResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/host-reputation'
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
            'host': host,
            'list-rating': list_rating
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, HostReputationResponse.from_dictionary)

    def ip_probe(self,
                 ip):
        """Does a POST request to /ip-probe.

        Analyze and extract provider information for an IP address. See:
        https://www.neutrinoapi.com/api/ip-probe/

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
        _url_path = '/ip-probe'
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
        addresses. See: https://www.neutrinoapi.com/api/ip-blocklist/

        Args:
            ip (string): An IPv4 or IPv6 address

        Returns:
            IPBlocklistResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/ip-blocklist'
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
                     fix_typos=False):
        """Does a POST request to /email-verify.

        SMTP based email address verification. See:
        https://www.neutrinoapi.com/api/email-verify/

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
        _url_path = '/email-verify'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'email': email,
            'output-case': 'camel',
            'fix-typos': fix_typos
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, EmailVerifyResponse.from_dictionary)
