# -*- coding: utf-8 -*-

"""
    neutrino_api.models.bad_word_filter_response

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io )
"""


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

    # Create a mapping from Model property names to API property names
    _names = {
        "bad_words_list":'badWordsList',
        "bad_words_total":'badWordsTotal',
        "censored_content":'censoredContent',
        "is_bad":'isBad'
    }

    def __init__(self,
                 bad_words_list=None,
                 bad_words_total=None,
                 censored_content=None,
                 is_bad=None):
        """Constructor for the BadWordFilterResponse class"""

        # Initialize members of the class
        self.bad_words_list = bad_words_list
        self.bad_words_total = bad_words_total
        self.censored_content = censored_content
        self.is_bad = is_bad


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
        bad_words_list = dictionary.get('badWordsList')
        bad_words_total = dictionary.get('badWordsTotal')
        censored_content = dictionary.get('censoredContent')
        is_bad = dictionary.get('isBad')

        # Return an object of this model
        return cls(bad_words_list,
                   bad_words_total,
                   censored_content,
                   is_bad)


