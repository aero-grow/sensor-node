#!/usr/bin/python

from devices.atlas.base_response import BaseResponse
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

    def write(self, cmd) -> None:
        self.device.write(cmd=cmd)

    def read(self, num_of_bytes=31) -> BaseResponse:
        return self.device.read(num_of_bytes=num_of_bytes)
    
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

    def set_name(self, new_name: str):
        if(len(new_name) > 16):
            new_name = new_name[0:15]
        return self.device.query(f'Name,{new_name}')

    def get_info(self):
        return self.device.query("I")

    def read_value(self):
        return self.device.query("R")

    def sleep(self):
        return self.device.query("SLEEP")
    
    def lock_protocol(self, unlock = False):
        return self.device.query(f'Plock,{0 if unlock else 1}')

class TempCompensatedBaseDevice(BaseDevice):

    def __init__(self, device: AtlasI2C):
        super().__init__(device)

    def set_temp_compensation(self, current_temp: int = 20):
        return self.device.query(f'T,{current_temp}')
    
    def read_temp_compensated(self, current_temp: int = 20):
        '''
        Reads the value of D.O. after setting the temperature compensation.
        Basically, does two actions at once (set_temp_compensation & read), reducing delay time.
        '''
        return self.device.query(f'RT,{current_temp}')