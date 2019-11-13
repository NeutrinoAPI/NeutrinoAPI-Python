# -*- coding: utf-8 -*-

"""
    neutrino_api

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""

from neutrino_api.api_helper import APIHelper


class Configuration(object):

    """A class used for configuring the SDK by a user.

    This class need not be instantiated and all properties and methods
    are accessible without instance creation.

    """

    # Set the array parameter serialization method
    # (allowed: indexed, unindexed, plain, csv, tsv, psv)
    array_serialization = "indexed"

    # An enum for SDK environments
    class Environment(object):
        # Multicloud endpoint
        MULTICLOUD = 0
        # AWS endpoint
        AWS = 1
        # GCP endpoint
        GCP = 2
        # MS Azure endpoint
        MSA = 3

    # An enum for API servers
    class Server(object):
        DEFAULT = 0

    # The environment in which the SDK is running
    environment = Environment.MULTICLOUD

    # Your user ID
    # TODO: Set an appropriate value
    user_id = None

    # Your API key
    # TODO: Set an appropriate value
    api_key = None


    # All the environments the SDK can run in
    environments = {
        Environment.MULTICLOUD: {
            Server.DEFAULT: 'https://neutrinoapi.net/',
        },
        Environment.AWS: {
            Server.DEFAULT: 'https://aws.neutrinoapi.net/',
        },
        Environment.GCP: {
            Server.DEFAULT: 'https://gcp.neutrinoapi.net/',
        },
        Environment.MSA: {
            Server.DEFAULT: 'https://msa.neutrinoapi.net/',
        },
    }

    @classmethod
    def get_base_uri(cls, server=Server.DEFAULT):
        """Generates the appropriate base URI for the environment and the server.

        Args:
            server (Configuration.Server): The server enum for which the base URI is required.

        Returns:
            String: The base URI.

        """
        return cls.environments[cls.environment][server]
