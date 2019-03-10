# -*- coding: utf-8 -*-

"""
    neutrino_api

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ConvertResponse(object):

    """Implementation of the 'Convert Response' model.

    TODO: type model description here.

    Attributes:
        valid (bool): True if the coversion was successful and produced a
            valid result
        result (string): The result of the conversion
        from_value (string): The value being converted from
        to_type (string): The type being converted to
        from_type (string): The type of the value being converted from

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "valid":'valid',
        "result":'result',
        "from_value":'fromValue',
        "to_type":'toType',
        "from_type":'fromType'
    }

    def __init__(self,
                 valid=None,
                 result=None,
                 from_value=None,
                 to_type=None,
                 from_type=None):
        """Constructor for the ConvertResponse class"""

        # Initialize members of the class
        self.valid = valid
        self.result = result
        self.from_value = from_value
        self.to_type = to_type
        self.from_type = from_type


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
        valid = dictionary.get('valid')
        result = dictionary.get('result')
        from_value = dictionary.get('fromValue')
        to_type = dictionary.get('toType')
        from_type = dictionary.get('fromType')

        # Return an object of this model
        return cls(valid,
                   result,
                   from_value,
                   to_type,
                   from_type)


