# -*- coding: utf-8 -*-

"""
   NeutrinoAPILib.Controllers.ImagingController

   This file was automatically generated for NeutrinoAPI.com by APIMATIC BETA v2.0 on 12/10/2015
"""
import unirest

from NeutrinoAPILib.APIHelper import APIHelper
from NeutrinoAPILib.Configuration import Configuration
from NeutrinoAPILib.APIException import APIException


class ImagingController(object):


    """A Controller to access Endpoints in the NeutrinoAPILib API."""

    def __init__(self,
                 user_id,
                 api_key):
        """
        Constructor with authentication and configuration parameters
        """
        self.__user_id = user_id
        self.__api_key = api_key

    def create_qr_code(self,
                       content,
                       bg_color=None,
                       fg_color=None,
                       height=None,
                       width=None):
        """Does a POST request to /qr-code.

        Generate a QR code as a PNG image. See:
        https://www.neutrinoapi.com/api/qr-code/

        Args:
            content (string): The content to encode into the QR code (e.g. a
                URL or a phone number)
            bg_color (string, optional): The QR code background color (you
                should always use a light color for this)
            fg_color (string, optional): The QR code foreground color (you
                should always use a dark color for this)
            height (int, optional): The height of the QR code (in px)
            width (int, optional): The width of the QR code (in px)

        Returns:
            binary: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/qr-code"

        # Process optional query parameters
        query_parameters = {
            "width":  width if width is not None else 250,
            "user-id": self.__user_id,
            "api-key": self.__api_key
        }
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, query_parameters)

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "APIMATIC 2.0"
        }

        # Prepare parameters
        parameters = {
            "content": content,
            "bg-color":  bg_color if bg_color is not None else "#ffffff",
            "fg-color":  fg_color if fg_color is not None else "#000000",
            "height":  height if height is not None else 250
        }
        # The body will be multipart data, so set the header
        headers['Content-Type'] = 'multipart/form-data'

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers, params=parameters)

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def create_html_to_pdf(self,
                           content,
                           html_width=None,
                           margin=None,
                           title=None):
        """Does a POST request to /html-to-pdf.

        Convert HTML content into PDF documents. See:
        https://www.neutrinoapi.com/api/html-to-pdf/

        Args:
            content (string): The HTML content. This can be either a URL to
                load HTML from or an actual HTML content string
            html_width (int, optional): The width (in px) to render the HTML
                document at
            margin (int, optional): The PDF document margin (in mm)
            title (string, optional): The PDF document title

        Returns:
            binary: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/html-to-pdf"

        # Process optional query parameters
        query_parameters = {
            "user-id": self.__user_id,
            "api-key": self.__api_key
        }
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, query_parameters)

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "APIMATIC 2.0"
        }

        # Prepare parameters
        parameters = {
            "content": content,
            "html-width":  html_width if html_width is not None else 1024,
            "margin":  margin if margin is not None else 10,
            "title": title
        }
        # The body will be multipart data, so set the header
        headers['Content-Type'] = 'multipart/form-data'

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers, params=parameters)

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def create_image_resize(self,
                            height,
                            image_url,
                            width,
                            format=None):
        """Does a POST request to /image-resize.

        Resize an image and output as either JPEG or PNG. See:
        https://www.neutrinoapi.com/api/image-resize/

        Args:
            height (int): Height to resize to (in px)
            image_url (string): The URL to the source image
            width (int): Width to resize to (in px)
            format (string, optional): The output image format, can be either
                png or jpg

        Returns:
            binary: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/image-resize"

        # Process optional query parameters
        query_parameters = {
            "user-id": self.__user_id,
            "api-key": self.__api_key
        }
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, query_parameters)

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "APIMATIC 2.0"
        }

        # Prepare parameters
        parameters = {
            "height": height,
            "image-url": image_url,
            "width": width,
            "format":  format if format is not None else "png"
        }
        # The body will be multipart data, so set the header
        headers['Content-Type'] = 'multipart/form-data'

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers, params=parameters)

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def create_image_watermark(self,
                               image_url,
                               watermark_url,
                               format=None,
                               height=None,
                               opacity=None,
                               position=None,
                               width=None):
        """Does a POST request to /image-watermark.

        Watermark one image with another image. See:
        https://www.neutrinoapi.com/api/image-watermark/

        Args:
            image_url (string): The URL to the source image
            watermark_url (string): The URL to the watermark image
            format (string, optional): The output image format, can be either
                png or jpg
            height (int, optional): If set resize the resulting image to this
                height (preserving aspect ratio)
            opacity (int, optional): The opacity of the watermark (0 to 100)
            position (string, optional): The position of the watermark image,
                possible values are: center, top-left, top-center, top-right,
                bottom-left, bottom-center, bottom-right
            width (int, optional): If set resize the resulting image to this
                width (preserving aspect ratio)

        Returns:
            binary: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/image-watermark"

        # Process optional query parameters
        query_parameters = {
            "user-id": self.__user_id,
            "api-key": self.__api_key
        }
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, query_parameters)

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "APIMATIC 2.0"
        }

        # Prepare parameters
        parameters = {
            "image-url": image_url,
            "watermark-url": watermark_url,
            "format":  format if format is not None else "png",
            "height": height,
            "opacity":  opacity if opacity is not None else 50,
            "position":  position if position is not None else "center",
            "width": width
        }
        # The body will be multipart data, so set the header
        headers['Content-Type'] = 'multipart/form-data'

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers, params=parameters)

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body
