'''
Created on Dec 8, 2016
 
@author: jdevenis
'''
# Website where I found the cranking curve for a car. 
# http://www.dtec.net.au/Ignition%20Coil%20Dwell%20Calibration.htm
 
# Based on Oscilloscope readings it takes ~128.0 - 148.0 ms for the power supply to drop the voltage to 8v. 
#                                         ~190 ms at 6.5v
# Based on Oscilloscope readings it takes ~ 1.196 seconds for the power supply to go from 12.7v - 8v - 12.7v
#                                         ~ 1.254 seconds 12.7v - 6.5v - 12.7v
 
import serial
 
# #Change COM port here
COM_port = 'COM6'
 
# Send data to the power supply
def setValue(Flag,Value=''):
    # Open serial port and send EDI command
    with serial.Serial(COM_port, 9600, timeout=1) as ser:
        command = Flag+str(Value)+'\r'
        ser.write(command.encode())
        return str(ser.readline())
 
# Read current and voltage 
def read_current_and_voltage():
    raw_value = setValue('GETD')
    voltage = str(raw_value[2:4]) + '.' + str(raw_value[4:6])
    current = str(raw_value[6:8]) + '.' + str(raw_value[8:10])
    return [voltage, current]
 
setValue('VOLT','127')
setValue('VOLT','067')
setValue('VOLT','127')
