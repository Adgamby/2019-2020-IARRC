#standard usb lib and data types
import serial
#import numpy

#TODO serial port - currently /dev/ttyUSB0
IMU = serial.Serial('/dev/ttyUSB0')
#Default BaudRate of the sensor is 115200
IMU.baudrate = 115200

#NOTE Data packet(Serial)  is in bytes 0xF7, Command,Command Paramter, Checksum, Sum of previous data - 0xF7
#NOTE Alternative DATA packet is ":", Command, Param1,Param2...,ParamN\n. \n marks the end of the data packet. The return data len is unknown but will be null terminated
#NOTE serial library automaically null terminiates strings

"""TEST

msg = ':0\n:'
IMU.write(b':0\n') #read quart data, response is 16 bytes in non ascii mode, send request may require UTF-8 encoding

x= IMU.readline()#read the data
print(x)

End TEST"""

#TODO Set filter paramters

#Tare with current orientation command
IMU.write(b':96\n')
#Read tare command 

#TODO Read Euler Angles & Rot Matrix

#Read Eul command - Tared
IMU.write(b':1\n')
print(IMU.readline())

#Read Rot Matrix - Tared
IMU.write(b':2\n')
print(IMU.readline())
