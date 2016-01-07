# -*- coding: utf-8 -*-

"""
   NeutrinoAPILib.Models.EmailValidateResponse
 
   This file was automatically generated for NeutrinoAPI.com by APIMATIC BETA v2.0 on 01/07/2016
"""
from NeutrinoAPILib.APIHelper import APIHelper

class EmailValidateResponse(object):

    """Implementation of the 'Email Validate Response' model.

    TODO: type model description here.

    Attributes:
        valid (bool): TODO: type description here.
        syntax_error (bool): TODO: type description here.
        domain (string): TODO: type description here.
        domain_error (bool): TODO: type description here.
        is_freemail (bool): TODO: type description here.
        email (string): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the EmailValidateResponse class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    valid -- bool -- Sets the attribute valid
                    syntaxError -- bool -- Sets the attribute syntax_error
                    domain -- string -- Sets the attribute domain
                    domainError -- bool -- Sets the attribute domain_error
                    isFreemail -- bool -- Sets the attribute is_freemail
                    email -- string -- Sets the attribute email
        
        """
        # Set all of the parameters to their default values
        self.valid = None
        self.syntax_error = None
        self.domain = None
        self.domain_error = None
        self.is_freemail = None
        self.email = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "valid": "valid",
            "syntaxError": "syntax_error",
            "domain": "domain",
            "domainError": "domain_error",
            "isFreemail": "is_freemail",
            "email": "email",
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
            "syntax_error": "syntaxError",
            "domain": "domain",
            "domain_error": "domainError",
            "is_freemail": "isFreemail",
            "email": "email",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)