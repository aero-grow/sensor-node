#!/usr/bin/python

from enum import Enum

# the timeout needed to query readings and calibrations
LONG_TIMEOUT = 1.5
# timeout for regular commands
SHORT_TIMEOUT = .3
# the default bus for I2C on the newer Raspberry Pis, 
# certain older boards use bus 0
DEFAULT_BUS = 1
# the default address for the sensor
DEFAULT_ADDRESS = 98
LONG_TIMEOUT_COMMANDS = ("R", "CAL")
SLEEP_COMMANDS = ("SLEEP", )

class AtlasDeviceTypes(Enum):
    UNDEFINED = ""
    CO2 = "CO2"
    DO = "D.O."
    EC = "EC"
    FLO = "FLO"
    HUM = "HUM"
    O2 = "O2"
    ORP = "ORP"
    PH = "pH"
    PMP = "PMP"
    PRS = "PRS"
    RGB = "RGB"
    RTD = "RTD"

class AtlasResponseCodes(Enum):
    UNDEFINED = ''
    SUCCESS = '1'
    SYNTAX_ERROR = '2'
    STILL_PROCESSING_NOT_READY = '254'
    NO_DATA_TO_SEND = '255'