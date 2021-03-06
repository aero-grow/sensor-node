#!/usr/bin/python

from enum import Enum
from .atlasi2c import AtlasI2C
from .base_device import BaseDevice

class RTDTempScale(Enum):
    celsius = "c"
    kelvin = "k"
    fahrenheit = "f"

class EzoRTD(BaseDevice):
    def __init__(self, device: AtlasI2C):
        super().__init__(device)

    def set_scale(self, scale: RTDTempScale = RTDTempScale.celsius):
        return self.device.query(f'S,{scale.value}')