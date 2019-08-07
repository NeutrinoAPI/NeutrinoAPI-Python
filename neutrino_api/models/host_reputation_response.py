# -*- coding: utf-8 -*-

"""
    neutrino_api

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""

import neutrino_api.models.blacklist

class HostReputationResponse(object):

    """Implementation of the 'Host Reputation Response' model.

    TODO: type model description here.

    Attributes:
        is_listed (bool): Is this host blacklisted
        lists (list of Blacklist): An array of objects for each DNSBL checked,
            with the following keys: <ul> <li>is-listed - true if listed,
            false if not</li> <li>list-name - the name of the DNSBL</li>
            <li>list-host - the domain/hostname of the DNSBL</li>
            <li>list-rating - the list rating [1-3] with 1 being the best
            rating and 3 the lowest rating</li> <li>txt-record - the TXT
            record returned for this listing (if listed)</li> <li>return-code
            - the specific return code for this listing (if listed)</li>
            <li>response-time - the DNSBL server response time in
            milliseconds</li> </ul>
        list_count (int): The number of DNSBLs the host is listed on
        host (string): The IP address or host name

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_listed":'isListed',
        "lists":'lists',
        "list_count":'listCount',
        "host":'host'
    }

    def __init__(self,
                 is_listed=None,
                 lists=None,
                 list_count=None,
                 host=None):
        """Constructor for the HostReputationResponse class"""

        # Initialize members of the class
        self.is_listed = is_listed
        self.lists = lists
        self.list_count = list_count
        self.host = host


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
        host = dictionary.get('host')

        # Return an object of this model
        return cls(is_listed,
                   lists,
                   list_count,
                   host)


