# -*- coding: utf-8 -*-

"""
   neutrino_api.http.auth.custom_query_auth

   This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io )
"""

from ...configuration import Configuration

class CustomQueryAuth:

    @staticmethod
    def apply(http_request):
        """ Add custom authentication to the request.

        Args:
            http_request (HttpRequest): The HttpRequest object to which 
                authentication will be added.

        """                
        http_request.query_parameters["user-id"] = Configuration.user_id
        http_request.query_parameters["api-key"] = Configuration.api_key
