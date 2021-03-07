#!/usr/bin/python

from devices.atlas.base_response import SingleFloatResponse
from .atlasi2c import AtlasI2C
from .base_device import TempCompensatedBaseDevice

class EzopH(TempCompensatedBaseDevice):
    def __init__(self, device: AtlasI2C):
        super().__init__(device)

    def slope(self):
        return self.device.query("Slope,?")

    def read_value(self) -> SingleFloatResponse:
        response = super().read_value()
        return SingleFloatResponse(response.status_code, response.response_data)
        
    def read_temp_compensated(self, current_temp: int = 20):
        '''
        Reads the value of D.O. after setting the temperature compensation.
        Basically, does two actions at once (set_temp_compensation & read), reducing delay time.
        '''
        response = super().read_temp_compensated(current_temp=current_temp)
        return SingleFloatResponse(response.status_code, response.response_data)