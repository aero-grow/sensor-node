#!/usr/bin/python

from enum import Enum

from devices.atlas.base_response import BaseResponse, SingleFloatResponse
from .constants import AtlasResponseCodes
from .atlasi2c import AtlasI2C
from .base_device import BaseDevice

class PRSUnits(Enum):
    psi = "psi"
    atm = "atm"
    bar = "bar"
    kPa = "kPa"
    inchesOfWater = "inh2o"
    cmOfWater = "cmh2o"

class EzoPRS(BaseDevice):
    def __init__(self, device: AtlasI2C):
        super().__init__(device)
        
    def enable_alarm(self, disable: bool = False):
        return self.device.query(f'Alarm,en,{0 if disable else 1}')
    
    def set_alarm(self, unit: int = 3, tolerence: int = None):
        response = self.device.query(f'Alarm,{unit}')

        if(tolerence is not None and response.status_code == AtlasResponseCodes.SUCCESS):
            return self.device.query(f'Alarm,tol,{tolerence}')
        else:
            return response

    def change_unit(self, unit: PRSUnits = PRSUnits.bar, output_to_read: bool = None):
        response = self.device.query(f'U,{unit.value}')

        if(output_to_read is not None and response.status_code == AtlasResponseCodes.SUCCESS):
            return self.device.query(f'U,{1 if output_to_read else 0}')
        else:
            return response

    def read_value(self) -> SingleFloatResponse:
        response = super().read_value()
        return SingleFloatResponse(response.status_code, response.response_data)