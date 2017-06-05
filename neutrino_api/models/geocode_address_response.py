# -*- coding: utf-8 -*-

"""
    neutrino_api.models.geocode_address_response

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io )
"""
import neutrino_api.models.location

class GeocodeAddressResponse(object):

    """Implementation of the 'Geocode Address Response' model.

    TODO: type model description here.

    Attributes:
        found (int): The number of possible matching locations found
        locations (list of Location): Array of matching location objects

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "found" : "found",
        "locations" : "locations"
    }

    def __init__(self,
                 found=None,
                 locations=None):
        """Constructor for the GeocodeAddressResponse class"""

        # Initialize members of the class
        self.found = found
        self.locations = locations


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
        found = dictionary.get("found")
        locations = None
        if dictionary.get("locations") != None:
            locations = list()
            for structure in dictionary.get("locations"):
                locations.append(neutrino_api.models.location.Location.from_dictionary(structure))

        # Return an object of this model
        return cls(found,
                   locations)


