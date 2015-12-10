# -*- coding: utf-8 -*-

"""
   NeutrinoAPILib.Models.PhoneValidateResponse
 
   This file was automatically generated for NeutrinoAPI.com by APIMATIC BETA v2.0 on 12/10/2015
"""
from NeutrinoAPILib.APIHelper import APIHelper

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

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the PhoneValidateResponse class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    valid -- bool -- Sets the attribute valid
                    internationalCallingCode -- string -- Sets the attribute international_calling_code
                    countryCode -- string -- Sets the attribute country_code
                    location -- string -- Sets the attribute location
                    isMobile -- bool -- Sets the attribute is_mobile
                    type -- string -- Sets the attribute mtype
                    internationalNumber -- string -- Sets the attribute international_number
                    localNumber -- string -- Sets the attribute local_number
        
        """
        # Set all of the parameters to their default values
        self.valid = None
        self.international_calling_code = None
        self.country_code = None
        self.location = None
        self.is_mobile = None
        self.mtype = None
        self.international_number = None
        self.local_number = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "valid": "valid",
            "internationalCallingCode": "international_calling_code",
            "countryCode": "country_code",
            "location": "location",
            "isMobile": "is_mobile",
            "type": "mtype",
            "internationalNumber": "international_number",
            "localNumber": "local_number",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

    def resolve_names(self):
        """Creates a dictionary representation of this object.
        
        This method converts an object to a dictionary that represents the
        format that the model should be in when passed into an API Request.
        Because of this, the generated dictionary may have different
        property names to that of the model itself.
        
        Returns:
            dict: The dictionary representing the object.
        
        """
        # Create a mapping from Model property names to API property names
        replace_names = {
            "valid": "valid",
            "international_calling_code": "internationalCallingCode",
            "country_code": "countryCode",
            "location": "location",
            "is_mobile": "isMobile",
            "mtype": "type",
            "international_number": "internationalNumber",
            "local_number": "localNumber",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)