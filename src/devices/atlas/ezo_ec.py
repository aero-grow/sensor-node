#!/usr/bin/python

from enum import Enum

from devices.atlas.base_response import BaseResponse, SingleFloatResponse
from devices.atlas.constants import AtlasResponseCodes
from .atlasi2c import AtlasI2C
from .base_device import TempCompensatedBaseDevice


class ECProbeType(Enum):
    K01 = "0.1"
    K1 = "1.0"
    K10 = "10"

class EzoEC(TempCompensatedBaseDevice):
    def __init__(self, device: AtlasI2C):
        super().__init__(device)
    
    def set_probe_type(self, probe_type: ECProbeType = ECProbeType.K1):
        return self.device.query(f'K,{probe_type.value}')

    def set_tds_conversion_factor(self, factor: float = 0.54):
        return self.device.query(f'TDS,{factor}')

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