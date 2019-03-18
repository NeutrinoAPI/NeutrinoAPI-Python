# Getting started

The general-purpose API

## How to Build


You must have Python ```2 >=2.7.9``` or Python ```3 >=3.4``` installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type ```pip --version```.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=NeutrinoAPI-Python)


## How to Use

The following section explains how to use the NeutrinoAPI SDK package in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your generated SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=openProject0&workspaceFolder=NeutrinoAPI-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=openProject1&workspaceFolder=NeutrinoAPI-Python&projectName=neutrino_api)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=NeutrinoAPI-Python&projectName=neutrino_api)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=createFile&workspaceFolder=NeutrinoAPI-Python&projectName=neutrino_api)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```Python
from neutrino_api.neutrino_api_client import NeutrinoApiClient
```

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=NeutrinoAPI-Python&libraryName=neutrino_api.neutrino_api_client&projectName=neutrino_api&className=NeutrinoApiClient)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=NeutrinoAPI-Python&libraryName=neutrino_api.neutrino_api_client&projectName=neutrino_api&className=NeutrinoApiClient)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke ```pip install -r test-requirements.txt```
  3. Invoke ```nosetests```

## Initialization

### Authentication
In order to setup authentication and initialization of the API client, you need the following information.

| Parameter | Description |
|-----------|-------------|
| user_id | Your user ID |
| api_key | Your API key |



API client can be initialized as following.

```python
# Configuration parameters and credentials
user_id = 'user_id' # Your user ID
api_key = 'api_key' # Your API key

client = NeutrinoApiClient(user_id, api_key)
```



# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [WWW](#www)
* [Imaging](#imaging)
* [Telephony](#telephony)
* [ECommerce](#e_commerce)
* [Geolocation](#geolocation)
* [SecurityAndNetworking](#security_and_networking)
* [DataTools](#data_tools)

## <a name="www"></a>![Class: ](https://apidocs.io/img/class.png ".WWW") WWW

### Get controller instance

An instance of the ``` WWW ``` class can be accessed from the API Client.

```python
 www_controller = client.www
```

### <a name="browser_bot"></a>![Method: ](https://apidocs.io/img/method.png ".WWW.browser_bot") browser_bot

> Browser bot can extract content, interact with keyboard and mouse events, and execute JavaScript on a website. See: https://www.neutrinoapi.com/api/browser-bot/

```python
def browser_bot(self,
                    url,
                    timeout=30,
                    delay=2,
                    selector=None,
                    mexec=,
                    user_agent=None,
                    ignore_certificate_errors=False)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| url |  ``` Required ```  | The URL to load |
| timeout |  ``` Optional ```  ``` DefaultValue ```  | Timeout in seconds. Give up if still trying to load the page after this number of seconds |
| delay |  ``` Optional ```  ``` DefaultValue ```  | Delay in seconds to wait before executing any selectors or JavaScript |
| selector |  ``` Optional ```  | Extract content from the page DOM using this selector. Commonly known as a CSS selector, you can find a good reference <a href="https://www.w3schools.com/cssref/css_selectors.asp" target="_blank">here</a> |
| mexec |  ``` Optional ```  ``` Collection ```  ``` DefaultValue ```  | Execute JavaScript on the page. Each array element should contain a valid JavaScript statement in string form. If a statement returns any kind of value it will be returned in the 'exec-results' response.<br/><br/>For your convenience you can also use the following special shortcut functions:<br/><div style='padding-left:32px; font-family:inherit; font-size:inherit;'>sleep(seconds); Just wait/sleep for the specified number of seconds.<br/>click('selector'); Click on the first element matching the given selector.<br/>focus('selector'); Focus on the first element matching the given selector.<br/>keys('characters'); Send the specified keyboard characters. Use click() or focus() first to send keys to a specific element.<br/>enter(); Send the Enter key.<br/>tab(); Send the Tab key.<br/></div><br/>Example:<br/><div style='padding-left:32px; font-family:inherit; font-size:inherit;'>[ "click('#button-id')", "sleep(1)", "click('.field-class')", "keys('1234')", "enter()" ]</div> |
| userAgent |  ``` Optional ```  | Override the browsers default user-agent string with this one |
| ignoreCertificateErrors |  ``` Optional ```  ``` DefaultValue ```  | Ignore any TLS/SSL certificate errors and load the page anyway |



#### Example Usage

```python
url = 'url'
timeout = 30
delay = 2
selector = 'selector'
mexec_value = '[]'
mexec = json.loads(mexec_value)
user_agent = 'user-agent'
ignore_certificate_errors = False

result = www_controller.browser_bot(url, timeout, delay, selector, mexec, user_agent, ignore_certificate_errors)

```


### <a name="html_clean"></a>![Method: ](https://apidocs.io/img/method.png ".WWW.html_clean") html_clean

> Clean and sanitize untrusted HTML. See: https://www.neutrinoapi.com/api/html-clean/

```python
def html_clean(self,
                   content,
                   output_type)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| content |  ``` Required ```  | The HTML content. This can be either a URL to load HTML from or an actual HTML content string |
| outputType |  ``` Required ```  | The level of sanitization, possible values are:<br/><b>plain-text</b>: reduce the content to plain text only (no HTML tags at all)<br/><br/><b>simple-text</b>: allow only very basic text formatting tags like b, em, i, strong, u<br/><br/><b>basic-html</b>: allow advanced text formatting and hyper links<br/><br/><b>basic-html-with-images</b>: same as basic html but also allows image tags<br/><br/><b>advanced-html</b>: same as basic html with images but also allows many more common HTML tags like table, ul, dl, pre<br/> |



#### Example Usage

```python
content = 'content'
output_type = 'output-type'

result = www_controller.html_clean(content, output_type)

```


### <a name="url_info"></a>![Method: ](https://apidocs.io/img/method.png ".WWW.url_info") url_info

> Parse, analyze and retrieve content from the supplied URL. See: https://www.neutrinoapi.com/api/url-info/

```python
def url_info(self,
                 url,
                 fetch_content=False)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| url |  ``` Required ```  | The URL to probe |
| fetchContent |  ``` Optional ```  ``` DefaultValue ```  | If this URL responds with html, text, json or xml then return the response. This option is useful if you want to perform further processing on the URL content (e.g. with the HTML Extract or HTML Clean APIs) |



#### Example Usage

```python
url = 'url'
fetch_content = False

result = www_controller.url_info(url, fetch_content)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="imaging"></a>![Class: ](https://apidocs.io/img/class.png ".Imaging") Imaging

### Get controller instance

An instance of the ``` Imaging ``` class can be accessed from the API Client.

```python
 imaging_controller = client.imaging
```

### <a name="image_watermark"></a>![Method: ](https://apidocs.io/img/method.png ".Imaging.image_watermark") image_watermark

> Watermark one image with another image. See: https://www.neutrinoapi.com/api/image-watermark/

```python
def image_watermark(self,
                        image_url,
                        watermark_url,
                        opacity=50,
                        format='png',
                        position='center',
                        width=None,
                        height=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| imageUrl |  ``` Required ```  | The URL to the source image |
| watermarkUrl |  ``` Required ```  | The URL to the watermark image |
| opacity |  ``` Optional ```  ``` DefaultValue ```  | The opacity of the watermark (0 to 100) |
| format |  ``` Optional ```  ``` DefaultValue ```  | The output image format, can be either png or jpg |
| position |  ``` Optional ```  ``` DefaultValue ```  | The position of the watermark image, possible values are:<br/>center, top-left, top-center, top-right, bottom-left, bottom-center, bottom-right |
| width |  ``` Optional ```  | If set resize the resulting image to this width (in px) while preserving aspect ratio |
| height |  ``` Optional ```  | If set resize the resulting image to this height (in px) while preserving aspect ratio |



#### Example Usage

```python
image_url = 'image-url'
watermark_url = 'watermark-url'
opacity = 50
format = 'png'
position = 'center'
width = 214
height = 214

result = imaging_controller.image_watermark(image_url, watermark_url, opacity, format, position, width, height)

```


### <a name="qr_code"></a>![Method: ](https://apidocs.io/img/method.png ".Imaging.qr_code") qr_code

> Generate a QR code as a PNG image. See: https://www.neutrinoapi.com/api/qr-code/

```python
def qr_code(self,
                content,
                width=256,
                height=256,
                fg_color='#000000',
                bg_color='#ffffff')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| content |  ``` Required ```  | The content to encode into the QR code (e.g. a URL or a phone number) |
| width |  ``` Optional ```  ``` DefaultValue ```  | The width of the QR code (in px) |
| height |  ``` Optional ```  ``` DefaultValue ```  | The height of the QR code (in px) |
| fgColor |  ``` Optional ```  ``` DefaultValue ```  | The QR code foreground color |
| bgColor |  ``` Optional ```  ``` DefaultValue ```  | The QR code background color |



#### Example Usage

```python
content = 'content'
width = 256
height = 256
fg_color = '#000000'
bg_color = '#ffffff'

result = imaging_controller.qr_code(content, width, height, fg_color, bg_color)

```


### <a name="image_resize"></a>![Method: ](https://apidocs.io/img/method.png ".Imaging.image_resize") image_resize

> Resize an image and output as either JPEG or PNG. See: https://www.neutrinoapi.com/api/image-resize/

```python
def image_resize(self,
                     image_url,
                     width,
                     height,
                     format='png')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| imageUrl |  ``` Required ```  | The URL to the source image |
| width |  ``` Required ```  | The width to resize to (in px) while preserving aspect ratio |
| height |  ``` Required ```  | The height to resize to (in px) while preserving aspect ratio |
| format |  ``` Optional ```  ``` DefaultValue ```  | The output image format, can be either png or jpg |



#### Example Usage

```python
image_url = 'image-url'
width = 214
height = 214
format = 'png'

result = imaging_controller.image_resize(image_url, width, height, format)

```


### <a name="html_5_render"></a>![Method: ](https://apidocs.io/img/method.png ".Imaging.html_5_render") html_5_render

> Render HTML content to PDF, JPG or PNG. See: https://www.neutrinoapi.com/api/html5-render/

```python
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
                      zoom=1,
                      grayscale=False,
                      media_print=False,
                      media_queries=False,
                      forms=False,
                      css=None,
                      image_width=1024,
                      image_height=None,
                      render_delay=0,
                      header_text_left=None,
                      header_text_center=None,
                      header_text_right=None,
                      header_size=9,
                      header_font='Courier',
                      header_font_size=11,
                      header_line=False,
                      footer_text_left=None,
                      footer_text_center=None,
                      footer_text_right=None,
                      footer_size=9,
                      footer_font='Courier',
                      footer_font_size=11,
                      footer_line=False,
                      page_width=None,
                      page_height=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| content |  ``` Required ```  | The HTML content. This can be either a URL to load HTML from or an actual HTML content string |
| format |  ``` Optional ```  ``` DefaultValue ```  | Which format to output, available options are: PDF, PNG, JPG |
| pageSize |  ``` Optional ```  ``` DefaultValue ```  | Set the document page size, can be one of: A0 - A9, B0 - B10, Comm10E, DLE or Letter |
| title |  ``` Optional ```  | The document title |
| margin |  ``` Optional ```  ``` DefaultValue ```  | The document margin (in mm) |
| marginLeft |  ``` Optional ```  ``` DefaultValue ```  | The document left margin (in mm) |
| marginRight |  ``` Optional ```  ``` DefaultValue ```  | The document right margin (in mm) |
| marginTop |  ``` Optional ```  ``` DefaultValue ```  | The document top margin (in mm) |
| marginBottom |  ``` Optional ```  ``` DefaultValue ```  | The document bottom margin (in mm) |
| landscape |  ``` Optional ```  ``` DefaultValue ```  | Set the document to lanscape orientation |
| zoom |  ``` Optional ```  ``` DefaultValue ```  | Set the zoom factor when rendering the page (2.0 for double size, 0.5 for half size) |
| grayscale |  ``` Optional ```  ``` DefaultValue ```  | Render the final document in grayscale |
| mediaPrint |  ``` Optional ```  ``` DefaultValue ```  | Use @media print CSS styles to render the document |
| mediaQueries |  ``` Optional ```  ``` DefaultValue ```  | Activate all @media queries before rendering. This can be useful if you wan't to render the mobile version of a responsive website |
| forms |  ``` Optional ```  ``` DefaultValue ```  | Generate real (fillable) PDF forms from HTML forms |
| css |  ``` Optional ```  | Inject custom CSS into the HTML. e.g. 'body { background-color: red;}' |
| imageWidth |  ``` Optional ```  ``` DefaultValue ```  | If rendering to an image format (PNG or JPG) use this image width (in pixels) |
| imageHeight |  ``` Optional ```  | If rendering to an image format (PNG or JPG) use this image height (in pixels). The default is automatic which dynamically sets the image height based on the content |
| renderDelay |  ``` Optional ```  ``` DefaultValue ```  | Number of milliseconds to wait before rendering the page (can be useful for pages with animations etc) |
| headerTextLeft |  ``` Optional ```  | Text to print to the left-hand side header of each page. e.g. 'My header - Page {page_number} of {total_pages}' |
| headerTextCenter |  ``` Optional ```  | Text to print to the center header of each page |
| headerTextRight |  ``` Optional ```  | Text to print to the right-hand side header of each page |
| headerSize |  ``` Optional ```  ``` DefaultValue ```  | The height of your header (in mm) |
| headerFont |  ``` Optional ```  ``` DefaultValue ```  | Set the header font. Fonts available: Times, Courier, Helvetica, Arial |
| headerFontSize |  ``` Optional ```  ``` DefaultValue ```  | Set the header font size (in pt) |
| headerLine |  ``` Optional ```  ``` DefaultValue ```  | Draw a full page width horizontal line under your header |
| footerTextLeft |  ``` Optional ```  | Text to print to the left-hand side footer of each page. e.g. 'My footer - Page {page_number} of {total_pages}' |
| footerTextCenter |  ``` Optional ```  | Text to print to the center header of each page |
| footerTextRight |  ``` Optional ```  | Text to print to the right-hand side header of each page |
| footerSize |  ``` Optional ```  ``` DefaultValue ```  | The height of your footer (in mm) |
| footerFont |  ``` Optional ```  ``` DefaultValue ```  | Set the footer font. Fonts available: Times, Courier, Helvetica, Arial |
| footerFontSize |  ``` Optional ```  ``` DefaultValue ```  | Set the footer font size (in pt) |
| footerLine |  ``` Optional ```  ``` DefaultValue ```  | Draw a full page width horizontal line above your footer |
| pageWidth |  ``` Optional ```  | Set the PDF page width explicitly (in mm) |
| pageHeight |  ``` Optional ```  | Set the PDF page height explicitly (in mm) |



#### Example Usage

```python
content = 'content'
format = 'PDF'
page_size = 'A4'
title = 'title'
margin = 0
margin_left = 0
margin_right = 0
margin_top = 0
margin_bottom = 0
landscape = False
zoom = 1
grayscale = False
media_print = False
media_queries = False
forms = False
css = 'css'
image_width = 1024
image_height = 50
render_delay = 0
header_text_left = 'header-text-left'
header_text_center = 'header-text-center'
header_text_right = 'header-text-right'
header_size = 9
header_font = 'Courier'
header_font_size = 11
header_line = False
footer_text_left = 'footer-text-left'
footer_text_center = 'footer-text-center'
footer_text_right = 'footer-text-right'
footer_size = 9
footer_font = 'Courier'
footer_font_size = 11
footer_line = False
page_width = 50
page_height = 50

result = imaging_controller.html_5_render(content, format, page_size, title, margin, margin_left, margin_right, margin_top, margin_bottom, landscape, zoom, grayscale, media_print, media_queries, forms, css, image_width, image_height, render_delay, header_text_left, header_text_center, header_text_right, header_size, header_font, header_font_size, header_line, footer_text_left, footer_text_center, footer_text_right, footer_size, footer_font, footer_font_size, footer_line, page_width, page_height)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="telephony"></a>![Class: ](https://apidocs.io/img/class.png ".Telephony") Telephony

### Get controller instance

An instance of the ``` Telephony ``` class can be accessed from the API Client.

```python
 telephony_controller = client.telephony
```

### <a name="phone_verify"></a>![Method: ](https://apidocs.io/img/method.png ".Telephony.phone_verify") phone_verify

> Make an automated call to any valid phone number and playback a unique security code. See: https://www.neutrinoapi.com/api/phone-verify/

```python
def phone_verify(self,
                     number,
                     code_length=6,
                     security_code=None,
                     playback_delay=800,
                     country_code=None,
                     language_code='en')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| number |  ``` Required ```  | The phone number to send the verification code to |
| codeLength |  ``` Optional ```  ``` DefaultValue ```  | The number of digits to use in the security code (between 4 and 12) |
| securityCode |  ``` Optional ```  | Pass in your own security code. This is useful if you have implemented TOTP or similar 2FA methods. If not set then we will generate a secure random code |
| playbackDelay |  ``` Optional ```  ``` DefaultValue ```  | The delay in milliseconds between the playback of each security code |
| countryCode |  ``` Optional ```  | ISO 2-letter country code, assume numbers are based in this country.<br/>If not set numbers are assumed to be in international format (with or without the leading + sign) |
| languageCode |  ``` Optional ```  ``` DefaultValue ```  | The language to playback the verification code in, available languages are:<ul><li>de - German</li><li>en - English</li><li>es - Spanish</li><li>fr - French</li><li>it - Italian</li><li>pt - Portuguese</li><li>ru - Russian</li></ul> |



#### Example Usage

```python
number = 'number'
code_length = 6
security_code = 50
playback_delay = 800
country_code = 'country-code'
language_code = 'en'

result = telephony_controller.phone_verify(number, code_length, security_code, playback_delay, country_code, language_code)

```


### <a name="sms_message"></a>![Method: ](https://apidocs.io/img/method.png ".Telephony.sms_message") sms_message

> Send a free-form message to any mobile device via SMS. See: https://www.neutrinoapi.com/api/sms-message/

```python
def sms_message(self,
                    number,
                    message,
                    country_code=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| number |  ``` Required ```  | The phone number to send a message to |
| message |  ``` Required ```  | The SMS message to send. Messages are truncated to a maximum of 150 characters for ASCII content OR 70 characters for UTF content |
| countryCode |  ``` Optional ```  | ISO 2-letter country code, assume numbers are based in this country.<br/>If not set numbers are assumed to be in international format (with or without the leading + sign) |



#### Example Usage

```python
number = 'number'
message = 'message'
country_code = 'country-code'

result = telephony_controller.sms_message(number, message, country_code)

```


### <a name="sms_verify"></a>![Method: ](https://apidocs.io/img/method.png ".Telephony.sms_verify") sms_verify

> Send a unique security code to any mobile device via SMS. See: https://www.neutrinoapi.com/api/sms-verify/

```python
def sms_verify(self,
                   number,
                   code_length=5,
                   security_code=None,
                   country_code=None,
                   language_code='en')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| number |  ``` Required ```  | The phone number to send a verification code to |
| codeLength |  ``` Optional ```  ``` DefaultValue ```  | The number of digits to use in the security code (must be between 4 and 12) |
| securityCode |  ``` Optional ```  | Pass in your own security code. This is useful if you have implemented TOTP or similar 2FA methods. If not set then we will generate a secure random code |
| countryCode |  ``` Optional ```  | ISO 2-letter country code, assume numbers are based in this country.<br/>If not set numbers are assumed to be in international format (with or without the leading + sign) |
| languageCode |  ``` Optional ```  ``` DefaultValue ```  | The language to send the verification code in, available languages are:<ul><li>de - German</li><li>en - English</li><li>es - Spanish</li><li>fr - French</li><li>it - Italian</li><li>pt - Portuguese</li><li>ru - Russian</li></ul> |



#### Example Usage

```python
number = 'number'
code_length = 5
security_code = 50
country_code = 'country-code'
language_code = 'en'

result = telephony_controller.sms_verify(number, code_length, security_code, country_code, language_code)

```


### <a name="verify_security_code"></a>![Method: ](https://apidocs.io/img/method.png ".Telephony.verify_security_code") verify_security_code

> Check if a security code from one of the verify APIs is valid. See: https://www.neutrinoapi.com/api/verify-security-code/

```python
def verify_security_code(self,
                             security_code)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| securityCode |  ``` Required ```  | The security code to verify |



#### Example Usage

```python
security_code = 'security-code'

result = telephony_controller.verify_security_code(security_code)

```


### <a name="phone_playback"></a>![Method: ](https://apidocs.io/img/method.png ".Telephony.phone_playback") phone_playback

> Make an automated call to any valid phone number and playback an audio message. See: https://www.neutrinoapi.com/api/phone-playback/

```python
def phone_playback(self,
                       number,
                       audio_url)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| number |  ``` Required ```  | The phone number to call. Must be in valid international format |
| audioUrl |  ``` Required ```  | A URL to a valid audio file. Accepted audio formats are:<ul><li>MP3</li><li>WAV</li><li>OGG</ul></ul>You can use the following MP3 URL for testing:<br/>https://www.neutrinoapi.com/test-files/test1.mp3 |



#### Example Usage

```python
number = 'number'
audio_url = 'audio-url'

result = telephony_controller.phone_playback(number, audio_url)

```


### <a name="hlr_lookup"></a>![Method: ](https://apidocs.io/img/method.png ".Telephony.hlr_lookup") hlr_lookup

> Connect to the global mobile cellular network and retrieve the status of a mobile device. See: https://www.neutrinoapi.com/api/hlr-lookup/

```python
def hlr_lookup(self,
                   number,
                   country_code=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| number |  ``` Required ```  | A phone number |
| countryCode |  ``` Optional ```  | ISO 2-letter country code, assume numbers are based in this country.<br/>If not set numbers are assumed to be in international format (with or without the leading + sign) |



#### Example Usage

```python
number = 'number'
country_code = 'country-code'

result = telephony_controller.hlr_lookup(number, country_code)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="e_commerce"></a>![Class: ](https://apidocs.io/img/class.png ".ECommerce") ECommerce

### Get controller instance

An instance of the ``` ECommerce ``` class can be accessed from the API Client.

```python
 e_commerce_controller = client.e_commerce
```

### <a name="bin_lookup"></a>![Method: ](https://apidocs.io/img/method.png ".ECommerce.bin_lookup") bin_lookup

> Perform a BIN (Bank Identification Number) or IIN (Issuer Identification Number) lookup. See: https://www.neutrinoapi.com/api/bin-lookup/

```python
def bin_lookup(self,
                   bin_number,
                   customer_ip=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| binNumber |  ``` Required ```  | The BIN or IIN number (the first 6 digits of a credit card number) |
| customerIp |  ``` Optional ```  | Pass in the customers IP address and we will return some extra information about them |



#### Example Usage

```python
bin_number = 'bin-number'
customer_ip = 'customer-ip'

result = e_commerce_controller.bin_lookup(bin_number, customer_ip)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="geolocation"></a>![Class: ](https://apidocs.io/img/class.png ".Geolocation") Geolocation

### Get controller instance

An instance of the ``` Geolocation ``` class can be accessed from the API Client.

```python
 geolocation_controller = client.geolocation
```

### <a name="geocode_address"></a>![Method: ](https://apidocs.io/img/method.png ".Geolocation.geocode_address") geocode_address

> Geocode an address, partial address or just the name of a place. See: https://www.neutrinoapi.com/api/geocode-address/

```python
def geocode_address(self,
                        address,
                        country_code=None,
                        language_code='en',
                        fuzzy_search=False)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| address |  ``` Required ```  | The address, partial address or name of a place to try and locate |
| countryCode |  ``` Optional ```  | The ISO 2-letter country code to be biased towards (the default is no country bias) |
| languageCode |  ``` Optional ```  ``` DefaultValue ```  | The language to display results in, available languages are:<ul><li>de, en, es, fr, it, pt, ru</li></ul> |
| fuzzySearch |  ``` Optional ```  ``` DefaultValue ```  | If no matches are found for the given address, start performing a recursive fuzzy search until a geolocation is found. We use a combination of approximate string matching and data cleansing to find possible location matches |



#### Example Usage

```python
address = 'address'
country_code = 'country-code'
language_code = 'en'
fuzzy_search = False

result = geolocation_controller.geocode_address(address, country_code, language_code, fuzzy_search)

```


### <a name="ip_info"></a>![Method: ](https://apidocs.io/img/method.png ".Geolocation.ip_info") ip_info

> Get location information about an IP address and do reverse DNS (PTR) lookups. See: https://www.neutrinoapi.com/api/ip-info/

```python
def ip_info(self,
                ip,
                reverse_lookup=False)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| ip |  ``` Required ```  | IPv4 or IPv6 address |
| reverseLookup |  ``` Optional ```  ``` DefaultValue ```  | Do a reverse DNS (PTR) lookup. This option can add extra delay to the request so only use it if you need it |



#### Example Usage

```python
ip = 'ip'
reverse_lookup = False

result = geolocation_controller.ip_info(ip, reverse_lookup)

```


### <a name="geocode_reverse"></a>![Method: ](https://apidocs.io/img/method.png ".Geolocation.geocode_reverse") geocode_reverse

> Convert a geographic coordinate (latitude and longitude) into a real world address or location. See: https://www.neutrinoapi.com/api/geocode-reverse/

```python
def geocode_reverse(self,
                        latitude,
                        longitude,
                        language_code='en')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| latitude |  ``` Required ```  | The location latitude in decimal degrees format |
| longitude |  ``` Required ```  | The location longitude in decimal degrees format |
| languageCode |  ``` Optional ```  ``` DefaultValue ```  | The language to display results in, available languages are:<ul><li>de, en, es, fr, it, pt, ru</li></ul> |



#### Example Usage

```python
latitude = 'latitude'
longitude = 'longitude'
language_code = 'en'

result = geolocation_controller.geocode_reverse(latitude, longitude, language_code)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="security_and_networking"></a>![Class: ](https://apidocs.io/img/class.png ".SecurityAndNetworking") SecurityAndNetworking

### Get controller instance

An instance of the ``` SecurityAndNetworking ``` class can be accessed from the API Client.

```python
 security_and_networking_controller = client.security_and_networking
```

### <a name="ip_blocklist"></a>![Method: ](https://apidocs.io/img/method.png ".SecurityAndNetworking.ip_blocklist") ip_blocklist

> The IP Blocklist API will detect potentially malicious or dangerous IP addresses. See: https://www.neutrinoapi.com/api/ip-blocklist/

```python
def ip_blocklist(self,
                     ip)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| ip |  ``` Required ```  | An IPv4 or IPv6 address |



#### Example Usage

```python
ip = 'ip'

result = security_and_networking_controller.ip_blocklist(ip)

```


### <a name="email_verify"></a>![Method: ](https://apidocs.io/img/method.png ".SecurityAndNetworking.email_verify") email_verify

> SMTP based email address verification. See: https://www.neutrinoapi.com/api/email-verify/

```python
def email_verify(self,
                     email,
                     fix_typos=False)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | An email address |
| fixTypos |  ``` Optional ```  ``` DefaultValue ```  | Automatically attempt to fix typos in the address |



#### Example Usage

```python
email = 'email'
fix_typos = False

result = security_and_networking_controller.email_verify(email, fix_typos)

```


### <a name="host_reputation"></a>![Method: ](https://apidocs.io/img/method.png ".SecurityAndNetworking.host_reputation") host_reputation

> Check the reputation of an IP address, domain name, FQDN or URL against a comprehensive list of blacklists and blocklists. See: https://www.neutrinoapi.com/api/host-reputation/

```python
def host_reputation(self,
                        host,
                        list_rating=3)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| host |  ``` Required ```  | An IP address, domain name, FQDN or URL.<br/>If you supply a domain/URL it will be checked against the URI DNSBL lists |
| listRating |  ``` Optional ```  ``` DefaultValue ```  | Only check lists with this rating or better |



#### Example Usage

```python
host = 'host'
list_rating = 3

result = security_and_networking_controller.host_reputation(host, list_rating)

```


### <a name="ip_probe"></a>![Method: ](https://apidocs.io/img/method.png ".SecurityAndNetworking.ip_probe") ip_probe

> Analyze and extract provider information for an IP address. See: https://www.neutrinoapi.com/api/ip-probe/

```python
def ip_probe(self,
                 ip)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| ip |  ``` Required ```  | IPv4 or IPv6 address |



#### Example Usage

```python
ip = 'ip'

result = security_and_networking_controller.ip_probe(ip)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="data_tools"></a>![Class: ](https://apidocs.io/img/class.png ".DataTools") DataTools

### Get controller instance

An instance of the ``` DataTools ``` class can be accessed from the API Client.

```python
 data_tools_controller = client.data_tools
```

### <a name="user_agent_info"></a>![Method: ](https://apidocs.io/img/method.png ".DataTools.user_agent_info") user_agent_info

> Parse, validate and get detailed user-agent information from a user agent string. See: https://www.neutrinoapi.com/api/user-agent-info/

```python
def user_agent_info(self,
                        user_agent)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| userAgent |  ``` Required ```  | A user agent string |



#### Example Usage

```python
user_agent = 'user-agent'

result = data_tools_controller.user_agent_info(user_agent)

```


### <a name="phone_validate"></a>![Method: ](https://apidocs.io/img/method.png ".DataTools.phone_validate") phone_validate

> Parse, validate and get location information about a phone number. See: https://www.neutrinoapi.com/api/phone-validate/

```python
def phone_validate(self,
                       number,
                       country_code=None,
                       ip=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| number |  ``` Required ```  | A phone number. This can be in international format (E.164) or local format. If passing local format you should use the 'country-code' or 'ip' options as well |
| countryCode |  ``` Optional ```  | ISO 2-letter country code, assume numbers are based in this country.<br/>If not set numbers are assumed to be in international format (with or without the leading + sign) |
| ip |  ``` Optional ```  | Pass in a users IP address and we will assume numbers are based in the country of the IP address |



#### Example Usage

```python
number = 'number'
country_code = 'country-code'
ip = 'ip'

result = data_tools_controller.phone_validate(number, country_code, ip)

```


### <a name="convert"></a>![Method: ](https://apidocs.io/img/method.png ".DataTools.convert") convert

> A powerful unit conversion tool. See: https://www.neutrinoapi.com/api/convert/

```python
def convert(self,
                from_value,
                from_type,
                to_type)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| fromValue |  ``` Required ```  | The value to convert from (e.g. 10.95) |
| fromType |  ``` Required ```  | The type of the value to convert from (e.g. USD) |
| toType |  ``` Required ```  | The type to convert to (e.g. EUR) |



#### Example Usage

```python
from_value = 'from-value'
from_type = 'from-type'
to_type = 'to-type'

result = data_tools_controller.convert(from_value, from_type, to_type)

```


### <a name="bad_word_filter"></a>![Method: ](https://apidocs.io/img/method.png ".DataTools.bad_word_filter") bad_word_filter

> Detect bad words, swear words and profanity in a given text. See: https://www.neutrinoapi.com/api/bad-word-filter/

```python
def bad_word_filter(self,
                        content,
                        censor_character=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| content |  ``` Required ```  | The content to scan. This can be either a URL to load content from or an actual content string |
| censorCharacter |  ``` Optional ```  | The character to use to censor out the bad words found |



#### Example Usage

```python
content = 'content'
censor_character = 'censor-character'

result = data_tools_controller.bad_word_filter(content, censor_character)

```


### <a name="email_validate"></a>![Method: ](https://apidocs.io/img/method.png ".DataTools.email_validate") email_validate

> Parse, validate and clean an email address. See: https://www.neutrinoapi.com/api/email-validate/

```python
def email_validate(self,
                       email,
                       fix_typos=False)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | An email address |
| fixTypos |  ``` Optional ```  ``` DefaultValue ```  | Automatically attempt to fix typos in the address |



#### Example Usage

```python
email = 'email'
fix_typos = False

result = data_tools_controller.email_validate(email, fix_typos)

```


[Back to List of Controllers](#list_of_controllers)



