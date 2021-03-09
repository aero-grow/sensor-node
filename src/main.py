#!/usr/bin/env python3
from rak811 import Mode, Rak811
from devices.sensor_manager import SensorManager

lora = Rak811()
lora.hard_reset()
lora.mode = Mode.LoRaWan
lora.band = 'EU868'
lora.set_config(dev_eui='xxxxxxxxxxxxxxxx',
app_eui='xxxxxxxxxxxxxxxx',
app_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
lora.join_otaa()
lora.dr = 5
lora.send('Hello world')
lora.close()

s = SensorManager()
for d in s.devices:
    msg = d.read_value()
    print(f'{d.moduletype}@{d.address} ({d.name})   -> {msg}')