# -*- coding: utf-8 -*-

"""
    neutrino_api.models.ip_info_response

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io )
"""


class IPInfoResponse(object):

    """Implementation of the 'IP Info Response' model.

    TODO: type model description here.

    Attributes:
        valid (bool): Is this a valid IP address
        country (string): Full country name
        hostname (string): The IPs hostname (only set if reverse-lookup has
            been used)
        city (string): Full city name (if detectable)
        country_code (string): ISO 2-letter country code
        latitude (float): Location latitude
        region (string): Full region name (if detectable)
        longitude (float): Location longitude

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "valid" : "valid",
        "country" : "country",
        "hostname" : "hostname",
        "city" : "city",
        "country_code" : "countryCode",
        "latitude" : "latitude",
        "region" : "region",
        "longitude" : "longitude"
    }

    def __init__(self,
                 valid=None,
                 country=None,
                 hostname=None,
                 city=None,
                 country_code=None,
                 latitude=None,
                 region=None,
                 longitude=None):
        """Constructor for the IPInfoResponse class"""

        # Initialize members of the class
        self.valid = valid
        self.country = country
        self.hostname = hostname
        self.city = city
        self.country_code = country_code
        self.latitude = latitude
        self.region = region
        self.longitude = longitude


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        valid = dictionary.get("valid")
        country = dictionary.get("country")
        hostname = dictionary.get("hostname")
        city = dictionary.get("city")
        country_code = dictionary.get("countryCode")
        latitude = dictionary.get("latitude")
        region = dictionary.get("region")
        longitude = dictionary.get("longitude")

        # Return an object of this model
        return cls(valid,
                   country,
                   hostname,
                   city,
                   country_code,
                   latitude,
                   region,
                   longitude)


