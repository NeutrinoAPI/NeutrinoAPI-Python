# -*- coding: utf-8 -*-

"""
    neutrino_api.controllers.imaging

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.custom_query_auth import CustomQueryAuth

class Imaging(BaseController):

    """A Controller to access Endpoints in the neutrino_api API."""


    def image_resize(self,
                     image_url,
                     width,
                     height,
                     format='png'):
        """Does a POST request to /image-resize.

        Resize an image and output as either JPEG or PNG. See:
        https://www.neutrinoapi.com/api/image-resize/

        Args:
            image_url (string): The URL to the source image
            width (int): Width to resize to (in px)
            height (int): Height to resize to (in px)
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

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/image-resize'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'image-url': image_url,
            'width': width,
            'height': height,
            'format': format
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request, binary = True)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def qr_code(self,
                content,
                width=250,
                height=250,
                fg_color='#000000',
                bg_color='#ffffff'):
        """Does a POST request to /qr-code.

        Generate a QR code as a PNG image. See:
        https://www.neutrinoapi.com/api/qr-code/

        Args:
            content (string): The content to encode into the QR code (e.g. a
                URL or a phone number)
            width (int, optional): The width of the QR code (in px)
            height (int, optional): The height of the QR code (in px)
            fg_color (string, optional): The QR code foreground color (you
                should always use a dark color for this)
            bg_color (string, optional): The QR code background color (you
                should always use a light color for this)

        Returns:
            binary: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/qr-code'
        _query_parameters = {
            'width': width
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'content': content,
            'height': height,
            'fg-color': fg_color,
            'bg-color': bg_color
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request, binary = True)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def image_watermark(self,
                        image_url,
                        watermark_url,
                        opacity=50,
                        format='png',
                        position='center',
                        width=None,
                        height=None):
        """Does a POST request to /image-watermark.

        Watermark one image with another image. See:
        https://www.neutrinoapi.com/api/image-watermark/

        Args:
            image_url (string): The URL to the source image
            watermark_url (string): The URL to the watermark image
            opacity (int, optional): The opacity of the watermark (0 to 100)
            format (string, optional): The output image format, can be either
                png or jpg
            position (string, optional): The position of the watermark image,
                possible values are: center, top-left, top-center, top-right,
                bottom-left, bottom-center, bottom-right
            width (int, optional): If set resize the resulting image to this
                width (preserving aspect ratio)
            height (int, optional): If set resize the resulting image to this
                height (preserving aspect ratio)

        Returns:
            binary: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/image-watermark'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'image-url': image_url,
            'watermark-url': watermark_url,
            'opacity': opacity,
            'format': format,
            'position': position,
            'width': width,
            'height': height
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request, binary = True)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def html_5_render(self,
                      content,
                      format='PDF',
                      page_size='A4',
                      title=None,
                      margin=0,
                      margin_left=0,
                      margin_right=0,
                      margin_top=0,
                      margin_bottom=0,
                      landscape=False,
                      zoom=1.0,
                      grayscale=False,
                      media_print=False,
                      media_queries=False,
                      forms=False,
                      css=None,
                      image_width=1024,
                      image_height=None,
                      render_delay=None,
                      header_text_left=None,
                      header_text_center=None,
                      header_text_right=None,
                      header_size=9,
                      header_font='Courier',
                      header_font_size='11',
                      header_line=False,
                      footer_text_left=None,
                      footer_text_center=None,
                      footer_text_right=None,
                      footer_size=9,
                      footer_font='Courier',
                      footer_font_size=11,
                      footer_line=False,
                      page_width=None,
                      page_height=None):
        """Does a POST request to /html5-render.

        Render HTML and HTML5 content to PDF, JPG or PNG

        Args:
            content (string): The HTML content. This can be either a URL to
                load HTML from or an actual HTML content string
            format (string, optional): Which format to output, available
                options are: PDF, PNG, JPG
            page_size (string, optional): Set the document page size, can be
                one of: A0 - A9, B0 - B10, Comm10E, DLE or Letter
            title (string, optional): The document title
            margin (int, optional): The document margin (in mm)
            margin_left (int, optional): The document left margin (in mm)
            margin_right (int, optional): The document right margin (in mm)
            margin_top (int, optional): The document top margin (in mm)
            margin_bottom (int, optional): The document bottom margin (in mm)
            landscape (bool, optional): Set the document to lanscape
                orientation
            zoom (float, optional): Set the zoom factor when rendering the
                page (2.0 for double size, 0.5 for half size)
            grayscale (bool, optional): Render the final document in
                grayscale
            media_print (bool, optional): Use @media print CSS styles to
                render the document
            media_queries (bool, optional): Activate all @media queries before
                rendering. This can be useful if you wan't to render the
                mobile version of a responsive website
            forms (bool, optional): Generate real (fillable) PDF forms from
                HTML forms
            css (string, optional): Inject custom CSS into the HTML. e.g.
                'body { background-color: red;}'
            image_width (int, optional): If rendering to an image format (PNG
                or JPG) use this image width (in pixels)
            image_height (int, optional): If rendering to an image format (PNG
                or JPG) use this image height (in pixels). The default is
                automatic which dynamically sets the image height based on the
                content
            render_delay (int, optional): Number of milliseconds to wait
                before rendering the page (can be useful for pages with
                animations etc)
            header_text_left (string, optional): Text to print to the
                left-hand side header of each page. e.g. 'My header - Page
                {page_number} of {total_pages}'
            header_text_center (string, optional): Text to print to the center
                header of each page
            header_text_right (string, optional): Text to print to the
                right-hand side header of each page
            header_size (int, optional): The height of your header (in mm)
            header_font (string, optional): Set the header font. Fonts
                available: Times, Courier, Helvetica, Arial
            header_font_size (string, optional): Set the header font size (in
                pt)
            header_line (bool, optional): Draw a full page width horizontal
                line under your header
            footer_text_left (string, optional): Text to print to the
                left-hand side footer of each page. e.g. 'My footer - Page
                {page_number} of {total_pages}'
            footer_text_center (string, optional): Text to print to the center
                header of each page
            footer_text_right (string, optional): Text to print to the
                right-hand side header of each page
            footer_size (int, optional): The height of your footer (in mm)
            footer_font (string, optional): Set the footer font. Fonts
                available: Times, Courier, Helvetica, Arial
            footer_font_size (int, optional): Set the footer font size (in
                pt)
            footer_line (bool, optional): Draw a full page width horizontal
                line above your footer
            page_width (int, optional): Set the PDF page width explicitly (in
                mm)
            page_height (int, optional): Set the PDF page height explicitly
                (in mm)

        Returns:
            binary: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/html5-render'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'output-case': 'camel',
            'content': content,
            'format': format,
            'page-size': page_size,
            'title': title,
            'margin': margin,
            'margin-left': margin_left,
            'margin-right': margin_right,
            'margin-top': margin_top,
            'margin-bottom': margin_bottom,
            'landscape': landscape,
            'zoom': zoom,
            'grayscale': grayscale,
            'media-print': media_print,
            'media-queries': media_queries,
            'forms': forms,
            'css': css,
            'image-width': image_width,
            'image-height': image_height,
            'render-delay': render_delay,
            'header-text-left': header_text_left,
            'header-text-center': header_text_center,
            'header-text-right': header_text_right,
            'header-size': header_size,
            'header-font': header_font,
            'header-font-size': header_font_size,
            'header-line': header_line,
            'footer-text-left': footer_text_left,
            'footer-text-center': footer_text_center,
            'footer-text-right': footer_text_right,
            'footer-size': footer_size,
            'footer-font': footer_font,
            'footer-font-size': footer_font_size,
            'footer-line': footer_line,
            'page-width': page_width,
            'page-height': page_height
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request, binary = True)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body
