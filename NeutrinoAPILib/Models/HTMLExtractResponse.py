# -*- coding: utf-8 -*-

"""
   NeutrinoAPILib.Models.HTMLExtractResponse
 
   This file was automatically generated for NeutrinoAPI.com by APIMATIC BETA v2.0 on 01/07/2016
"""
from NeutrinoAPILib.APIHelper import APIHelper

class HTMLExtractResponse(object):

    """Implementation of the 'HTML Extract Response' model.

    TODO: type model description here.

    Attributes:
        total (int): The total number of values extracted
        values (list of string): Array of extracted values

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the HTMLExtractResponse class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    total -- int -- Sets the attribute total
                    values -- list of string -- Sets the attribute values
        
        """
        # Set all of the parameters to their default values
        self.total = None
        self.values = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "total": "total",
            "values": "values",
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
            "total": "total",
            "values": "values",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)