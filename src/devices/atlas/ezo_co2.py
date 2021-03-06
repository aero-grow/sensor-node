#!/usr/bin/python

from .atlasi2c import AtlasI2C
from .base_device import BaseDevice
from .constants import AtlasResponseCodes

class EzoCO2(BaseDevice):
    def __init__(self, device: AtlasI2C):
        super().__init__(device)

    def enable_alarm(self, disable: bool = False):
        return self.device.query(f'Alarm,en,{0 if disable else 1}')
    
    def set_alarm(self, ppm: int = 2000, tolerence: int = None):
        response = self.device.query(f'Alarm,{ppm}')

        if(tolerence is not None and response.status_code == AtlasResponseCodes.SUCCESS):
            return self.device.query(f'Alarm,tol,{tolerence}')
        else:
            return response
    
    