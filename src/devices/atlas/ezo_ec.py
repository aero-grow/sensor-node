#!/usr/bin/python

from enum import Enum
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
