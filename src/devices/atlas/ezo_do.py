#!/usr/bin/python

from .atlasi2c import AtlasI2C
from .base_device import TempCompensatedBaseDevice

class EzoDO(TempCompensatedBaseDevice):
    def __init__(self, device: AtlasI2C):
        super().__init__(device)

