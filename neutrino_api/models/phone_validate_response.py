# -*- coding: utf-8 -*-

"""
    neutrino_api

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""


class PhoneValidateResponse(object):

    """Implementation of the 'Phone Validate Response' model.

    TODO: type model description here.

    Attributes:
        valid (bool): Is this a valid phone number
        international_calling_code (int): The international calling code
        country_code (string): The phone number country as an ISO 2-letter
            country code
        location (string): The phone number location. Could be a city, region
            or country depending on the type of number
        is_mobile (bool): True if this is a mobile number (only true with 100%
            certainty, if the number type is unknown this value will be
            false)
        mtype (string): The predicted number type.<br/>Note: type detection is
            not possible in some countries which have no predictable prefix
            pattern (you can use the HLR Lookup API in these cases)<br/>
            Possible values
            are:<br/><ul><li>mobile</li><li>fixed-line</li><li>premium-rate</li
            ><li>toll-free</li><li>voip</li><li>unknown (use HLR lookup
            instead)</li></ul>
        international_number (string): The number represented in full
            international format (E.164)
        local_number (string): The number represented in local dialing format
        country (string): The phone number country
        country_code_3 (string): The phone number country as an ISO 3-letter
            country code
        currency_code (string): ISO 4217 currency code associated with the
            country

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "valid":'valid',
        "international_calling_code":'internationalCallingCode',
        "country_code":'countryCode',
        "location":'location',
        "is_mobile":'isMobile',
        "mtype":'type',
        "international_number":'internationalNumber',
        "local_number":'localNumber',
        "country":'country',
        "country_code_3":'countryCode3',
        "currency_code":'currencyCode'
    }

    def __init__(self,
                 valid=None,
                 international_calling_code=None,
                 country_code=None,
                 location=None,
                 is_mobile=None,
                 mtype=None,
                 international_number=None,
                 local_number=None,
                 country=None,
                 country_code_3=None,
                 currency_code=None):
        """Constructor for the PhoneValidateResponse class"""

        # Initialize members of the class
        self.valid = valid
        self.international_calling_code = international_calling_code
        self.country_code = country_code
        self.location = location
        self.is_mobile = is_mobile
        self.mtype = mtype
        self.international_number = international_number
        self.local_number = local_number
        self.country = country
        self.country_code_3 = country_code_3
        self.currency_code = currency_code


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
        valid = dictionary.get('valid')
        international_calling_code = dictionary.get('internationalCallingCode')
        country_code = dictionary.get('countryCode')
        location = dictionary.get('location')
        is_mobile = dictionary.get('isMobile')
        mtype = dictionary.get('type')
        international_number = dictionary.get('internationalNumber')
        local_number = dictionary.get('localNumber')
        country = dictionary.get('country')
        country_code_3 = dictionary.get('countryCode3')
        currency_code = dictionary.get('currencyCode')

        # Return an object of this model
        return cls(valid,
                   international_calling_code,
                   country_code,
                   location,
                   is_mobile,
                   mtype,
                   international_number,
                   local_number,
                   country,
                   country_code_3,
                   currency_code)


