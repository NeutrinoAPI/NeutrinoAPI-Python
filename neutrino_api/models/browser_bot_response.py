# -*- coding: utf-8 -*-

"""
    neutrino_api

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""


class BrowserBotResponse(object):

    """Implementation of the 'Browser Bot Response' model.

    TODO: type model description here.

    Attributes:
        url (string): The page URL
        content (string): The complete raw, decompressed and decoded page
            content. Usually will be either HTML, JSON or XML
        mime_type (string): The document MIME type
        title (string): The document title
        is_error (bool): True if an error has occurred loading the page. Check
            the 'error-message' field for details
        is_timeout (bool): True if a timeout occurred while loading the page.
            You can set the timeout with the request parameter 'timeout'
        error_message (string): Contains the error message if an error has
            occurred ('is-error' will be true)
        http_status_code (int): The HTTP status code the URL returned
        http_status_message (string): The HTTP status message the URL
            returned
        is_http_ok (bool): True if the HTTP status is OK (200)
        is_http_redirect (bool): True if the URL responded with an HTTP
            redirect
        http_redirect_url (string): The redirected URL if the URL responded
            with an HTTP redirect
        server_ip (string): The HTTP servers IP address
        load_time (float): The number of seconds taken to load the page (from
            initial request until DOM ready)
        response_headers (dict<object, string>): Map containing all the HTTP
            response headers the URL responded with
        is_secure (bool): True if the page is secured using TLS/SSL
        security_details (dict<object, string>): Map containing details of the
            TLS/SSL setup
        elements (list of string): Array containing all the elements matching
            the supplied selector.<br/>Each element object will contain the
            text content, HTML content and all current element attributes
        exec_results (list of string): If you executed any JavaScript this
            array holds the results as objects

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "url":'url',
        "content":'content',
        "mime_type":'mimeType',
        "title":'title',
        "is_error":'isError',
        "is_timeout":'isTimeout',
        "error_message":'errorMessage',
        "http_status_code":'httpStatusCode',
        "http_status_message":'httpStatusMessage',
        "is_http_ok":'isHttpOk',
        "is_http_redirect":'isHttpRedirect',
        "http_redirect_url":'httpRedirectUrl',
        "server_ip":'serverIp',
        "load_time":'loadTime',
        "response_headers":'responseHeaders',
        "is_secure":'isSecure',
        "security_details":'securityDetails',
        "elements":'elements',
        "exec_results":'execResults'
    }

    def __init__(self,
                 url=None,
                 content=None,
                 mime_type=None,
                 title=None,
                 is_error=None,
                 is_timeout=None,
                 error_message=None,
                 http_status_code=None,
                 http_status_message=None,
                 is_http_ok=None,
                 is_http_redirect=None,
                 http_redirect_url=None,
                 server_ip=None,
                 load_time=None,
                 response_headers=None,
                 is_secure=None,
                 security_details=None,
                 elements=None,
                 exec_results=None):
        """Constructor for the BrowserBotResponse class"""

        # Initialize members of the class
        self.url = url
        self.content = content
        self.mime_type = mime_type
        self.title = title
        self.is_error = is_error
        self.is_timeout = is_timeout
        self.error_message = error_message
        self.http_status_code = http_status_code
        self.http_status_message = http_status_message
        self.is_http_ok = is_http_ok
        self.is_http_redirect = is_http_redirect
        self.http_redirect_url = http_redirect_url
        self.server_ip = server_ip
        self.load_time = load_time
        self.response_headers = response_headers
        self.is_secure = is_secure
        self.security_details = security_details
        self.elements = elements
        self.exec_results = exec_results


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
        url = dictionary.get('url')
        content = dictionary.get('content')
        mime_type = dictionary.get('mimeType')
        title = dictionary.get('title')
        is_error = dictionary.get('isError')
        is_timeout = dictionary.get('isTimeout')
        error_message = dictionary.get('errorMessage')
        http_status_code = dictionary.get('httpStatusCode')
        http_status_message = dictionary.get('httpStatusMessage')
        is_http_ok = dictionary.get('isHttpOk')
        is_http_redirect = dictionary.get('isHttpRedirect')
        http_redirect_url = dictionary.get('httpRedirectUrl')
        server_ip = dictionary.get('serverIp')
        load_time = dictionary.get('loadTime')
        response_headers = dictionary.get('responseHeaders')
        is_secure = dictionary.get('isSecure')
        security_details = dictionary.get('securityDetails')
        elements = dictionary.get('elements')
        exec_results = dictionary.get('execResults')

        # Return an object of this model
        return cls(url,
                   content,
                   mime_type,
                   title,
                   is_error,
                   is_timeout,
                   error_message,
                   http_status_code,
                   http_status_message,
                   is_http_ok,
                   is_http_redirect,
                   http_redirect_url,
                   server_ip,
                   load_time,
                   response_headers,
                   is_secure,
                   security_details,
                   elements,
                   exec_results)


