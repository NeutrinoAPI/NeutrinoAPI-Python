# -*- coding: utf-8 -*-

"""
    neutrino_api.neutrino_api_client

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""
from .decorators import lazy_property
from .controllers.data_tools import DataTools
from .controllers.e_commerce import ECommerce
from .controllers.geolocation import Geolocation
from .controllers.security_and_networking import SecurityAndNetworking
from .controllers.telephony import Telephony
from .controllers.imaging import Imaging
from .configuration import Configuration

class NeutrinoApiClient(object):

    @lazy_property
    def data_tools(self):
        return DataTools()

    @lazy_property
    def e_commerce(self):
        return ECommerce()

    @lazy_property
    def geolocation(self):
        return Geolocation()

    @lazy_property
    def security_and_networking(self):
        return SecurityAndNetworking()

    @lazy_property
    def telephony(self):
        return Telephony()

    @lazy_property
    def imaging(self):
        return Imaging()


    def __init__(self, 
                 user_id = None,
                 api_key = None):
        if user_id != None:
            Configuration.user_id = user_id
        if api_key != None:
            Configuration.api_key = api_key


