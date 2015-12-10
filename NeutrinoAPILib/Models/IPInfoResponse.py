# -*- coding: utf-8 -*-

"""
   NeutrinoAPILib.Models.IPInfoResponse
 
   This file was automatically generated for NeutrinoAPI.com by APIMATIC BETA v2.0 on 12/10/2015
"""
from NeutrinoAPILib.APIHelper import APIHelper

class IPInfoResponse(object):

    """Implementation of the 'IP Info Response' model.

    TODO: type model description here.

    Attributes:
        valid (bool): Is this a valid IP address
        country (string): Full country name
        hostname (string): IP hostname (if reverse-lookup has been used)
        city (string): Full city name (if detectable)
        country_code (string): ISO 2-letter country code
        latitude (double): Location latitude
        region (string): Full region name (if detectable)
        longitude (double): Location longitude

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the IPInfoResponse class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    valid -- bool -- Sets the attribute valid
                    country -- string -- Sets the attribute country
                    hostname -- string -- Sets the attribute hostname
                    city -- string -- Sets the attribute city
                    countryCode -- string -- Sets the attribute country_code
                    latitude -- double -- Sets the attribute latitude
                    region -- string -- Sets the attribute region
                    longitude -- double -- Sets the attribute longitude
        
        """
        # Set all of the parameters to their default values
        self.valid = None
        self.country = None
        self.hostname = None
        self.city = None
        self.country_code = None
        self.latitude = None
        self.region = None
        self.longitude = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "valid": "valid",
            "country": "country",
            "hostname": "hostname",
            "city": "city",
            "countryCode": "country_code",
            "latitude": "latitude",
            "region": "region",
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
            "valid": "valid",
            "country": "country",
            "hostname": "hostname",
            "city": "city",
            "country_code": "countryCode",
            "latitude": "latitude",
            "region": "region",
            "longitude": "longitude",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)