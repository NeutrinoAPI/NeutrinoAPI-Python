# -*- coding: utf-8 -*-

"""
   NeutrinoAPILib.Models.HostReputationResponse
 
   This file was automatically generated for NeutrinoAPI.com by APIMATIC BETA v2.0 on 12/10/2015
"""
from NeutrinoAPILib.APIHelper import APIHelper
from NeutrinoAPILib.Models.Blacklist import Blacklist

class HostReputationResponse(object):

    """Implementation of the 'Host Reputation Response' model.

    TODO: type model description here.

    Attributes:
        is_listed (bool): Is this host blacklisted
        lists (list of Blacklist): An array of objects for each DNSBL checked
        list_count (int): The number of DNSBL's the host is listed on

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the HostReputationResponse class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    isListed -- bool -- Sets the attribute is_listed
                    lists -- list of Blacklist -- Sets the attribute lists
                    listCount -- int -- Sets the attribute list_count
        
        """
        # Set all of the parameters to their default values
        self.is_listed = None
        self.lists = None
        self.list_count = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "isListed": "is_listed",
            "lists": "lists",
            "listCount": "list_count",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

            # Other objects also need to be initialised properly
            if "lists" in kwargs:
                # Parameter is an array, so we need to iterate through it
                self.lists = list()
                for item in kwargs["lists"]:
                    self.lists.append(Blacklist(**item))

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
            "is_listed": "isListed",
            "lists": "lists",
            "list_count": "listCount",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)