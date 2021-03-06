#!/usr/bin/python

from atlas import (
    AtlasI2C,
    AtlasDeviceTypes,
    BaseDevice,
    EzoCo2,
    EzoDo,
    EzoEc,
    EzoHum,
    EzoOrp,
    EzoPh,
    EzoPmp,
    EzoPrs,
    EzoRtd
)

class SensorManager:
    device = AtlasI2C()

    def __init__(self):
        self.devices = self.find_devices()
    
    def find_devices(self) -> [BaseDevice]:
        devices = [BaseDevice]
        for address in self.device.list_i2c_devices():
            self.device.set_i2c_address(address)
            response = self.device.query("I")
            moduletype = response.split(",")[1] 
            name = self.device.query("name,?").split(",")[1]

            devices.append(self.instantiate_specific_sensor_type(address, moduletype, name))
        return devices
    
    def instantiate_specific_sensor_type(self, address: int, moduletype: str, name: str) -> BaseDevice:
        if(moduletype == AtlasDeviceTypes.CO2):
            return EzoCo2(AtlasI2C(address = address, moduletype = moduletype, name = name))
        if(moduletype == AtlasDeviceTypes.DO):
            return EzoDo(AtlasI2C(address = address, moduletype = moduletype, name = name))
        if(moduletype == AtlasDeviceTypes.EC):
            return EzoEc(AtlasI2C(address = address, moduletype = moduletype, name = name))
        if(moduletype == AtlasDeviceTypes.HUM):
            return EzoHum(AtlasI2C(address = address, moduletype = moduletype, name = name))
        if(moduletype == AtlasDeviceTypes.ORP):
            return EzoOrp(AtlasI2C(address = address, moduletype = moduletype, name = name))
        if(moduletype == AtlasDeviceTypes.PH):
            return EzoPh(AtlasI2C(address = address, moduletype = moduletype, name = name))
        if(moduletype == AtlasDeviceTypes.PMP):
            return EzoPmp(AtlasI2C(address = address, moduletype = moduletype, name = name))
        if(moduletype == AtlasDeviceTypes.PRS):
            return EzoPrs(AtlasI2C(address = address, moduletype = moduletype, name = name))
        if(moduletype == AtlasDeviceTypes.RTD):
            return EzoRtd(AtlasI2C(address = address, moduletype = moduletype, name = name))
        
        return BaseDevice(AtlasI2C(address = address, moduletype = moduletype, name = name))
