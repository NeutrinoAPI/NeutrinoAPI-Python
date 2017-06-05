# -*- coding: utf-8 -*-

"""
    neutrino_api.models.url_info_response

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io )
"""


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
        load_time (float): The time taken to load the URL content (in
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
        content (string): The actual content this URL responded with. Only set
            if the 'fetch-content' option was used

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "http_status_message" : "httpStatusMessage",
        "server_region" : "serverRegion",
        "query" : "query",
        "server_name" : "serverName",
        "url_port" : "urlPort",
        "server_country" : "serverCountry",
        "real" : "real",
        "server_city" : "serverCity",
        "url_path" : "urlPath",
        "url" : "url",
        "valid" : "valid",
        "server_hostname" : "serverHostname",
        "load_time" : "loadTime",
        "http_ok" : "httpOk",
        "content_size" : "contentSize",
        "http_status" : "httpStatus",
        "server_country_code" : "serverCountryCode",
        "content_encoding" : "contentEncoding",
        "server_ip" : "serverIp",
        "url_protocol" : "urlProtocol",
        "content_type" : "contentType",
        "http_redirect" : "httpRedirect",
        "content" : "content"
    }

    def __init__(self,
                 http_status_message=None,
                 server_region=None,
                 query=None,
                 server_name=None,
                 url_port=None,
                 server_country=None,
                 real=None,
                 server_city=None,
                 url_path=None,
                 url=None,
                 valid=None,
                 server_hostname=None,
                 load_time=None,
                 http_ok=None,
                 content_size=None,
                 http_status=None,
                 server_country_code=None,
                 content_encoding=None,
                 server_ip=None,
                 url_protocol=None,
                 content_type=None,
                 http_redirect=None,
                 content=None):
        """Constructor for the URLInfoResponse class"""

        # Initialize members of the class
        self.http_status_message = http_status_message
        self.server_region = server_region
        self.query = query
        self.server_name = server_name
        self.url_port = url_port
        self.server_country = server_country
        self.real = real
        self.server_city = server_city
        self.url_path = url_path
        self.url = url
        self.valid = valid
        self.server_hostname = server_hostname
        self.load_time = load_time
        self.http_ok = http_ok
        self.content_size = content_size
        self.http_status = http_status
        self.server_country_code = server_country_code
        self.content_encoding = content_encoding
        self.server_ip = server_ip
        self.url_protocol = url_protocol
        self.content_type = content_type
        self.http_redirect = http_redirect
        self.content = content


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
        http_status_message = dictionary.get("httpStatusMessage")
        server_region = dictionary.get("serverRegion")
        query = dictionary.get("query")
        server_name = dictionary.get("serverName")
        url_port = dictionary.get("urlPort")
        server_country = dictionary.get("serverCountry")
        real = dictionary.get("real")
        server_city = dictionary.get("serverCity")
        url_path = dictionary.get("urlPath")
        url = dictionary.get("url")
        valid = dictionary.get("valid")
        server_hostname = dictionary.get("serverHostname")
        load_time = dictionary.get("loadTime")
        http_ok = dictionary.get("httpOk")
        content_size = dictionary.get("contentSize")
        http_status = dictionary.get("httpStatus")
        server_country_code = dictionary.get("serverCountryCode")
        content_encoding = dictionary.get("contentEncoding")
        server_ip = dictionary.get("serverIp")
        url_protocol = dictionary.get("urlProtocol")
        content_type = dictionary.get("contentType")
        http_redirect = dictionary.get("httpRedirect")
        content = dictionary.get("content")

        # Return an object of this model
        return cls(http_status_message,
                   server_region,
                   query,
                   server_name,
                   url_port,
                   server_country,
                   real,
                   server_city,
                   url_path,
                   url,
                   valid,
                   server_hostname,
                   load_time,
                   http_ok,
                   content_size,
                   http_status,
                   server_country_code,
                   content_encoding,
                   server_ip,
                   url_protocol,
                   content_type,
                   http_redirect,
                   content)


