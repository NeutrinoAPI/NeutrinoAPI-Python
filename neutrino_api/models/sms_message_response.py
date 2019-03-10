# -*- coding: utf-8 -*-

"""
    neutrino_api

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""


class SMSMessageResponse(object):

    """Implementation of the 'SMS Message Response' model.

    TODO: type model description here.

    Attributes:
        number_valid (bool): True if this a valid phone number
        sent (bool): True if the SMS has been sent

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "number_valid":'numberValid',
        "sent":'sent'
    }

    def __init__(self,
                 number_valid=None,
                 sent=None):
        """Constructor for the SMSMessageResponse class"""

        # Initialize members of the class
        self.number_valid = number_valid
        self.sent = sent


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
        number_valid = dictionary.get('numberValid')
        sent = dictionary.get('sent')

        # Return an object of this model
        return cls(number_valid,
                   sent)


