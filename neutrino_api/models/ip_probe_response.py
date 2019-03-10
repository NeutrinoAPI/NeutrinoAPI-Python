# -*- coding: utf-8 -*-

"""
    neutrino_api

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""


class IPProbeResponse(object):

    """Implementation of the 'IP Probe Response' model.

    TODO: type model description here.

    Attributes:
        valid (bool): Is this a valid IPv4 or IPv6 address
        country (string): Full country name
        provider_type (string): The detected provider type, possible values
            are:<br/><ul><li>isp - IP belongs to an internet service provider.
            This includes both mobile, home and business internet
            providers</li><li>hosting - IP belongs to a hosting company. This
            includes website hosting, cloud computing platforms and colocation
            facilities</li><li>vpn - IP belongs to a VPN
            provider</li><li>proxy - IP belongs to a proxy service. This
            includes HTTP/SOCKS proxies and browser based
            proxies</li><li>university - IP belongs to a
            university/college/campus</li><li>government - IP belongs to a
            government department. This includes military
            facilities</li><li>commercial - IP belongs to a commercial entity
            such as a corporate headquarters or company office</li><li>unknown
            - could not identify the provider type</li></ul>
        country_code (string): ISO 2-letter country code
        hostname (string): The IPs hostname (PTR)
        provider_domain (string): The domain name of the provider
        city (string): Full city name (if detectable)
        provider_website (string): The website URL for the provider
        ip (string): The IP address
        region (string): Full region name (if detectable)
        provider_description (string): A description of the provider (usually
            extracted from the providers website)
        continent_code (string): ISO 2-letter continent code
        is_hosting (bool): True if this IP belongs to a hosting company. Note
            that this can still be true even if the provider type is
            VPN/proxy, this occurs in the case that the IP is detected as both
            types
        is_isp (bool): True if this IP belongs to an internet service
            provider. Note that this can still be true even if the provider
            type is VPN/proxy, this occurs in the case that the IP is detected
            as both types
        country_code_3 (string): ISO 3-letter country code
        currency_code (string): ISO 4217 currency code associated with the
            country
        is_vpn (bool): True if this IP ia a VPN
        is_proxy (bool): True if this IP ia a proxy
        asn (string): The autonomous system (AS) number
        as_cidr (string): The autonomous system (AS) CIDR range
        as_country_code (string): The autonomous system (AS) ISO 2-letter
            country code
        as_country_code_3 (string): The autonomous system (AS) ISO 3-letter
            country code
        as_domains (list of string): Array of all the domains associated with
            the autonomous system (AS)
        as_description (string): The autonomous system (AS) description /
            company name
        as_age (int): The age of the autonomous system (AS) in number of years
            since registration

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
        "is_isp":'isIsp',
        "country_code_3":'countryCode3',
        "currency_code":'currencyCode',
        "is_vpn":'isVpn',
        "is_proxy":'isProxy',
        "asn":'asn',
        "as_cidr":'asCidr',
        "as_country_code":'asCountryCode',
        "as_country_code_3":'asCountryCode3',
        "as_domains":'asDomains',
        "as_description":'asDescription',
        "as_age":'asAge'
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
                 is_isp=None,
                 country_code_3=None,
                 currency_code=None,
                 is_vpn=None,
                 is_proxy=None,
                 asn=None,
                 as_cidr=None,
                 as_country_code=None,
                 as_country_code_3=None,
                 as_domains=None,
                 as_description=None,
                 as_age=None):
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
        self.country_code_3 = country_code_3
        self.currency_code = currency_code
        self.is_vpn = is_vpn
        self.is_proxy = is_proxy
        self.asn = asn
        self.as_cidr = as_cidr
        self.as_country_code = as_country_code
        self.as_country_code_3 = as_country_code_3
        self.as_domains = as_domains
        self.as_description = as_description
        self.as_age = as_age


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
        country_code_3 = dictionary.get('countryCode3')
        currency_code = dictionary.get('currencyCode')
        is_vpn = dictionary.get('isVpn')
        is_proxy = dictionary.get('isProxy')
        asn = dictionary.get('asn')
        as_cidr = dictionary.get('asCidr')
        as_country_code = dictionary.get('asCountryCode')
        as_country_code_3 = dictionary.get('asCountryCode3')
        as_domains = dictionary.get('asDomains')
        as_description = dictionary.get('asDescription')
        as_age = dictionary.get('asAge')

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
                   is_isp,
                   country_code_3,
                   currency_code,
                   is_vpn,
                   is_proxy,
                   asn,
                   as_cidr,
                   as_country_code,
                   as_country_code_3,
                   as_domains,
                   as_description,
                   as_age)


