# -*- coding: utf-8 -*-

"""
   NeutrinoAPILib.Models.PhonePlaybackResponse
 
   This file was automatically generated for NeutrinoAPI.com by APIMATIC BETA v2.0 on 01/07/2016
"""
from NeutrinoAPILib.APIHelper import APIHelper

class PhonePlaybackResponse(object):

    """Implementation of the 'Phone Playback Response' model.

    TODO: type model description here.

    Attributes:
        calling (bool): True if the call is being made now
        number_valid (bool): Is this a valid phone number

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the PhonePlaybackResponse class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    calling -- bool -- Sets the attribute calling
                    number-valid -- bool -- Sets the attribute number_valid
        
        """
        # Set all of the parameters to their default values
        self.calling = None
        self.number_valid = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "calling": "calling",
            "number-valid": "number_valid",
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
            "calling": "calling",
            "number_valid": "number-valid",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)