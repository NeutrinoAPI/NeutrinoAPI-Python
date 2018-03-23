# -*- coding: utf-8 -*-

"""
    neutrino_api.models.api_error_exception

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io )
"""
from ..api_helper import APIHelper
import neutrino_api.exceptions.api_exception

class APIErrorException(neutrino_api.exceptions.api_exception.APIException):
    def __init__(self, reason, context):
        """Constructor for the APIErrorException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            context (HttpContext):  The HttpContext of the API call.

        """
        super(APIErrorException, self).__init__(reason, context)
        dictionary = APIHelper.json_deserialize(self.context.response.raw_body)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)

    def unbox(self, dictionary):
        """Populates the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        self.api_error = dictionary.get('apiError')
        self.api_error_msg = dictionary.get('apiErrorMsg')
