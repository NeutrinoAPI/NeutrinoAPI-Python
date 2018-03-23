# -*- coding: utf-8 -*-

"""
    neutrino_api.models.ip_blocklist_response

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io )
"""


class IPBlocklistResponse(object):

    """Implementation of the 'IP Blocklist Response' model.

    TODO: type model description here.

    Attributes:
        ip (string): The IP address
        is_bot (bool): IP is hosting a malicious bot or is part of a botnet
        is_exploit_bot (bool): IP is hosting an exploit finding bot or exploit
            scanning software
        is_malware (bool): IP is involved in distributing malware
        is_spider (bool): IP is a hostile spider or crawler
        is_dshield (bool): IP has been flagged on DShield (dshield.org)
        list_count (int): The number of blocklists the IP is listed on
        is_proxy (bool): IP has been detected as an anonymous web proxy or
            anonymous HTTP proxy
        is_hijacked (bool): hijacked netblocks or netblocks controlled by
            criminal organizations
        is_tor (bool): IP is coming from a Tor node
        is_spyware (bool): IP is being used by spyware, malware, botnets or
            for other malicious activities
        is_spam_bot (bool): IP address is hosting a spam bot, comment spamming
            or other spamming software
        is_listed (bool): Is this IP on a blocklist
        is_vpn (bool): IP has been detected as coming from a VPN hosting
            provider
        last_seen (int): The last time this IP was seen on a blocklist (in
            Unix time or 0 if not listed recently)
        blocklists (list of string): An array of strings indicating which
            blocklists this IP is listed on (empty if not listed)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ip":'ip',
        "is_bot":'isBot',
        "is_exploit_bot":'isExploitBot',
        "is_malware":'isMalware',
        "is_spider":'isSpider',
        "is_dshield":'isDshield',
        "list_count":'listCount',
        "is_proxy":'isProxy',
        "is_hijacked":'isHijacked',
        "is_tor":'isTor',
        "is_spyware":'isSpyware',
        "is_spam_bot":'isSpamBot',
        "is_listed":'isListed',
        "is_vpn":'isVpn',
        "last_seen":'lastSeen',
        "blocklists":'blocklists'
    }

    def __init__(self,
                 ip=None,
                 is_bot=None,
                 is_exploit_bot=None,
                 is_malware=None,
                 is_spider=None,
                 is_dshield=None,
                 list_count=None,
                 is_proxy=None,
                 is_hijacked=None,
                 is_tor=None,
                 is_spyware=None,
                 is_spam_bot=None,
                 is_listed=None,
                 is_vpn=None,
                 last_seen=None,
                 blocklists=None):
        """Constructor for the IPBlocklistResponse class"""

        # Initialize members of the class
        self.ip = ip
        self.is_bot = is_bot
        self.is_exploit_bot = is_exploit_bot
        self.is_malware = is_malware
        self.is_spider = is_spider
        self.is_dshield = is_dshield
        self.list_count = list_count
        self.is_proxy = is_proxy
        self.is_hijacked = is_hijacked
        self.is_tor = is_tor
        self.is_spyware = is_spyware
        self.is_spam_bot = is_spam_bot
        self.is_listed = is_listed
        self.is_vpn = is_vpn
        self.last_seen = last_seen
        self.blocklists = blocklists


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
        ip = dictionary.get('ip')
        is_bot = dictionary.get('isBot')
        is_exploit_bot = dictionary.get('isExploitBot')
        is_malware = dictionary.get('isMalware')
        is_spider = dictionary.get('isSpider')
        is_dshield = dictionary.get('isDshield')
        list_count = dictionary.get('listCount')
        is_proxy = dictionary.get('isProxy')
        is_hijacked = dictionary.get('isHijacked')
        is_tor = dictionary.get('isTor')
        is_spyware = dictionary.get('isSpyware')
        is_spam_bot = dictionary.get('isSpamBot')
        is_listed = dictionary.get('isListed')
        is_vpn = dictionary.get('isVpn')
        last_seen = dictionary.get('lastSeen')
        blocklists = dictionary.get('blocklists')

        # Return an object of this model
        return cls(ip,
                   is_bot,
                   is_exploit_bot,
                   is_malware,
                   is_spider,
                   is_dshield,
                   list_count,
                   is_proxy,
                   is_hijacked,
                   is_tor,
                   is_spyware,
                   is_spam_bot,
                   is_listed,
                   is_vpn,
                   last_seen,
                   blocklists)


