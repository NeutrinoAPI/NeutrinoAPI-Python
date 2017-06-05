# -*- coding: utf-8 -*-

"""
    neutrino_api.models.verify_security_code_response

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io )
"""


class VerifySecurityCodeResponse(object):

    """Implementation of the 'Verify Security Code Response' model.

    TODO: type model description here.

    Attributes:
        verified (bool): True if the code is valid

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "verified" : "verified"
    }

    def __init__(self,
                 verified=None):
        """Constructor for the VerifySecurityCodeResponse class"""

        # Initialize members of the class
        self.verified = verified


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
        verified = dictionary.get("verified")

        # Return an object of this model
        return cls(verified)


