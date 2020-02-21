#standard usb lib and data types
import serial 
import sys
sys.path.append('/home/pringles/comms-python')
from Host import Host

#delay Lib for testing
import time
#NOTE Data packet(Serial)  is in bytes 0xF7, Command,Command Paramter, Checksum, Sum of previous data - 0xF7
#NOTE Alternative DATA packet is ":"Command, Param1,Param2...,ParamN\n. \n marks the end of the data packet. The return data len is unknown but will be null terminated
#NOTE serial library automaically null terminiates strings
#NOTE YostLabs IMU has a default baudrate of 115200

#USB_Device Class Declaratoin
class USB_Device:
	def __init__(self,Port,Baudrate):
		self.IMU = serial.Serial()
		self.IMU.baudrate = Baudrate
		self.IMU.port = Port
		self.IMU.open()
	
	def IMU_CommitSettings(self):
		self.IMU.write(b':225\n')

	def IMU_SetBaud(self,Baud):
		
		self.IMU.write(b':231,9600\n')
		self.IMU.baudrate = Baud

	def IMU_Tare(self):
    	#Tare with current orientation command
	#	self.IMU.open()#Open Port in case it was closed
		self.IMU.write(b':96\n')
	#	self.IMU.close()#Close Port After Operation is done

	def IMU_ReadTare(self):
    	#Read tare command (returned as a rot matrix)
	#	self.IMU.open()#Open Port in case it was closed
		self.IMU.write(b':129\n')
		return self.IMU.readline() #TODO Publish over ZMQ
        	#IMU.close()#Close Port After we are done

	def IMU_Read_EUL(self):
    	#Read Eul command - Tared
	#	IMU.open()#Open Port in case it was closed
		self.IMU.write(b':1\n')
		print(IMU.readline()) #TODO Publish over ZMQ
	#	IMU.close()#Close Port

	def IMU_Read_ROT(self):
	#Read Rot Matrix - Tared
	#	IMU.open()#Open Port in case it was closed
		self.IMU.write(b':2\n')
		print(IMU.readline()) #TODO Publish over ZMQ
	#	IMU.close()#Close Port
"""TEST
IMU = serial.Serial()
IMU.port = '/dev/ttyUSB0'
IMU.baudrate = 115200
msg = ':0\n:'
IMU.open()
IMU.write(b':0\n') #read quart data, response is 16 bytes in non ascii mode, send request may require UTF-8 encoding

x= IMU.readline()#read the data
print(x)

#End TEST"""

class USB_IMU(Host):

	name = 'usb_imu'

	def run(self):
		IMU =  USB_Device('/dev/ttyUSB0',115200)
	#	IMU.IMU_SetBaud(9600)
		node = self.node
		while True:
			IMU.IMU_Tare()
		#	time.sleep(1) #Delay needed bcasue the IMU was getitng overwhelmed
			node.send('IMU_RAW',IMU.IMU_ReadTare())
		    	#IMU.IMU_Read_EUL
			#IMU.IMU_Read_ROT
