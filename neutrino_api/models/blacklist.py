# -*- coding: utf-8 -*-

"""
    neutrino_api.models.blacklist

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io )
"""


class Blacklist(object):

    """Implementation of the 'Blacklist' model.

    TODO: type model description here.

    Attributes:
        is_listed (bool): true if listed, false if not
        list_host (string): the domain/hostname of the DNSBL
        list_rating (int): the list rating [1-3] with 1 being the best rating
            and 3 the lowest rating
        list_name (string): the name of the DNSBL
        txt_record (string): the TXT record returned for this listing (if
            listed)
        response_time (int): the DNSBL server response time in milliseconds

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_listed":'isListed',
        "list_host":'listHost',
        "list_rating":'listRating',
        "list_name":'listName',
        "txt_record":'txtRecord',
        "response_time":'responseTime'
    }

    def __init__(self,
                 is_listed=None,
                 list_host=None,
                 list_rating=None,
                 list_name=None,
                 txt_record=None,
                 response_time=None):
        """Constructor for the Blacklist class"""

        # Initialize members of the class
        self.is_listed = is_listed
        self.list_host = list_host
        self.list_rating = list_rating
        self.list_name = list_name
        self.txt_record = txt_record
        self.response_time = response_time


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
        is_listed = dictionary.get('isListed')
        list_host = dictionary.get('listHost')
        list_rating = dictionary.get('listRating')
        list_name = dictionary.get('listName')
        txt_record = dictionary.get('txtRecord')
        response_time = dictionary.get('responseTime')

        # Return an object of this model
        return cls(is_listed,
                   list_host,
                   list_rating,
                   list_name,
                   txt_record,
                   response_time)


