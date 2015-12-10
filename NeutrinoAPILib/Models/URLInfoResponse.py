# -*- coding: utf-8 -*-

"""
   NeutrinoAPILib.Models.URLInfoResponse
 
   This file was automatically generated for NeutrinoAPI.com by APIMATIC BETA v2.0 on 12/10/2015
"""
from NeutrinoAPILib.APIHelper import APIHelper

class URLInfoResponse(object):

    """Implementation of the 'URL Info Response' model.

    TODO: type model description here.

    Attributes:
        http_status_message (string): The HTTP status message assoicated with
            the status code
        server_region (string): Server IP geo-location: full region name (if
            detectable)
        query (dict<object, object>): A key:value map of the URL query
            paramaters
        server_name (string): The name of the server software hosting this
            URL
        url_port (int): The URL port
        server_country (string): Server IP geo-location: full country name
        real (bool): Is this URL actually serving real content
        server_city (string): Server IP geo-location: full city name (if
            detectable)
        url_path (string): The URL path
        url (string): The fully qualified URL. This may be different to the
            URL requested if http-redirect is True
        valid (bool): Is this a valid well-formed URL
        server_hostname (string): The server hostname (PTR)
        load_time (double): The time taken to load the URL content (in
            seconds)
        http_ok (bool): True if this URL responded with an HTTP OK (200)
            status
        content_size (int): The size of the URL content in bytes
        http_status (int): The HTTP status code this URL responded with
        server_country_code (string): Server IP geo-location: ISO 2-letter
            country code
        content_encoding (string): The encoding type the URL uses
        server_ip (string): The IP address of the server hosting this URL
        url_protocol (string): The URL protocol (usually http or https)
        content_type (string): The content-type the URL points to
        http_redirect (bool): True if this URL responded with a HTTP redirect

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the URLInfoResponse class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    httpStatusMessage -- string -- Sets the attribute http_status_message
                    serverRegion -- string -- Sets the attribute server_region
                    query -- dict<object, object> -- Sets the attribute query
                    serverName -- string -- Sets the attribute server_name
                    urlPort -- int -- Sets the attribute url_port
                    serverCountry -- string -- Sets the attribute server_country
                    real -- bool -- Sets the attribute real
                    serverCity -- string -- Sets the attribute server_city
                    urlPath -- string -- Sets the attribute url_path
                    url -- string -- Sets the attribute url
                    valid -- bool -- Sets the attribute valid
                    serverHostname -- string -- Sets the attribute server_hostname
                    loadTime -- double -- Sets the attribute load_time
                    httpOk -- bool -- Sets the attribute http_ok
                    contentSize -- int -- Sets the attribute content_size
                    httpStatus -- int -- Sets the attribute http_status
                    serverCountryCode -- string -- Sets the attribute server_country_code
                    contentEncoding -- string -- Sets the attribute content_encoding
                    serverIp -- string -- Sets the attribute server_ip
                    urlProtocol -- string -- Sets the attribute url_protocol
                    contentType -- string -- Sets the attribute content_type
                    httpRedirect -- bool -- Sets the attribute http_redirect
        
        """
        # Set all of the parameters to their default values
        self.http_status_message = None
        self.server_region = None
        self.query = None
        self.server_name = None
        self.url_port = None
        self.server_country = None
        self.real = None
        self.server_city = None
        self.url_path = None
        self.url = None
        self.valid = None
        self.server_hostname = None
        self.load_time = None
        self.http_ok = None
        self.content_size = None
        self.http_status = None
        self.server_country_code = None
        self.content_encoding = None
        self.server_ip = None
        self.url_protocol = None
        self.content_type = None
        self.http_redirect = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "httpStatusMessage": "http_status_message",
            "serverRegion": "server_region",
            "query": "query",
            "serverName": "server_name",
            "urlPort": "url_port",
            "serverCountry": "server_country",
            "real": "real",
            "serverCity": "server_city",
            "urlPath": "url_path",
            "url": "url",
            "valid": "valid",
            "serverHostname": "server_hostname",
            "loadTime": "load_time",
            "httpOk": "http_ok",
            "contentSize": "content_size",
            "httpStatus": "http_status",
            "serverCountryCode": "server_country_code",
            "contentEncoding": "content_encoding",
            "serverIp": "server_ip",
            "urlProtocol": "url_protocol",
            "contentType": "content_type",
            "httpRedirect": "http_redirect",
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
            "http_status_message": "httpStatusMessage",
            "server_region": "serverRegion",
            "query": "query",
            "server_name": "serverName",
            "url_port": "urlPort",
            "server_country": "serverCountry",
            "real": "real",
            "server_city": "serverCity",
            "url_path": "urlPath",
            "url": "url",
            "valid": "valid",
            "server_hostname": "serverHostname",
            "load_time": "loadTime",
            "http_ok": "httpOk",
            "content_size": "contentSize",
            "http_status": "httpStatus",
            "server_country_code": "serverCountryCode",
            "content_encoding": "contentEncoding",
            "server_ip": "serverIp",
            "url_protocol": "urlProtocol",
            "content_type": "contentType",
            "http_redirect": "httpRedirect",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)