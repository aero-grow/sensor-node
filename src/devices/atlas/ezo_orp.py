#!/usr/bin/python

from devices.atlas.base_response import SingleFloatResponse
from .atlasi2c import AtlasI2C
from .base_device import BaseDevice

class EzoORP(BaseDevice):
    def __init__(self, device: AtlasI2C):
        super().__init__(device)
        
    def read_value(self) -> SingleFloatResponse:
        response = super().read_value()
        return SingleFloatResponse(response.status_code, response.response_data)