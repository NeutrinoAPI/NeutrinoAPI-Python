# -*- coding: utf-8 -*-

"""
   NeutrinoAPILib.Models.BadWordFilterResponse
 
   This file was automatically generated for NeutrinoAPI.com by APIMATIC BETA v2.0 on 01/07/2016
"""
from NeutrinoAPILib.APIHelper import APIHelper

class BadWordFilterResponse(object):

    """Implementation of the 'Bad Word Filter Response' model.

    TODO: type model description here.

    Attributes:
        bad_words_list (list of string): Array of the bad words found
        bad_words_total (int): Total number of bad words detected
        censored_content (string): The censored content (only set if
            censor-character has been set)
        is_bad (bool): Does the text contain bad words

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the BadWordFilterResponse class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    badWordsList -- list of string -- Sets the attribute bad_words_list
                    badWordsTotal -- int -- Sets the attribute bad_words_total
                    censoredContent -- string -- Sets the attribute censored_content
                    isBad -- bool -- Sets the attribute is_bad
        
        """
        # Set all of the parameters to their default values
        self.bad_words_list = None
        self.bad_words_total = None
        self.censored_content = None
        self.is_bad = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "badWordsList": "bad_words_list",
            "badWordsTotal": "bad_words_total",
            "censoredContent": "censored_content",
            "isBad": "is_bad",
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
            "bad_words_list": "badWordsList",
            "bad_words_total": "badWordsTotal",
            "censored_content": "censoredContent",
            "is_bad": "isBad",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)