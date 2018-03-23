# -*- coding: utf-8 -*-

"""
    neutrino_api.models.html_extract_response

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io )
"""


class HTMLExtractResponse(object):

    """Implementation of the 'HTML Extract Response' model.

    TODO: type model description here.

    Attributes:
        total (int): The total number of values extracted
        values (list of string): Array of extracted values

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "total":'total',
        "values":'values'
    }

    def __init__(self,
                 total=None,
                 values=None):
        """Constructor for the HTMLExtractResponse class"""

        # Initialize members of the class
        self.total = total
        self.values = values


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
        total = dictionary.get('total')
        values = dictionary.get('values')

        # Return an object of this model
        return cls(total,
                   values)


