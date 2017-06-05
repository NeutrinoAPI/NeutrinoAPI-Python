# -*- coding: utf-8 -*-

"""
    neutrino_api.models.bin_lookup_response

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io )
"""


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

    # Create a mapping from Model property names to API property names
    _names = {
        "country" : "country",
        "ip_city" : "ipCity",
        "ip_matches_bin" : "ipMatchesBin",
        "card_type" : "cardType",
        "card_category" : "cardCategory",
        "ip_country_code" : "ipCountryCode",
        "ip_country" : "ipCountry",
        "issuer" : "issuer",
        "ip_blocklisted" : "ipBlocklisted",
        "valid" : "valid",
        "ip_blocklists" : "ipBlocklists",
        "issuer_website" : "issuerWebsite",
        "country_code" : "countryCode",
        "ip_region" : "ipRegion",
        "card_brand" : "cardBrand",
        "issuer_phone" : "issuerPhone"
    }

    def __init__(self,
                 country=None,
                 ip_city=None,
                 ip_matches_bin=None,
                 card_type=None,
                 card_category=None,
                 ip_country_code=None,
                 ip_country=None,
                 issuer=None,
                 ip_blocklisted=None,
                 valid=None,
                 ip_blocklists=None,
                 issuer_website=None,
                 country_code=None,
                 ip_region=None,
                 card_brand=None,
                 issuer_phone=None):
        """Constructor for the BINLookupResponse class"""

        # Initialize members of the class
        self.country = country
        self.ip_city = ip_city
        self.ip_matches_bin = ip_matches_bin
        self.card_type = card_type
        self.card_category = card_category
        self.ip_country_code = ip_country_code
        self.ip_country = ip_country
        self.issuer = issuer
        self.ip_blocklisted = ip_blocklisted
        self.valid = valid
        self.ip_blocklists = ip_blocklists
        self.issuer_website = issuer_website
        self.country_code = country_code
        self.ip_region = ip_region
        self.card_brand = card_brand
        self.issuer_phone = issuer_phone


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
        country = dictionary.get("country")
        ip_city = dictionary.get("ipCity")
        ip_matches_bin = dictionary.get("ipMatchesBin")
        card_type = dictionary.get("cardType")
        card_category = dictionary.get("cardCategory")
        ip_country_code = dictionary.get("ipCountryCode")
        ip_country = dictionary.get("ipCountry")
        issuer = dictionary.get("issuer")
        ip_blocklisted = dictionary.get("ipBlocklisted")
        valid = dictionary.get("valid")
        ip_blocklists = dictionary.get("ipBlocklists")
        issuer_website = dictionary.get("issuerWebsite")
        country_code = dictionary.get("countryCode")
        ip_region = dictionary.get("ipRegion")
        card_brand = dictionary.get("cardBrand")
        issuer_phone = dictionary.get("issuerPhone")

        # Return an object of this model
        return cls(country,
                   ip_city,
                   ip_matches_bin,
                   card_type,
                   card_category,
                   ip_country_code,
                   ip_country,
                   issuer,
                   ip_blocklisted,
                   valid,
                   ip_blocklists,
                   issuer_website,
                   country_code,
                   ip_region,
                   card_brand,
                   issuer_phone)


