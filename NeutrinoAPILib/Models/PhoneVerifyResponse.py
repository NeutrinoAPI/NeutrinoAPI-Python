# -*- coding: utf-8 -*-

"""
   NeutrinoAPILib.Models.PhoneVerifyResponse
 
   This file was automatically generated for NeutrinoAPI.com by APIMATIC BETA v2.0 on 12/10/2015
"""
from NeutrinoAPILib.APIHelper import APIHelper

class PhoneVerifyResponse(object):

    """Implementation of the 'Phone Verify Response' model.

    TODO: type model description here.

    Attributes:
        number_valid (bool): Is this a valid phone number
        calling (bool): True if the call is being made now
        security_code (string): The security code generated, you can save this
            code to perform your own verification or you can use the Verify
            Security Code API

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the PhoneVerifyResponse class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    numberValid -- bool -- Sets the attribute number_valid
                    calling -- bool -- Sets the attribute calling
                    securityCode -- string -- Sets the attribute security_code
        
        """
        # Set all of the parameters to their default values
        self.number_valid = None
        self.calling = None
        self.security_code = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "numberValid": "number_valid",
            "calling": "calling",
            "securityCode": "security_code",
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
            "number_valid": "numberValid",
            "calling": "calling",
            "security_code": "securityCode",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)