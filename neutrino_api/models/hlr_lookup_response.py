# -*- coding: utf-8 -*-

"""
    neutrino_api.models.hlr_lookup_response

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io )
"""


class HLRLookupResponse(object):

    """Implementation of the 'HLR Lookup Response' model.

    TODO: type model description here.

    Attributes:
        number_valid (bool): Is this a valid phone number (mobile or
            otherwise)
        international_calling_code (string): Numbers international calling
            code
        mnc (string): The mobile MNC number (only set if HLR lookup valid)
        number_type (string): The number type, possible values are: mobile,
            fixed-line, premium-rate, toll-free, voip, unknown
        hlr_valid (bool): Was the HLR lookup successful. If true then this is
            a working and registered cell-phone or mobile device (SMS and
            phone calls will be delivered)
        hlr_status (string): The HLR lookup status. See API docs for specific
            status details
        ported_network (string): If the number has been ported, the ported to
            mobile carrier name (only set if HLR lookup valid)
        imsi (string): The mobile IMSI number (only set if HLR lookup valid)
        mcc (string): The mobile MCC number (only set if HLR lookup valid)
        international_number (string): Number represented in international
            format
        local_number (string): Number represented in local format
        country_code (string): Number location ISO 2-letter country code
        is_ported (bool): Has this number been ported to another network
        msin (string): The mobile MSIN number (only set if HLR lookup valid)
        location (string): Number location (could be a city, region or
            country)
        origin_network (string): The origin mobile carrier name (only set if
            HLR lookup valid)
        is_mobile (bool): Is this a mobile number
        is_roaming (bool): Is this number currently roaming from its origin
            country
        country (string): The phone number country

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "number_valid" : "numberValid",
        "international_calling_code" : "internationalCallingCode",
        "mnc" : "mnc",
        "number_type" : "numberType",
        "hlr_valid" : "hlrValid",
        "hlr_status" : "hlrStatus",
        "ported_network" : "portedNetwork",
        "imsi" : "imsi",
        "mcc" : "mcc",
        "international_number" : "internationalNumber",
        "local_number" : "localNumber",
        "country_code" : "countryCode",
        "is_ported" : "isPorted",
        "msin" : "msin",
        "location" : "location",
        "origin_network" : "originNetwork",
        "is_mobile" : "isMobile",
        "is_roaming" : "isRoaming",
        "country" : "country"
    }

    def __init__(self,
                 number_valid=None,
                 international_calling_code=None,
                 mnc=None,
                 number_type=None,
                 hlr_valid=None,
                 hlr_status=None,
                 ported_network=None,
                 imsi=None,
                 mcc=None,
                 international_number=None,
                 local_number=None,
                 country_code=None,
                 is_ported=None,
                 msin=None,
                 location=None,
                 origin_network=None,
                 is_mobile=None,
                 is_roaming=None,
                 country=None):
        """Constructor for the HLRLookupResponse class"""

        # Initialize members of the class
        self.number_valid = number_valid
        self.international_calling_code = international_calling_code
        self.mnc = mnc
        self.number_type = number_type
        self.hlr_valid = hlr_valid
        self.hlr_status = hlr_status
        self.ported_network = ported_network
        self.imsi = imsi
        self.mcc = mcc
        self.international_number = international_number
        self.local_number = local_number
        self.country_code = country_code
        self.is_ported = is_ported
        self.msin = msin
        self.location = location
        self.origin_network = origin_network
        self.is_mobile = is_mobile
        self.is_roaming = is_roaming
        self.country = country


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
        number_valid = dictionary.get("numberValid")
        international_calling_code = dictionary.get("internationalCallingCode")
        mnc = dictionary.get("mnc")
        number_type = dictionary.get("numberType")
        hlr_valid = dictionary.get("hlrValid")
        hlr_status = dictionary.get("hlrStatus")
        ported_network = dictionary.get("portedNetwork")
        imsi = dictionary.get("imsi")
        mcc = dictionary.get("mcc")
        international_number = dictionary.get("internationalNumber")
        local_number = dictionary.get("localNumber")
        country_code = dictionary.get("countryCode")
        is_ported = dictionary.get("isPorted")
        msin = dictionary.get("msin")
        location = dictionary.get("location")
        origin_network = dictionary.get("originNetwork")
        is_mobile = dictionary.get("isMobile")
        is_roaming = dictionary.get("isRoaming")
        country = dictionary.get("country")

        # Return an object of this model
        return cls(number_valid,
                   international_calling_code,
                   mnc,
                   number_type,
                   hlr_valid,
                   hlr_status,
                   ported_network,
                   imsi,
                   mcc,
                   international_number,
                   local_number,
                   country_code,
                   is_ported,
                   msin,
                   location,
                   origin_network,
                   is_mobile,
                   is_roaming,
                   country)


