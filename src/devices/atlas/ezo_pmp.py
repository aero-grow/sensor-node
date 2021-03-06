#!/usr/bin/python

from .atlasi2c import AtlasI2C
from .base_device import BaseDevice

class EzoPMP(BaseDevice):
    def __init__(self, device: AtlasI2C):
        super().__init__(device)

    def dispense(self, reverse = False):
        if(reverse):
            return self.device.query("D,-*")
        else:
            return self.device.query("D,*")
    
    def dispense_volumne(self, mililiters: int, reverse = False):
        if(reverse):
            return self.device.query(f'D,-{mililiters}')
        else:
            return self.device.query(f'D,{mililiters}')
    
    def dispense_over_time(self, mililiters: int, minutes: int, reverse = False):
        if(reverse):
            return self.device.query(f'D,-{mililiters},{minutes}')
        else:
            return self.device.query(f'D,{mililiters},{minutes}')

    def dispense_constantly(self, mililiters_per_minute: int, duration_in_minutes: int = 0, reverse = False):
        duration_as_string = "*" if duration_in_minutes == 0 else str(duration_in_minutes)
        if(reverse):
            return self.device.query(f'DC,-{mililiters_per_minute},{duration_as_string}')
        else:
            return self.device.query(f'DC,{mililiters_per_minute},{duration_as_string}')
    
    def pause_dispensing(self):
        return self.device.query("P")
    
    def stop_dispensing(self):
        return self.device.query("X")

