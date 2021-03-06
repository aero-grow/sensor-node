#!/usr/bin/python
import typing
from .atlas import (
    AtlasI2C,
    AtlasDeviceTypes,
    BaseDevice,
    EzoCO2,
    EzoDO,
    EzoEC,
    EzoHUM,
    EzoORP,
    EzopH,
    EzoPMP,
    EzoPRS,
    EzoRTD
)

class SensorManager:
    device = AtlasI2C()

    def __init__(self):
        self.devices = self.find_devices()
    
    def find_devices(self) -> typing.List[BaseDevice]:
        devices = []
        for address in self.device.list_i2c_devices():
            self.device.set_i2c_address(address)
            response = self.device.query("I")
            moduletype = response.split(",")[1] 
            name = self.device.query("name,?").split(",")[1]

            devices.append(self.instantiate_specific_sensor_type(address, moduletype, name))
        return devices
    
    def instantiate_specific_sensor_type(self, address: int, moduletype: str, name: str) -> BaseDevice:
        if(moduletype == AtlasDeviceTypes.CO2):
            return EzoCO2(AtlasI2C(address = address, moduletype = moduletype, name = name))
        if(moduletype == AtlasDeviceTypes.DO):
            return EzoDO(AtlasI2C(address = address, moduletype = moduletype, name = name))
        if(moduletype == AtlasDeviceTypes.EC):
            return EzoEC(AtlasI2C(address = address, moduletype = moduletype, name = name))
        if(moduletype == AtlasDeviceTypes.HUM):
            return EzoHUM(AtlasI2C(address = address, moduletype = moduletype, name = name))
        if(moduletype == AtlasDeviceTypes.ORP):
            return EzoORP(AtlasI2C(address = address, moduletype = moduletype, name = name))
        if(moduletype == AtlasDeviceTypes.PH):
            return EzopH(AtlasI2C(address = address, moduletype = moduletype, name = name))
        if(moduletype == AtlasDeviceTypes.PMP):
            return EzoPMP(AtlasI2C(address = address, moduletype = moduletype, name = name))
        if(moduletype == AtlasDeviceTypes.PRS):
            return EzoPRS(AtlasI2C(address = address, moduletype = moduletype, name = name))
        if(moduletype == AtlasDeviceTypes.RTD):
            return EzoRTD(AtlasI2C(address = address, moduletype = moduletype, name = name))
        
        return BaseDevice(AtlasI2C(address = address, moduletype = moduletype, name = name))
