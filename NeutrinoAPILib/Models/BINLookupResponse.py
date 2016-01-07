# -*- coding: utf-8 -*-

"""
   NeutrinoAPILib.Models.BINLookupResponse
 
   This file was automatically generated for NeutrinoAPI.com by APIMATIC BETA v2.0 on 01/07/2016
"""
from NeutrinoAPILib.APIHelper import APIHelper

class BINLookupResponse(object):

    """Implementation of the 'BIN Lookup Response' model.

    TODO: type model description here.

    Attributes:
        country (string): Full country name of the issuer
        ip_city (string): The city name (if detectable) from the customer IP
        ip_matches_bin (bool): True if the customer IP address country matches
            the BIN country
        card_type (string): The card type, will always be one of: DEBIT,
            CREDIT, CHARGE CARD
        card_category (string): The card category (if known)
        ip_country_code (string): The ISO 2-letter country code detected from
            the customer IP
        ip_country (string): The country detected from the customer IP
        issuer (string): The card issuer (if known)
        ip_blocklisted (bool): True if the customer IP is listed on one of our
            blocklists, see the IP Blocklist API for more details
        valid (bool): Is this a valid BIN or IIN number
        ip_blocklists (list of string): An array of strings indicating which
            blocklists this IP is listed on
        issuer_website (string): The card issuer website (if known)
        country_code (string): ISO 2-letter country code of the issuer
        ip_region (string): The region name (if detectable) from the customer
            IP
        card_brand (string): The card brand (e.g. Visa or Mastercard)
        issuer_phone (string): The card issuer phone number (if known)

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the BINLookupResponse class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    country -- string -- Sets the attribute country
                    ipCity -- string -- Sets the attribute ip_city
                    ipMatchesBin -- bool -- Sets the attribute ip_matches_bin
                    cardType -- string -- Sets the attribute card_type
                    cardCategory -- string -- Sets the attribute card_category
                    ipCountryCode -- string -- Sets the attribute ip_country_code
                    ipCountry -- string -- Sets the attribute ip_country
                    issuer -- string -- Sets the attribute issuer
                    ipBlocklisted -- bool -- Sets the attribute ip_blocklisted
                    valid -- bool -- Sets the attribute valid
                    ipBlocklists -- list of string -- Sets the attribute ip_blocklists
                    issuerWebsite -- string -- Sets the attribute issuer_website
                    countryCode -- string -- Sets the attribute country_code
                    ipRegion -- string -- Sets the attribute ip_region
                    cardBrand -- string -- Sets the attribute card_brand
                    issuerPhone -- string -- Sets the attribute issuer_phone
        
        """
        # Set all of the parameters to their default values
        self.country = None
        self.ip_city = None
        self.ip_matches_bin = None
        self.card_type = None
        self.card_category = None
        self.ip_country_code = None
        self.ip_country = None
        self.issuer = None
        self.ip_blocklisted = None
        self.valid = None
        self.ip_blocklists = None
        self.issuer_website = None
        self.country_code = None
        self.ip_region = None
        self.card_brand = None
        self.issuer_phone = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "country": "country",
            "ipCity": "ip_city",
            "ipMatchesBin": "ip_matches_bin",
            "cardType": "card_type",
            "cardCategory": "card_category",
            "ipCountryCode": "ip_country_code",
            "ipCountry": "ip_country",
            "issuer": "issuer",
            "ipBlocklisted": "ip_blocklisted",
            "valid": "valid",
            "ipBlocklists": "ip_blocklists",
            "issuerWebsite": "issuer_website",
            "countryCode": "country_code",
            "ipRegion": "ip_region",
            "cardBrand": "card_brand",
            "issuerPhone": "issuer_phone",
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
            "country": "country",
            "ip_city": "ipCity",
            "ip_matches_bin": "ipMatchesBin",
            "card_type": "cardType",
            "card_category": "cardCategory",
            "ip_country_code": "ipCountryCode",
            "ip_country": "ipCountry",
            "issuer": "issuer",
            "ip_blocklisted": "ipBlocklisted",
            "valid": "valid",
            "ip_blocklists": "ipBlocklists",
            "issuer_website": "issuerWebsite",
            "country_code": "countryCode",
            "ip_region": "ipRegion",
            "card_brand": "cardBrand",
            "issuer_phone": "issuerPhone",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)