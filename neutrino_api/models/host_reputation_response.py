# -*- coding: utf-8 -*-

"""
    neutrino_api.models.host_reputation_response

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io )
"""
import neutrino_api.models.blacklist

class HostReputationResponse(object):

    """Implementation of the 'Host Reputation Response' model.

    TODO: type model description here.

    Attributes:
        is_listed (bool): Is this host blacklisted
        lists (list of Blacklist): An array of objects for each DNSBL checked
        list_count (int): The number of DNSBL's the host is listed on

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_listed":'isListed',
        "lists":'lists',
        "list_count":'listCount'
    }

    def __init__(self,
                 is_listed=None,
                 lists=None,
                 list_count=None):
        """Constructor for the HostReputationResponse class"""

        # Initialize members of the class
        self.is_listed = is_listed
        self.lists = lists
        self.list_count = list_count


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
        lists = None
        if dictionary.get('lists') != None:
            lists = list()
            for structure in dictionary.get('lists'):
                lists.append(neutrino_api.models.blacklist.Blacklist.from_dictionary(structure))
        list_count = dictionary.get('listCount')

        # Return an object of this model
        return cls(is_listed,
                   lists,
                   list_count)


