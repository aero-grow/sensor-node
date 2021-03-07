#!/usr/bin/python

from devices.atlas.base_response import MultipleResponse
from devices.atlas.constants import AtlasResponseCodes
from .atlasi2c import AtlasI2C
from .base_device import BaseDevice

class HUMResponse(MultipleResponse):
    def __init__(self, status_code: AtlasResponseCodes, response_data: str):
        super().__init__(status_code=status_code, response_data=response_data)

    @property
    def humidity(self) -> int:
        if(len(self.responses) > 0):
            return self.responses[0]

    @property
    def temp(self) -> int:
        if(len(self.responses) > 1):
            return self.responses[1]

    @property
    def dew(self) -> int:
        if(len(self.responses) > 2):
            return self.responses[2]
        
class EzoHUM(BaseDevice):
    def __init__(self, device: AtlasI2C):
        super().__init__(device)
        
    def read_value(self) -> HUMResponse:
        response = super().read_value()
        return HUMResponse(response.status_code, response.response_data)