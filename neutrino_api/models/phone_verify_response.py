# -*- coding: utf-8 -*-

"""
    neutrino_api.models.phone_verify_response

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io )
"""


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

    # Create a mapping from Model property names to API property names
    _names = {
        "number_valid" : "numberValid",
        "calling" : "calling",
        "security_code" : "securityCode"
    }

    def __init__(self,
                 number_valid=None,
                 calling=None,
                 security_code=None):
        """Constructor for the PhoneVerifyResponse class"""

        # Initialize members of the class
        self.number_valid = number_valid
        self.calling = calling
        self.security_code = security_code


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        number_valid = dictionary.get("numberValid")
        calling = dictionary.get("calling")
        security_code = dictionary.get("securityCode")

        # Return an object of this model
        return cls(number_valid,
                   calling,
                   security_code)


