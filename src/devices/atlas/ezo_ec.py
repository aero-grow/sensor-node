#!/usr/bin/python

from .atlasi2c import AtlasI2C
from .base_device import BaseDevice

class EzoEc(BaseDevice):
    def __init__(self, device: AtlasI2C):
        super().__init__(device)