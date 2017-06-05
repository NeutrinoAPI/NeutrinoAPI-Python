# -*- coding: utf-8 -*-

"""
    neutrino_api.models.phone_playback_response

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io )
"""


class PhonePlaybackResponse(object):

    """Implementation of the 'Phone Playback Response' model.

    TODO: type model description here.

    Attributes:
        calling (bool): True if the call is being made now
        number_valid (bool): Is this a valid phone number

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "calling" : "calling",
        "number_valid" : "number-valid"
    }

    def __init__(self,
                 calling=None,
                 number_valid=None):
        """Constructor for the PhonePlaybackResponse class"""

        # Initialize members of the class
        self.calling = calling
        self.number_valid = number_valid


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
        calling = dictionary.get("calling")
        number_valid = dictionary.get("number-valid")

        # Return an object of this model
        return cls(calling,
                   number_valid)


