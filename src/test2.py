#!/usr/bin/python

import io
import sys
import fcntl
import time
import copy
import string
import typing
from devices.atlas import constants
from devices.atlas.base_device import BaseDevice
from devices.sensor_manager import SensorManager

def print_devices(devices: typing.List[BaseDevice]):
    for i in devices:
        print(f'Module: {i.moduletype}, Name: {i.name}, Address: {i.address}')

def print_help_text():
    print('''
>> Atlas Scientific I2C sample code
>> Any commands entered are passed to the default target device via I2C except:
  - Help
      brings up this menu
  - List 
      lists the available I2C circuits.
      the --> indicates the target device that will receive individual commands
  - xxx:[command]
      sends the command to the device at I2C address xxx 
      and sets future communications to that address
      Ex: "102:status" will send the command status to address 102
  - all:[command]
      sends the command to all devices
  - Poll[,x.xx]
      command continuously polls all devices
      the optional argument [,x.xx] lets you set a polling time
      where x.xx is greater than the minimum %0.2f second timeout.
      by default it will poll every %0.2f seconds
>> Pressing ctrl-c will stop the polling
    ''' % (constants.LONG_TIMEOUT, constants.LONG_TIMEOUT))

def main():
    sensor_manager = SensorManager()
    real_raw_input = vars(__builtins__).get('raw_input', input)

    while True:
        try:
        
            user_cmd = real_raw_input(">> Enter command: ")
            
            # show all the available devices
            if user_cmd.upper().strip().startswith("LIST"):
                print_devices(sensor_manager.devices)
                
            # print the help text 
            elif user_cmd.upper().startswith("HELP"):
                print_help_text()
                
            # continuous polling command automatically polls the board
            elif user_cmd.upper().strip().startswith("POLL"):
                cmd_list = user_cmd.split(',')
                if len(cmd_list) > 1:
                    delaytime = float(cmd_list[1])
                else:
                    delaytime = device.long_timeout

                # check for polling time being too short, change it to the minimum timeout if too short
                if delaytime < device.long_timeout:
                    print("Polling time is shorter than timeout, setting polling time to %0.2f" % device.long_timeout)
                    delaytime = device.long_timeout
                try:
                    while True:
                        print("-------press ctrl-c to stop the polling")
                        for dev in sensor_manager.devices:
                            dev.write("R")
                        time.sleep(delaytime)
                        for dev in sensor_manager.devices:
                            print(dev.read())
                    
                except KeyboardInterrupt:       # catches the ctrl-c command, which breaks the loop above
                    print("Continuous polling stopped")
                    print_devices(sensor_manager.devices)
                    
            # send a command to all the available devices
            elif user_cmd.upper().strip().startswith("ALL:"):
                cmd_list = user_cmd.split(":")
                for dev in sensor_manager.devices:
                    dev.write(cmd_list[1])
                
                # figure out how long to wait before reading the response
                timeout = sensor_manager.device.get_command_timeout(cmd_list[1].strip())
                # if we dont have a timeout, dont try to read, since it means we issued a sleep command
                if(timeout):
                    time.sleep(timeout)
                    for dev in sensor_manager.devices:
                        print(dev.read())
                    
            # if not a special keyword, see if we change the address, and communicate with that device
            else:
                try:
                    cmd_list = user_cmd.split(":")
                    if(len(cmd_list) > 1):
                        addr = cmd_list[0]
                        
                        # go through the devices to figure out if its available
                        # and swith to it if it is
                        switched = False
                        for i in sensor_manager.devices:
                            if(i.address == int(addr)):
                                device = i
                                switched = True
                        if(switched):
                            print(device.query(cmd_list[1]))
                        else:
                            print("No device found at address " + addr)
                    else:
                        # if no address change, just send the command to the device
                        print(device.query(user_cmd))
                except IOError:
                    print("Query failed \n - Address may be invalid, use list command to see available addresses")

                    
        except:
            pass

if __name__ == '__main__':
    main()
    

