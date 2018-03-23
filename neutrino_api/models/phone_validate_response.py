# -*- coding: utf-8 -*-

"""
    neutrino_api.models.phone_validate_response

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io )
"""


class PhoneValidateResponse(object):

    """Implementation of the 'Phone Validate Response' model.

    TODO: type model description here.

    Attributes:
        valid (bool): Is this a valid phone number
        international_calling_code (string): Numbers international calling
            code
        country_code (string): Number location ISO 2-letter country code
        location (string): Number location (could be a city, region or
            country)
        is_mobile (bool): Is this a mobile number
        mtype (string): The number type, possible values are: mobile,
            fixed-line, premium-rate, toll-free, voip, unknown
        international_number (string): Number represented in international
            format
        local_number (string): Number represented in local format
        country (string): The phone number country

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
        "country":'country'
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
                 country=None):
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

        # Return an object of this model
        return cls(valid,
                   international_calling_code,
                   country_code,
                   location,
                   is_mobile,
                   mtype,
                   international_number,
                   local_number,
                   country)


