#!/usr/bin/python

from .atlasi2c import AtlasI2C
from .constants import AtlasDeviceTypes

class BaseDevice:
    def __init__(self, device: AtlasI2C):
        self.device = device
    
    @property
    def name(self) -> str:
        return self.device.name
        
    @property
    def address(self) -> int:
        return self.device.address
        
    @property
    def moduletype(self) -> AtlasDeviceTypes:
        return self.device.moduletype
    
    def change_address(self, new_address: int) -> None:
        if(new_address < 1 or new_address > 127):
            #TODO: maybe throw exception or return error
            pass
        return self.device.write(f'I2C,{new_address}')

    def find(self):
        return self.device.query("Find")

    def toggle_led(self, on = True):
        return self.device.query(f'L,{1 if on else 0}')

    def led_status(self):
        response = self.device.query("L,?")
        return True if response.split(",")[1] == "1" else False

    def get_info(self):
        return self.device.query("I")

    def read_value(self):
        return self.device.query("R")

    def sleep(self):
        return self.device.query("SLEEP")
    
    def lock_protocol(self, unlock = False):
        return self.device.query(f'Plock,{0 if unlock else 1}')