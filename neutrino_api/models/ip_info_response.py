# -*- coding: utf-8 -*-

"""
    neutrino_api

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""


class IPInfoResponse(object):

    """Implementation of the 'IP Info Response' model.

    TODO: type model description here.

    Attributes:
        valid (bool): Is this a valid IPv4 or IPv6 address
        country (string): Full country name
        hostname (string): The IPs full hostname (only set if reverse-lookup
            has been used)
        city (string): Name of the city (if detectable)
        country_code (string): ISO 2-letter country code
        latitude (int): Location latitude
        region (string): Name of the region (if detectable)
        longitude (int): Location longitude
        continent_code (string): ISO 2-letter continent code
        ip (string): The IP address
        country_code_3 (string): ISO 3-letter country code
        currency_code (string): ISO 4217 currency code associated with the
            country
        host_domain (string): The IPs host domain (only set if reverse-lookup
            has been used)
        timezone (dict<object, string>): Map containing timezone details for
            the location: <ul> <li>id - the time zone ID as per the IANA time
            zone database (tzdata)</li> <li>name - the time zone name</li>
            <li>abbr - the time zone abbreviation</li> <li>date - the current
            date within the time zone (ISO format)</li> <li>time - the current
            time within the time zone (ISO format)</li> </ul>

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "valid":'valid',
        "country":'country',
        "hostname":'hostname',
        "city":'city',
        "country_code":'countryCode',
        "latitude":'latitude',
        "region":'region',
        "longitude":'longitude',
        "continent_code":'continentCode',
        "ip":'ip',
        "country_code_3":'countryCode3',
        "currency_code":'currencyCode',
        "host_domain":'hostDomain',
        "timezone":'timezone'
    }

    def __init__(self,
                 valid=None,
                 country=None,
                 hostname=None,
                 city=None,
                 country_code=None,
                 latitude=None,
                 region=None,
                 longitude=None,
                 continent_code=None,
                 ip=None,
                 country_code_3=None,
                 currency_code=None,
                 host_domain=None,
                 timezone=None):
        """Constructor for the IPInfoResponse class"""

        # Initialize members of the class
        self.valid = valid
        self.country = country
        self.hostname = hostname
        self.city = city
        self.country_code = country_code
        self.latitude = latitude
        self.region = region
        self.longitude = longitude
        self.continent_code = continent_code
        self.ip = ip
        self.country_code_3 = country_code_3
        self.currency_code = currency_code
        self.host_domain = host_domain
        self.timezone = timezone


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
        valid = dictionary.get('valid')
        country = dictionary.get('country')
        hostname = dictionary.get('hostname')
        city = dictionary.get('city')
        country_code = dictionary.get('countryCode')
        latitude = dictionary.get('latitude')
        region = dictionary.get('region')
        longitude = dictionary.get('longitude')
        continent_code = dictionary.get('continentCode')
        ip = dictionary.get('ip')
        country_code_3 = dictionary.get('countryCode3')
        currency_code = dictionary.get('currencyCode')
        host_domain = dictionary.get('hostDomain')
        timezone = dictionary.get('timezone')

        # Return an object of this model
        return cls(valid,
                   country,
                   hostname,
                   city,
                   country_code,
                   latitude,
                   region,
                   longitude,
                   continent_code,
                   ip,
                   country_code_3,
                   currency_code,
                   host_domain,
                   timezone)


