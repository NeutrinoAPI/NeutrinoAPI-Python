# Getting started

## How to Build


You must have Python 2 >=2.7.9 or Python 3 >=3.4 installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
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
from neutrino_api.neutrino_api_client.py import *
```

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=NeutrinoAPI-Python&libraryName=neutrino_api.neutrino_api_client.py&projectName=neutrino_api)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=NeutrinoAPI-Python&libraryName=neutrino_api.neutrino_api_client.py&projectName=neutrino_api)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke 'pip install -r test-requirements.txt'
  3. Invoke 'nosetests'

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
user_id = "user_id" # Your user ID
api_key = "api_key" # Your API key

client = NeutrinoApiClient(user_id, api_key)
```

# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [DataTools](#data_tools)
* [ECommerce](#e_commerce)
* [Geolocation](#geolocation)
* [SecurityAndNetworking](#security_and_networking)
* [Telephony](#telephony)
* [Imaging](#imaging)

## <a name="data_tools"></a>![Class: ](https://apidocs.io/img/class.png ".DataTools") DataTools

### Get controller instance

An instance of the ``` DataTools ``` class can be accessed from the API Client.

```python
 data_tools_client = client.data_tools
```

### <a name="convert"></a>![Method: ](https://apidocs.io/img/method.png ".DataTools.convert") convert

> A powerful unit and currency conversion tool

```python
def convert(self,
                from_value,
                from_type,
                to_type)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| fromValue |  ``` Required ```  | The value to convert from |
| fromType |  ``` Required ```  | The type of the value to convert from |
| toType |  ``` Required ```  | The type to convert to |



#### Example Usage

```python
from_value = 'from-value'
from_type = 'from-type'
to_type = 'to-type'

result = data_tools_client.convert(from_value, from_type, to_type)

```


### <a name="bad_word_filter"></a>![Method: ](https://apidocs.io/img/method.png ".DataTools.bad_word_filter") bad_word_filter

> Detect bad words, swear words and profanity in a given text

```python
def bad_word_filter(self,
                        content,
                        censor_character=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| content |  ``` Required ```  | The text content to check. This can be either a URL to load content from or an actual content string |
| censorCharacter |  ``` Optional ```  | The character to use to censor out the bad words found |



#### Example Usage

```python
content = 'content'
censor_character = 'censor-character'

result = data_tools_client.bad_word_filter(content, censor_character)

```


### <a name="email_validate"></a>![Method: ](https://apidocs.io/img/method.png ".DataTools.email_validate") email_validate

> Parse, validate and clean an email address

```python
def email_validate(self,
                       email,
                       fix_typos=False)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| email |  ``` Required ```  | The email address |
| fixTypos |  ``` Optional ```  ``` DefaultValue ```  | Automatically attempt to fix typos in the address |



#### Example Usage

```python
email = 'email'
fix_typos = False

result = data_tools_client.email_validate(email, fix_typos)

```


### <a name="html_clean"></a>![Method: ](https://apidocs.io/img/method.png ".DataTools.html_clean") html_clean

> Clean and sanitize untrusted HTML

```python
def html_clean(self,
                   content,
                   output_type)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| content |  ``` Required ```  | The HTML content. This can be either a URL to load HTML from or an actual HTML content string |
| outputType |  ``` Required ```  | The level of sanitization, possible values are: plain-text, simple-text, basic-html, basic-html-with-images, advanced-html |



#### Example Usage

```python
content = 'content'
output_type = 'output-type'

result = data_tools_client.html_clean(content, output_type)

```


### <a name="code_highlight"></a>![Method: ](https://apidocs.io/img/method.png ".DataTools.code_highlight") code_highlight

> Code highlight will take raw source code and convert into nicely formatted HTML with syntax and keyword highlighting

```python
def code_highlight(self,
                       content,
                       mtype,
                       add_keyword_links=False)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| content |  ``` Required ```  | The source content. This can be either a URL to load from or an actual content string |
| mtype |  ``` Required ```  | The code type. See the API docs for all supported types |
| addKeywordLinks |  ``` Optional ```  ``` DefaultValue ```  | Add links on source code keywords to the relevant language documentation |



#### Example Usage

```python
content = 'content'
mtype = 'type'
add_keyword_links = False

result = data_tools_client.code_highlight(content, mtype, add_keyword_links)

```


### <a name="user_agent_info"></a>![Method: ](https://apidocs.io/img/method.png ".DataTools.user_agent_info") user_agent_info

> Parse, validate and get detailed user-agent information from a user agent string

```python
def user_agent_info(self,
                        user_agent)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| userAgent |  ``` Required ```  | A user-agent string |



#### Example Usage

```python
user_agent = 'user-agent'

result = data_tools_client.user_agent_info(user_agent)

```


### <a name="html_extract"></a>![Method: ](https://apidocs.io/img/method.png ".DataTools.html_extract") html_extract

> Extract specific HTML tag contents or attributes from complex HTML or XHTML content

```python
def html_extract(self,
                     content,
                     tag,
                     attribute=None,
                     base_url=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| content |  ``` Required ```  | The HTML content. This can be either a URL to load HTML from or an actual HTML content string |
| tag |  ``` Required ```  | The HTML tag(s) to extract data from. This can just be a simple tag name like 'img' OR a CSS/jQuery style selector |
| attribute |  ``` Optional ```  | If set, then extract data from the specified tag attribute. If not set, then data will be extracted from the tags inner content |
| baseUrl |  ``` Optional ```  | The base URL to replace into realive links |



#### Example Usage

```python
content = 'content'
tag = 'tag'
attribute = 'attribute'
base_url = 'base-url'

result = data_tools_client.html_extract(content, tag, attribute, base_url)

```


### <a name="phone_validate"></a>![Method: ](https://apidocs.io/img/method.png ".DataTools.phone_validate") phone_validate

> Parse, validate and get location information about a phone number

```python
def phone_validate(self,
                       number,
                       country_code=None,
                       ip=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| number |  ``` Required ```  | The phone number |
| countryCode |  ``` Optional ```  | ISO 2-letter country code, assume numbers are based in this country. If not set numbers are assumed to be in international format (with or without the leading + sign) |
| ip |  ``` Optional ```  | Pass in a users IP address and we will assume numbers are based in the country of the IP address |



#### Example Usage

```python
number = 'number'
country_code = 'country-code'
ip = 'ip'

result = data_tools_client.phone_validate(number, country_code, ip)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="e_commerce"></a>![Class: ](https://apidocs.io/img/class.png ".ECommerce") ECommerce

### Get controller instance

An instance of the ``` ECommerce ``` class can be accessed from the API Client.

```python
 e_commerce_client = client.e_commerce
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
| customerIp |  ``` Optional ```  | Pass in a customers remote IP address. The API will then determine the country of the IP address and match it against the BIN country. This feature is designed for fraud prevention and detection checks. |



#### Example Usage

```python
bin_number = 'bin-number'
customer_ip = 'customer-ip'

result = e_commerce_client.bin_lookup(bin_number, customer_ip)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="geolocation"></a>![Class: ](https://apidocs.io/img/class.png ".Geolocation") Geolocation

### Get controller instance

An instance of the ``` Geolocation ``` class can be accessed from the API Client.

```python
 geolocation_client = client.geolocation
```

### <a name="geocode_reverse"></a>![Method: ](https://apidocs.io/img/method.png ".Geolocation.geocode_reverse") geocode_reverse

> Convert a geographic coordinate (latitude and longitude) into a real world address or location.

```python
def geocode_reverse(self,
                        latitude,
                        longitude,
                        language_code='en')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| latitude |  ``` Required ```  | The location latitude |
| longitude |  ``` Required ```  | The location longitude |
| languageCode |  ``` Optional ```  ``` DefaultValue ```  | The language to display results in, available languages are: de, en, es, fr, it, pt, ru |



#### Example Usage

```python
latitude = 75.3087793455034
longitude = 75.3087793455034
language_code = 'en'

result = geolocation_client.geocode_reverse(latitude, longitude, language_code)

```


### <a name="geocode_address"></a>![Method: ](https://apidocs.io/img/method.png ".Geolocation.geocode_address") geocode_address

> Geocode an address, partial address or the name of a location

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
| address |  ``` Required ```  | The address or partial address to try and locate |
| countryCode |  ``` Optional ```  | The ISO 2-letter country code to be biased towards (default is no country bias) |
| languageCode |  ``` Optional ```  ``` DefaultValue ```  | The language to display results in, available languages are: de, en, es, fr, it, pt, ru |
| fuzzySearch |  ``` Optional ```  ``` DefaultValue ```  | If no matches are found for the given address, start performing a recursive fuzzy search until a geolocation is found. We use a combination of approximate string matching and data cleansing to find possible location matches |



#### Example Usage

```python
address = 'address'
country_code = 'country-code'
language_code = 'en'
fuzzy_search = False

result = geolocation_client.geocode_address(address, country_code, language_code, fuzzy_search)

```


### <a name="ip_info"></a>![Method: ](https://apidocs.io/img/method.png ".Geolocation.ip_info") ip_info

> Get location information about an IP address and do reverse DNS (PTR) lookups.

```python
def ip_info(self,
                ip,
                reverse_lookup=False)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| ip |  ``` Required ```  | The IP address |
| reverseLookup |  ``` Optional ```  ``` DefaultValue ```  | Do a reverse DNS (PTR) lookup. This option can add extra delay to the request so only use it if you need it |



#### Example Usage

```python
ip = 'ip'
reverse_lookup = False

result = geolocation_client.ip_info(ip, reverse_lookup)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="security_and_networking"></a>![Class: ](https://apidocs.io/img/class.png ".SecurityAndNetworking") SecurityAndNetworking

### Get controller instance

An instance of the ``` SecurityAndNetworking ``` class can be accessed from the API Client.

```python
 security_and_networking_client = client.security_and_networking
```

### <a name="host_reputation"></a>![Method: ](https://apidocs.io/img/method.png ".SecurityAndNetworking.host_reputation") host_reputation

> Check the reputation of an IP address or domain against a comprehensive list of blacklists and blocklists (DNSBLs)

```python
def host_reputation(self,
                        host)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| host |  ``` Required ```  | An IPv4 address or a domain name. If you supply a domain name it will be checked against the URI DNSBL list |



#### Example Usage

```python
host = 'host'

result = security_and_networking_client.host_reputation(host)

```


### <a name="ip_blocklist"></a>![Method: ](https://apidocs.io/img/method.png ".SecurityAndNetworking.ip_blocklist") ip_blocklist

> The IP Blocklist API will detect potentially malicious or dangerous IP addresses

```python
def ip_blocklist(self,
                     ip)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| ip |  ``` Required ```  | An IPv4 address |



#### Example Usage

```python
ip = 'ip'

result = security_and_networking_client.ip_blocklist(ip)

```


### <a name="ip_probe"></a>![Method: ](https://apidocs.io/img/method.png ".SecurityAndNetworking.ip_probe") ip_probe

> Analyze and extract provider information for an IP address

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

result = security_and_networking_client.ip_probe(ip)

```


### <a name="url_info"></a>![Method: ](https://apidocs.io/img/method.png ".SecurityAndNetworking.url_info") url_info

> Parse, analyze and retrieve content from the supplied URL

```python
def url_info(self,
                 url,
                 fetch_content)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| url |  ``` Required ```  | The URL to process |
| fetchContent |  ``` Required ```  | If this URL responds with html, text, json or xml then return the response. This option is useful if you want to perform further processing on the URL content |



#### Example Usage

```python
url = 'url'
fetch_content = False

result = security_and_networking_client.url_info(url, fetch_content)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="telephony"></a>![Class: ](https://apidocs.io/img/class.png ".Telephony") Telephony

### Get controller instance

An instance of the ``` Telephony ``` class can be accessed from the API Client.

```python
 telephony_client = client.telephony
```

### <a name="hlr_lookup"></a>![Method: ](https://apidocs.io/img/method.png ".Telephony.hlr_lookup") hlr_lookup

> Connect to the global mobile cellular network and retrieve the status of a mobile device

```python
def hlr_lookup(self,
                   number,
                   country_code=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| number |  ``` Required ```  | A phone number |
| countryCode |  ``` Optional ```  | ISO 2-letter country code, assume numbers are based in this country. If not set numbers are assumed to be in international format (with or without the leading + sign) |



#### Example Usage

```python
number = 'number'
country_code = 'country-code'

result = telephony_client.hlr_lookup(number, country_code)

```


### <a name="verify_security_code"></a>![Method: ](https://apidocs.io/img/method.png ".Telephony.verify_security_code") verify_security_code

> Check if a security code from one of the verify APIs is valid

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
security_code = 166

result = telephony_client.verify_security_code(security_code)

```


### <a name="sms_verify"></a>![Method: ](https://apidocs.io/img/method.png ".Telephony.sms_verify") sms_verify

> Send a unique security code to any mobile device via SMS

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
| securityCode |  ``` Optional ```  | ass in your own security code. This is useful if you have implemented TOTP or similar 2FA methods. If not set then we will generate a secure random code (only numerical security codes are currently supported) |
| countryCode |  ``` Optional ```  | ISO 2-letter country code, assume numbers are based in this country. If not set numbers are assumed to be in international format (with or without the leading + sign) |
| languageCode |  ``` Optional ```  ``` DefaultValue ```  | The language to send the verification code in, available languages are: de - German, en - English, es - Spanish, fr - Fench, it - Italian, pt - Portuguese, ru - Russian |



#### Example Usage

```python
number = 'number'
code_length = 5
security_code = 166
country_code = 'country-code'
language_code = 'en'

result = telephony_client.sms_verify(number, code_length, security_code, country_code, language_code)

```


### <a name="phone_playback"></a>![Method: ](https://apidocs.io/img/method.png ".Telephony.phone_playback") phone_playback

> Make an automated call to any valid phone number and playback an audio message

```python
def phone_playback(self,
                       number,
                       audio_url)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| number |  ``` Required ```  | The phone number to call. Must be valid international format |
| audioUrl |  ``` Required ```  | A URL to a valid audio file. Accepted audio formats are: MP3, WAV, OGG |



#### Example Usage

```python
number = 'number'
audio_url = 'audio-url'

result = telephony_client.phone_playback(number, audio_url)

```


### <a name="phone_verify"></a>![Method: ](https://apidocs.io/img/method.png ".Telephony.phone_verify") phone_verify

> Make an automated call to any valid phone number and playback a unique security code

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
| securityCode |  ``` Optional ```  | Pass in your own security code. This is useful if you have implemented TOTP or similar 2FA methods. If not set then we will generate a secure random code (only numerical security codes are currently supported) |
| playbackDelay |  ``` Optional ```  ``` DefaultValue ```  | The delay in milliseconds between the playback of each security code |
| countryCode |  ``` Optional ```  | ISO 2-letter country code, assume numbers are based in this country. If not set numbers are assumed to be in international format (with or without the leading + sign) |
| languageCode |  ``` Optional ```  ``` DefaultValue ```  | The language to playback the verification code in, available languages are: de - German, en - English, es - Spanish, fr - Fench, it - Italian, pt - Portuguese, ru - Russian |



#### Example Usage

```python
number = 'number'
code_length = 6
security_code = 166
playback_delay = 800
country_code = 'country-code'
language_code = 'en'

result = telephony_client.phone_verify(number, code_length, security_code, playback_delay, country_code, language_code)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="imaging"></a>![Class: ](https://apidocs.io/img/class.png ".Imaging") Imaging

### Get controller instance

An instance of the ``` Imaging ``` class can be accessed from the API Client.

```python
 imaging_client = client.imaging
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
| width |  ``` Required ```  | Width to resize to (in px) |
| height |  ``` Required ```  | Height to resize to (in px) |
| format |  ``` Optional ```  ``` DefaultValue ```  | The output image format, can be either png or jpg |



#### Example Usage

```python
image_url = 'image-url'
width = 166
height = 166
format = 'png'

result = imaging_client.image_resize(image_url, width, height, format)

```


### <a name="qr_code"></a>![Method: ](https://apidocs.io/img/method.png ".Imaging.qr_code") qr_code

> Generate a QR code as a PNG image. See: https://www.neutrinoapi.com/api/qr-code/

```python
def qr_code(self,
                content,
                width=250,
                height=250,
                fg_color='#000000',
                bg_color='#ffffff')
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| content |  ``` Required ```  | The content to encode into the QR code (e.g. a URL or a phone number) |
| width |  ``` Optional ```  ``` DefaultValue ```  | The width of the QR code (in px) |
| height |  ``` Optional ```  ``` DefaultValue ```  | The height of the QR code (in px) |
| fgColor |  ``` Optional ```  ``` DefaultValue ```  | The QR code foreground color (you should always use a dark color for this) |
| bgColor |  ``` Optional ```  ``` DefaultValue ```  | The QR code background color (you should always use a light color for this) |



#### Example Usage

```python
content = 'content'
width = 250
height = 250
fg_color = '#000000'
bg_color = '#ffffff'

result = imaging_client.qr_code(content, width, height, fg_color, bg_color)

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
| position |  ``` Optional ```  ``` DefaultValue ```  | The position of the watermark image, possible values are: center, top-left, top-center, top-right, bottom-left, bottom-center, bottom-right |
| width |  ``` Optional ```  | If set resize the resulting image to this width (preserving aspect ratio) |
| height |  ``` Optional ```  | If set resize the resulting image to this height (preserving aspect ratio) |



#### Example Usage

```python
image_url = 'image-url'
watermark_url = 'watermark-url'
opacity = 50
format = 'png'
position = 'center'
width = 166
height = 166

result = imaging_client.image_watermark(image_url, watermark_url, opacity, format, position, width, height)

```


### <a name="html_5_render"></a>![Method: ](https://apidocs.io/img/method.png ".Imaging.html_5_render") html_5_render

> Render HTML and HTML5 content to PDF, JPG or PNG

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
                      zoom=1.0,
                      grayscale=False,
                      media_print=False,
                      media_queries=False,
                      forms=False,
                      css=None,
                      image_width=1024,
                      image_height=None)
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
zoom = 1.0
grayscale = False
media_print = False
media_queries = False
forms = False
css = 'css'
image_width = 1024
image_height = 166

result = imaging_client.html_5_render(content, format, page_size, title, margin, margin_left, margin_right, margin_top, margin_bottom, landscape, zoom, grayscale, media_print, media_queries, forms, css, image_width, image_height)

```


[Back to List of Controllers](#list_of_controllers)



