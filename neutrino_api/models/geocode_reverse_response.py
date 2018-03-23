# -*- coding: utf-8 -*-

"""
    neutrino_api.models.geocode_reverse_response

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io )
"""


class GeocodeReverseResponse(object):

    """Implementation of the 'Geocode Reverse Response' model.

    TODO: type model description here.

    Attributes:
        country (string): The country of the location
        found (bool): True if these coordinates map to a real location
        address (string): The fully formatted address
        city (string): The city of the location
        country_code (string): The ISO 2-letter country code of the location
        postal_code (string): The postal code for the location
        state (string): The state of the location
        address_components (dict<object, string>): The components which make
            up the address such as road, city, state etc. May also include
            additional metadata about the address

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "country":'country',
        "found":'found',
        "address":'address',
        "city":'city',
        "country_code":'countryCode',
        "postal_code":'postalCode',
        "state":'state',
        "address_components":'addressComponents'
    }

    def __init__(self,
                 country=None,
                 found=None,
                 address=None,
                 city=None,
                 country_code=None,
                 postal_code=None,
                 state=None,
                 address_components=None):
        """Constructor for the GeocodeReverseResponse class"""

        # Initialize members of the class
        self.country = country
        self.found = found
        self.address = address
        self.city = city
        self.country_code = country_code
        self.postal_code = postal_code
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
        country = dictionary.get('country')
        found = dictionary.get('found')
        address = dictionary.get('address')
        city = dictionary.get('city')
        country_code = dictionary.get('countryCode')
        postal_code = dictionary.get('postalCode')
        state = dictionary.get('state')
        address_components = dictionary.get('addressComponents')

        # Return an object of this model
        return cls(country,
                   found,
                   address,
                   city,
                   country_code,
                   postal_code,
                   state,
                   address_components)


