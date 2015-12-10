# -*- coding: utf-8 -*-

"""
   NeutrinoAPILib.Models.ConvertResponse
 
   This file was automatically generated for NeutrinoAPI.com by APIMATIC BETA v2.0 on 12/10/2015
"""
from NeutrinoAPILib.APIHelper import APIHelper

class ConvertResponse(object):

    """Implementation of the 'Convert Response' model.

    TODO: type model description here.

    Attributes:
        valid (bool): Was the coversion successful and produced a valid
            result
        result (string): The result of the conversion
        from_value (string): The value being converted from
        to_type (string): The type being converted to
        from_type (string): The type of the value being converted from

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the ConvertResponse class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    valid -- bool -- Sets the attribute valid
                    result -- string -- Sets the attribute result
                    fromValue -- string -- Sets the attribute from_value
                    toType -- string -- Sets the attribute to_type
                    fromType -- string -- Sets the attribute from_type
        
        """
        # Set all of the parameters to their default values
        self.valid = None
        self.result = None
        self.from_value = None
        self.to_type = None
        self.from_type = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "valid": "valid",
            "result": "result",
            "fromValue": "from_value",
            "toType": "to_type",
            "fromType": "from_type",
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
            "result": "result",
            "from_value": "fromValue",
            "to_type": "toType",
            "from_type": "fromType",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)