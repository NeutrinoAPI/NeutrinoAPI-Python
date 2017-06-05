# -*- coding: utf-8 -*-

"""
   neutrino_api.configuration

   This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io )
"""
from .api_helper import APIHelper

class Configuration(object):

    """A class used for configuring the SDK by a user.

    This class need not be instantiated and all properties and methods
    are accessible without instance creation.

    """

    # Set the array parameter serialization method
    # (allowed: indexed, unindexed, plain, csv, tsv, psv)
    array_serialization = "indexed"

    # The base Uri for API calls
    base_uri = 'https://neutrinoapi.com'

    # Your user ID
    # TODO: Set an appropriate value
    user_id = "TODO: Replace"

    # Your API key
    # TODO: Set an appropriate value
    api_key = "TODO: Replace"

