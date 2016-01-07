# -*- coding: utf-8 -*-

"""
   NeutrinoAPILib.Models.HLRLookupResponse
 
   This file was automatically generated for NeutrinoAPI.com by APIMATIC BETA v2.0 on 01/07/2016
"""
from NeutrinoAPILib.APIHelper import APIHelper

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

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the HLRLookupResponse class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    numberValid -- bool -- Sets the attribute number_valid
                    internationalCallingCode -- string -- Sets the attribute international_calling_code
                    mnc -- string -- Sets the attribute mnc
                    numberType -- string -- Sets the attribute number_type
                    hlrValid -- bool -- Sets the attribute hlr_valid
                    hlrStatus -- string -- Sets the attribute hlr_status
                    portedNetwork -- string -- Sets the attribute ported_network
                    imsi -- string -- Sets the attribute imsi
                    mcc -- string -- Sets the attribute mcc
                    internationalNumber -- string -- Sets the attribute international_number
                    localNumber -- string -- Sets the attribute local_number
                    countryCode -- string -- Sets the attribute country_code
                    isPorted -- bool -- Sets the attribute is_ported
                    msin -- string -- Sets the attribute msin
                    location -- string -- Sets the attribute location
                    originNetwork -- string -- Sets the attribute origin_network
                    isMobile -- bool -- Sets the attribute is_mobile
        
        """
        # Set all of the parameters to their default values
        self.number_valid = None
        self.international_calling_code = None
        self.mnc = None
        self.number_type = None
        self.hlr_valid = None
        self.hlr_status = None
        self.ported_network = None
        self.imsi = None
        self.mcc = None
        self.international_number = None
        self.local_number = None
        self.country_code = None
        self.is_ported = None
        self.msin = None
        self.location = None
        self.origin_network = None
        self.is_mobile = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "numberValid": "number_valid",
            "internationalCallingCode": "international_calling_code",
            "mnc": "mnc",
            "numberType": "number_type",
            "hlrValid": "hlr_valid",
            "hlrStatus": "hlr_status",
            "portedNetwork": "ported_network",
            "imsi": "imsi",
            "mcc": "mcc",
            "internationalNumber": "international_number",
            "localNumber": "local_number",
            "countryCode": "country_code",
            "isPorted": "is_ported",
            "msin": "msin",
            "location": "location",
            "originNetwork": "origin_network",
            "isMobile": "is_mobile",
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
            "number_valid": "numberValid",
            "international_calling_code": "internationalCallingCode",
            "mnc": "mnc",
            "number_type": "numberType",
            "hlr_valid": "hlrValid",
            "hlr_status": "hlrStatus",
            "ported_network": "portedNetwork",
            "imsi": "imsi",
            "mcc": "mcc",
            "international_number": "internationalNumber",
            "local_number": "localNumber",
            "country_code": "countryCode",
            "is_ported": "isPorted",
            "msin": "msin",
            "location": "location",
            "origin_network": "originNetwork",
            "is_mobile": "isMobile",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)