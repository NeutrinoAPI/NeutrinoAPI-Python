# -*- coding: utf-8 -*-

"""
   NeutrinoAPILib.Models.Location
 
   This file was automatically generated for NeutrinoAPI.com by APIMATIC BETA v2.0 on 01/07/2016
"""
from NeutrinoAPILib.APIHelper import APIHelper

class Location(object):

    """Implementation of the 'Location' model.

    TODO: type model description here.

    Attributes:
        country (string): TODO: type description here.
        address (string): TODO: type description here.
        city (string): TODO: type description here.
        country_code (string): TODO: type description here.
        latitude (double): TODO: type description here.
        postal_code (string): TODO: type description here.
        longitude (double): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the Location class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    country -- string -- Sets the attribute country
                    address -- string -- Sets the attribute address
                    city -- string -- Sets the attribute city
                    countryCode -- string -- Sets the attribute country_code
                    latitude -- double -- Sets the attribute latitude
                    postalCode -- string -- Sets the attribute postal_code
                    longitude -- double -- Sets the attribute longitude
        
        """
        # Set all of the parameters to their default values
        self.country = None
        self.address = None
        self.city = None
        self.country_code = None
        self.latitude = None
        self.postal_code = None
        self.longitude = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "country": "country",
            "address": "address",
            "city": "city",
            "countryCode": "country_code",
            "latitude": "latitude",
            "postalCode": "postal_code",
            "longitude": "longitude",
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
            "address": "address",
            "city": "city",
            "country_code": "countryCode",
            "latitude": "latitude",
            "postal_code": "postalCode",
            "longitude": "longitude",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)