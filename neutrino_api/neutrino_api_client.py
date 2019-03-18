# -*- coding: utf-8 -*-

"""
    neutrino_api

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""

from neutrino_api.decorators import lazy_property
from neutrino_api.configuration import Configuration
from neutrino_api.controllers.www import WWW
from neutrino_api.controllers.imaging import Imaging
from neutrino_api.controllers.telephony import Telephony
from neutrino_api.controllers.e_commerce import ECommerce
from neutrino_api.controllers.geolocation import Geolocation
from neutrino_api.controllers.security_and_networking import SecurityAndNetworking
from neutrino_api.controllers.data_tools import DataTools


class NeutrinoApiClient(object):

    config = Configuration

    @lazy_property
    def www(self):
        return WWW()

    @lazy_property
    def imaging(self):
        return Imaging()

    @lazy_property
    def telephony(self):
        return Telephony()

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
    def data_tools(self):
        return DataTools()


    def __init__(self,
                 user_id=None,
                 api_key=None):
        if user_id != None:
            Configuration.user_id = user_id
        if api_key != None:
            Configuration.api_key = api_key


