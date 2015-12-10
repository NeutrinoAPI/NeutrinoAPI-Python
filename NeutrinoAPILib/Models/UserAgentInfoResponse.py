# -*- coding: utf-8 -*-

"""
   NeutrinoAPILib.Models.UserAgentInfoResponse
 
   This file was automatically generated for NeutrinoAPI.com by APIMATIC BETA v2.0 on 12/10/2015
"""
from NeutrinoAPILib.APIHelper import APIHelper

class UserAgentInfoResponse(object):

    """Implementation of the 'User Agent Info Response' model.

    TODO: type model description here.

    Attributes:
        mobile_screen_width (int): Mobile device screen width (in px)
        mobile_brand (string): Mobile device brand
        mobile_model (string): Mobile device model
        producer (string): Producer or manufacturer
        browser_name (string): Browser software name
        mobile_screen_height (int): Mobile device screen height (in px)
        is_mobile (bool): True if this is a mobile user-agent
        mtype (string): The user-agent type, possible values are:
            desktop-browser, email-client, feed-reader, software-library,
            media-player, mobile-browser, robot, unknown
        version (string): Software version
        operating_system (string): Operating system
        mobile_browser (string): Mobile device browser

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the UserAgentInfoResponse class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    mobileScreenWidth -- int -- Sets the attribute mobile_screen_width
                    mobileBrand -- string -- Sets the attribute mobile_brand
                    mobileModel -- string -- Sets the attribute mobile_model
                    producer -- string -- Sets the attribute producer
                    browserName -- string -- Sets the attribute browser_name
                    mobileScreenHeight -- int -- Sets the attribute mobile_screen_height
                    isMobile -- bool -- Sets the attribute is_mobile
                    type -- string -- Sets the attribute mtype
                    version -- string -- Sets the attribute version
                    operatingSystem -- string -- Sets the attribute operating_system
                    mobileBrowser -- string -- Sets the attribute mobile_browser
        
        """
        # Set all of the parameters to their default values
        self.mobile_screen_width = None
        self.mobile_brand = None
        self.mobile_model = None
        self.producer = None
        self.browser_name = None
        self.mobile_screen_height = None
        self.is_mobile = None
        self.mtype = None
        self.version = None
        self.operating_system = None
        self.mobile_browser = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "mobileScreenWidth": "mobile_screen_width",
            "mobileBrand": "mobile_brand",
            "mobileModel": "mobile_model",
            "producer": "producer",
            "browserName": "browser_name",
            "mobileScreenHeight": "mobile_screen_height",
            "isMobile": "is_mobile",
            "type": "mtype",
            "version": "version",
            "operatingSystem": "operating_system",
            "mobileBrowser": "mobile_browser",
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
            "mobile_screen_width": "mobileScreenWidth",
            "mobile_brand": "mobileBrand",
            "mobile_model": "mobileModel",
            "producer": "producer",
            "browser_name": "browserName",
            "mobile_screen_height": "mobileScreenHeight",
            "is_mobile": "isMobile",
            "mtype": "type",
            "version": "version",
            "operating_system": "operatingSystem",
            "mobile_browser": "mobileBrowser",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)