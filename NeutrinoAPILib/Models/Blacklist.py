# -*- coding: utf-8 -*-

"""
   NeutrinoAPILib.Models.Blacklist
 
   This file was automatically generated for NeutrinoAPI.com by APIMATIC BETA v2.0 on 12/10/2015
"""
from NeutrinoAPILib.APIHelper import APIHelper

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

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the Blacklist class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    isListed -- bool -- Sets the attribute is_listed
                    listHost -- string -- Sets the attribute list_host
                    listRating -- int -- Sets the attribute list_rating
                    listName -- string -- Sets the attribute list_name
                    txtRecord -- string -- Sets the attribute txt_record
        
        """
        # Set all of the parameters to their default values
        self.is_listed = None
        self.list_host = None
        self.list_rating = None
        self.list_name = None
        self.txt_record = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "isListed": "is_listed",
            "listHost": "list_host",
            "listRating": "list_rating",
            "listName": "list_name",
            "txtRecord": "txt_record",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

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
            "list_host": "listHost",
            "list_rating": "listRating",
            "list_name": "listName",
            "txt_record": "txtRecord",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)