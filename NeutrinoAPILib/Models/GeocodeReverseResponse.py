# -*- coding: utf-8 -*-

"""
   NeutrinoAPILib.Models.GeocodeReverseResponse
 
   This file was automatically generated for NeutrinoAPI.com by APIMATIC BETA v2.0 on 12/10/2015
"""
from NeutrinoAPILib.APIHelper import APIHelper

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

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the GeocodeReverseResponse class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    country -- string -- Sets the attribute country
                    found -- bool -- Sets the attribute found
                    address -- string -- Sets the attribute address
                    city -- string -- Sets the attribute city
                    countryCode -- string -- Sets the attribute country_code
                    postalCode -- string -- Sets the attribute postal_code
        
        """
        # Set all of the parameters to their default values
        self.country = None
        self.found = None
        self.address = None
        self.city = None
        self.country_code = None
        self.postal_code = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "country": "country",
            "found": "found",
            "address": "address",
            "city": "city",
            "countryCode": "country_code",
            "postalCode": "postal_code",
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
            "country": "country",
            "found": "found",
            "address": "address",
            "city": "city",
            "country_code": "countryCode",
            "postal_code": "postalCode",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)