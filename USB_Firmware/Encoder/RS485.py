#Comms Interace for the RS422 Encoder 
#Target Encoder : AMT213A-V
#Bit Time = 104us
	#A. Gamby 1/28/19
#Standard USB Library
import serial

#Open RS485 Adapter Serial Port
Adapter = serial.Serial('/dev/ttyUSB0')
#Set the BaudRate
Adapter.baudrate = 9600

#Send the Read Command to the Encoder
Adapter.write('T'.encode('utf-8'))
#Wait for Encoder Byte Response Response
Adapter.read(2)
