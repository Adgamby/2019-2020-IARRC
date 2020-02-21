# importing Host from comms-python framework
import sys
sys.path.append('~/comms-python')
from Host import Host


# make a class that extends Host
class TestReceiver(Host):
	# override the name attribute (should match this module's name in the configs)    
	name = 'test-receiver'
	# override the run method (treat this as the starting point of your script)     
	def run(self):
		while True:
			msg = self.node.recv_simple('IMU_RAW')
			print("Message received:")
			print(msg)

