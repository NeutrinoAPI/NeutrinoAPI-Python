# -*- coding: utf-8 -*-

"""
    neutrino_api.models.location

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io )
"""


class Location(object):

    """Implementation of the 'Location' model.

    TODO: type model description here.

    Attributes:
        country (string): The country of the location
        address (string): The fully formatted address
        city (string): The city of the location
        country_code (string): The ISO 2-letter country code of the location
        latitude (float): The location latitude
        postal_code (string): The postal code for the location
        longitude (float): The location longitude
        state (string): The state of the location (if applicable)
        address_components (dict<object, string>): The components which make
            up the address such as road, city, state etc. May also include
            additional metadata about the address

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "country" : "country",
        "address" : "address",
        "city" : "city",
        "country_code" : "countryCode",
        "latitude" : "latitude",
        "postal_code" : "postalCode",
        "longitude" : "longitude",
        "state" : "state",
        "address_components" : "addressComponents"
    }

    def __init__(self,
                 country=None,
                 address=None,
                 city=None,
                 country_code=None,
                 latitude=None,
                 postal_code=None,
                 longitude=None,
                 state=None,
                 address_components=None):
        """Constructor for the Location class"""

        # Initialize members of the class
        self.country = country
        self.address = address
        self.city = city
        self.country_code = country_code
        self.latitude = latitude
        self.postal_code = postal_code
        self.longitude = longitude
        self.state = state
        self.address_components = address_components


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
        country = dictionary.get("country")
        address = dictionary.get("address")
        city = dictionary.get("city")
        country_code = dictionary.get("countryCode")
        latitude = dictionary.get("latitude")
        postal_code = dictionary.get("postalCode")
        longitude = dictionary.get("longitude")
        state = dictionary.get("state")
        address_components = dictionary.get("addressComponents")

        # Return an object of this model
        return cls(country,
                   address,
                   city,
                   country_code,
                   latitude,
                   postal_code,
                   longitude,
                   state,
                   address_components)


