# -*- coding: utf-8 -*-

"""
    neutrino_api

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
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
            up the address such as road, city, state, etc
        country_code_3 (string): The ISO 3-letter country code of the
            location
        currency_code (string): ISO 4217 currency code associated with the
            country
        location_type (string): The detected location type ordered roughly
            from most to least precise, possible values
            are:<br/><ul><li>address - indicates a precise street
            address</li><li>street - accurate to the street level but may not
            point to the exact location of the house/building
            number</li><li>city - accurate to the city level, this includes
            villages, towns, suburbs, etc</li><li>postal-code - indicates a
            postal code area (no house or street information
            present)</li><li>railway - location is part of a rail network such
            as a station or railway track</li><li>natural - indicates a
            natural feature, for example a mountain peak or a
            waterway</li><li>island - location is an island or
            archipelago</li><li>administrative - indicates an administrative
            boundary such as a country, state or province</li></ul>
        location_tags (list of string): Array of strings containing any
            location tags associated with the address. Tags are additional
            pieces of metadata about a specific location, there are thousands
            of different tags. Some examples of tags: shop, office, cafe,
            bank, pub

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
        "address_components":'addressComponents',
        "country_code_3":'countryCode3',
        "currency_code":'currencyCode',
        "location_type":'locationType',
        "location_tags":'locationTags'
    }

    def __init__(self,
                 country=None,
                 found=None,
                 address=None,
                 city=None,
                 country_code=None,
                 postal_code=None,
                 state=None,
                 address_components=None,
                 country_code_3=None,
                 currency_code=None,
                 location_type=None,
                 location_tags=None):
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
        self.country_code_3 = country_code_3
        self.currency_code = currency_code
        self.location_type = location_type
        self.location_tags = location_tags


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
        country_code_3 = dictionary.get('countryCode3')
        currency_code = dictionary.get('currencyCode')
        location_type = dictionary.get('locationType')
        location_tags = dictionary.get('locationTags')

        # Return an object of this model
        return cls(country,
                   found,
                   address,
                   city,
                   country_code,
                   postal_code,
                   state,
                   address_components,
                   country_code_3,
                   currency_code,
                   location_type,
                   location_tags)


