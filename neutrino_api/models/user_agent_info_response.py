# -*- coding: utf-8 -*-

"""
    neutrino_api

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UserAgentInfoResponse(object):

    """Implementation of the 'User Agent Info Response' model.

    TODO: type model description here.

    Attributes:
        mobile_screen_width (int): The estimated mobile device screen width in
            CSS 'px'
        mobile_brand (string): The mobile device brand
        mobile_model (string): The mobile device model
        producer (string): The producer or manufacturer of the user agent
        browser_name (string): The browser software name
        mobile_screen_height (int): The estimated mobile device screen height
            in CSS 'px'
        is_mobile (bool): True if this is a mobile user agent
        mtype (string): The user agent type, possible values are: <ul>
            <li>desktop-browser</li> <li>mobile-browser</li>
            <li>email-client</li> <li>feed-reader</li>
            <li>software-library</li> <li>media-player (includes smart
            TVs)</li> <li>robot</li> <li>unknown</li> </ul>
        version (string): The browser software version
        operating_system (string): The full operating system name which may
            include the major version number or code name
        mobile_browser (string): The mobile device browser name (this is
            usually the same as the browser name)
        is_android (bool): True if this is an Android based mobile user agent
        is_ios (bool): True if this is an iOS based mobile user agent
        operating_system_family (string): The operating system family name,
            this is the OS name without any version information
        operating_system_version (string): The operating system version number
            (if detectable)
        engine (string): The browser engine name
        engine_version (string): The browser engine version (if detectable)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mobile_screen_width":'mobileScreenWidth',
        "mobile_brand":'mobileBrand',
        "mobile_model":'mobileModel',
        "producer":'producer',
        "browser_name":'browserName',
        "mobile_screen_height":'mobileScreenHeight',
        "is_mobile":'isMobile',
        "mtype":'type',
        "version":'version',
        "operating_system":'operatingSystem',
        "mobile_browser":'mobileBrowser',
        "is_android":'isAndroid',
        "is_ios":'isIos',
        "operating_system_family":'operatingSystemFamily',
        "operating_system_version":'operatingSystemVersion',
        "engine":'engine',
        "engine_version":'engineVersion'
    }

    def __init__(self,
                 mobile_screen_width=None,
                 mobile_brand=None,
                 mobile_model=None,
                 producer=None,
                 browser_name=None,
                 mobile_screen_height=None,
                 is_mobile=None,
                 mtype=None,
                 version=None,
                 operating_system=None,
                 mobile_browser=None,
                 is_android=None,
                 is_ios=None,
                 operating_system_family=None,
                 operating_system_version=None,
                 engine=None,
                 engine_version=None):
        """Constructor for the UserAgentInfoResponse class"""

        # Initialize members of the class
        self.mobile_screen_width = mobile_screen_width
        self.mobile_brand = mobile_brand
        self.mobile_model = mobile_model
        self.producer = producer
        self.browser_name = browser_name
        self.mobile_screen_height = mobile_screen_height
        self.is_mobile = is_mobile
        self.mtype = mtype
        self.version = version
        self.operating_system = operating_system
        self.mobile_browser = mobile_browser
        self.is_android = is_android
        self.is_ios = is_ios
        self.operating_system_family = operating_system_family
        self.operating_system_version = operating_system_version
        self.engine = engine
        self.engine_version = engine_version


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
        mobile_screen_width = dictionary.get('mobileScreenWidth')
        mobile_brand = dictionary.get('mobileBrand')
        mobile_model = dictionary.get('mobileModel')
        producer = dictionary.get('producer')
        browser_name = dictionary.get('browserName')
        mobile_screen_height = dictionary.get('mobileScreenHeight')
        is_mobile = dictionary.get('isMobile')
        mtype = dictionary.get('type')
        version = dictionary.get('version')
        operating_system = dictionary.get('operatingSystem')
        mobile_browser = dictionary.get('mobileBrowser')
        is_android = dictionary.get('isAndroid')
        is_ios = dictionary.get('isIos')
        operating_system_family = dictionary.get('operatingSystemFamily')
        operating_system_version = dictionary.get('operatingSystemVersion')
        engine = dictionary.get('engine')
        engine_version = dictionary.get('engineVersion')

        # Return an object of this model
        return cls(mobile_screen_width,
                   mobile_brand,
                   mobile_model,
                   producer,
                   browser_name,
                   mobile_screen_height,
                   is_mobile,
                   mtype,
                   version,
                   operating_system,
                   mobile_browser,
                   is_android,
                   is_ios,
                   operating_system_family,
                   operating_system_version,
                   engine,
                   engine_version)


