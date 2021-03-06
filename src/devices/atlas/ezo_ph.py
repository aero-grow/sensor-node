#!/usr/bin/python

from .atlasi2c import AtlasI2C
from .base_device import TempCompensatedBaseDevice

class EzopH(TempCompensatedBaseDevice):
    def __init__(self, device: AtlasI2C):
        super().__init__(device)

    def slope(self):
        return self.device.query("Slope,?")