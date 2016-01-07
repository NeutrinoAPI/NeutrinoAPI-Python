# -*- coding: utf-8 -*-

"""
   NeutrinoAPILib.Models.GeocodeAddressResponse
 
   This file was automatically generated for NeutrinoAPI.com by APIMATIC BETA v2.0 on 01/07/2016
"""
from NeutrinoAPILib.APIHelper import APIHelper
from NeutrinoAPILib.Models.Location import Location

class GeocodeAddressResponse(object):

    """Implementation of the 'Geocode Address Response' model.

    TODO: type model description here.

    Attributes:
        found (int): The number of possible matching locations found
        locations (list of Location): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the GeocodeAddressResponse class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    found -- int -- Sets the attribute found
                    locations -- list of Location -- Sets the attribute locations
        
        """
        # Set all of the parameters to their default values
        self.found = None
        self.locations = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "found": "found",
            "locations": "locations",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

            # Other objects also need to be initialised properly
            if "locations" in kwargs:
                # Parameter is an array, so we need to iterate through it
                self.locations = list()
                for item in kwargs["locations"]:
                    self.locations.append(Location(**item))

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
            "found": "found",
            "locations": "locations",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)