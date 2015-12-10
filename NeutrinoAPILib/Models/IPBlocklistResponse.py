# -*- coding: utf-8 -*-

"""
   NeutrinoAPILib.Models.IPBlocklistResponse
 
   This file was automatically generated for NeutrinoAPI.com by APIMATIC BETA v2.0 on 12/10/2015
"""
from NeutrinoAPILib.APIHelper import APIHelper

class IPBlocklistResponse(object):

    """Implementation of the 'IP Blocklist Response' model.

    TODO: type model description here.

    Attributes:
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

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the IPBlocklistResponse class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    isBot -- bool -- Sets the attribute is_bot
                    isExploitBot -- bool -- Sets the attribute is_exploit_bot
                    isMalware -- bool -- Sets the attribute is_malware
                    isSpider -- bool -- Sets the attribute is_spider
                    isDshield -- bool -- Sets the attribute is_dshield
                    listCount -- int -- Sets the attribute list_count
                    isProxy -- bool -- Sets the attribute is_proxy
                    isHijacked -- bool -- Sets the attribute is_hijacked
                    isTor -- bool -- Sets the attribute is_tor
                    isSpyware -- bool -- Sets the attribute is_spyware
                    isSpamBot -- bool -- Sets the attribute is_spam_bot
                    isListed -- bool -- Sets the attribute is_listed
                    isVpn -- bool -- Sets the attribute is_vpn
        
        """
        # Set all of the parameters to their default values
        self.is_bot = None
        self.is_exploit_bot = None
        self.is_malware = None
        self.is_spider = None
        self.is_dshield = None
        self.list_count = None
        self.is_proxy = None
        self.is_hijacked = None
        self.is_tor = None
        self.is_spyware = None
        self.is_spam_bot = None
        self.is_listed = None
        self.is_vpn = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "isBot": "is_bot",
            "isExploitBot": "is_exploit_bot",
            "isMalware": "is_malware",
            "isSpider": "is_spider",
            "isDshield": "is_dshield",
            "listCount": "list_count",
            "isProxy": "is_proxy",
            "isHijacked": "is_hijacked",
            "isTor": "is_tor",
            "isSpyware": "is_spyware",
            "isSpamBot": "is_spam_bot",
            "isListed": "is_listed",
            "isVpn": "is_vpn",
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
            "is_bot": "isBot",
            "is_exploit_bot": "isExploitBot",
            "is_malware": "isMalware",
            "is_spider": "isSpider",
            "is_dshield": "isDshield",
            "list_count": "listCount",
            "is_proxy": "isProxy",
            "is_hijacked": "isHijacked",
            "is_tor": "isTor",
            "is_spyware": "isSpyware",
            "is_spam_bot": "isSpamBot",
            "is_listed": "isListed",
            "is_vpn": "isVpn",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)