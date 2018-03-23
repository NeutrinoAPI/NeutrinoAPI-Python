# -*- coding: utf-8 -*-

"""
    neutrino_api.models.ip_probe_response

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io )
"""


class IPProbeResponse(object):

    """Implementation of the 'IP Probe Response' model.

    TODO: type model description here.

    Attributes:
        valid (bool): Is this a valid IPv4 or IPv6 address
        country (string): Full country name
        provider_type (string): The detected provider type. See online API
            docs for specific provider type details
        country_code (string): ISO 2-letter country code
        hostname (string): The IPs hostname (PTR)
        provider_domain (string): The domain name of the provider
        city (string): Full city name (if detectable)
        provider_website (string): The website URL for the provider
        ip (string): The IP address
        region (string): Full region name (if detectable)
        provider_description (string): A description of the provider, usually
            extracted from the providers website or WHOIS record
        continent_code (string): ISO 2-letter continent code
        is_hosting (bool): True if this IP belongs to a hosting company. Note
            that this can still be true even if the provider type is
            VPN/proxy, this occurs in the case that the IP is detected as both
            types
        is_isp (bool): True if this IP belongs to an ISP. Note that this can
            still be true even if the provider type is VPN/proxy, this occurs
            in the case that the IP is detected as both types

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "valid":'valid',
        "country":'country',
        "provider_type":'providerType',
        "country_code":'countryCode',
        "hostname":'hostname',
        "provider_domain":'providerDomain',
        "city":'city',
        "provider_website":'providerWebsite',
        "ip":'ip',
        "region":'region',
        "provider_description":'providerDescription',
        "continent_code":'continentCode',
        "is_hosting":'isHosting',
        "is_isp":'isIsp'
    }

    def __init__(self,
                 valid=None,
                 country=None,
                 provider_type=None,
                 country_code=None,
                 hostname=None,
                 provider_domain=None,
                 city=None,
                 provider_website=None,
                 ip=None,
                 region=None,
                 provider_description=None,
                 continent_code=None,
                 is_hosting=None,
                 is_isp=None):
        """Constructor for the IPProbeResponse class"""

        # Initialize members of the class
        self.valid = valid
        self.country = country
        self.provider_type = provider_type
        self.country_code = country_code
        self.hostname = hostname
        self.provider_domain = provider_domain
        self.city = city
        self.provider_website = provider_website
        self.ip = ip
        self.region = region
        self.provider_description = provider_description
        self.continent_code = continent_code
        self.is_hosting = is_hosting
        self.is_isp = is_isp


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
        provider_type = dictionary.get('providerType')
        country_code = dictionary.get('countryCode')
        hostname = dictionary.get('hostname')
        provider_domain = dictionary.get('providerDomain')
        city = dictionary.get('city')
        provider_website = dictionary.get('providerWebsite')
        ip = dictionary.get('ip')
        region = dictionary.get('region')
        provider_description = dictionary.get('providerDescription')
        continent_code = dictionary.get('continentCode')
        is_hosting = dictionary.get('isHosting')
        is_isp = dictionary.get('isIsp')

        # Return an object of this model
        return cls(valid,
                   country,
                   provider_type,
                   country_code,
                   hostname,
                   provider_domain,
                   city,
                   provider_website,
                   ip,
                   region,
                   provider_description,
                   continent_code,
                   is_hosting,
                   is_isp)


