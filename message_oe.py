import bitarray, copy
import numpy as np

#Konstruktor
class Message(object):
	"""docstring for Message"""
	def __init__(self, msg):
		self.msg = msg
		self.mb = bitarray.bitarray()
		#SyncBits
		self.mb.append(False)
		self.mb.append(True)
		if msg:
			self.mb.append(self.mb.frombytes(msg.encode('utf-8')))
		#print(self.mb)
		#self.mb.frombytes(msg.encode('utf-8'))
		self.msg_len = len(msg)
		self.mb_len = (self.msg_len*8)+2
	#Get message string
	def getMsg(self):
		return self.msg
	#Get message in bits
	def getMb(self):
		return self.mb
	#Get message length
	def getMsgLen(self):
		return self.msg_len
	#get bit length
	def getMbLen(self):
		return self.mb_len
	#Set message bits
	def setMB(self, mb):
		self.mb = mb
		self.bitToString()
	#convert bit to string
	def bitToString(self):
		#self.msg = self.mb[2:].tostring()
		self.msg = bitarray.bitarray(self.mb[2:]).tobytes().decode('utf-8')
		self.msg_len = len(self.msg)
		self.mb_len = self.msg_len*8+2

	def constr(self, array):
		mb = bitarray.bitarray()
		mb.extend(array)
		self.mb = mb
		self.bitToString()

	#check methode (not used)
	def checkBits(self):
		print(self.mb)
		a = np.fromstring(self.mb.unpack(), dtype=bool)
		print(a)

		array = copy.copy(a.reshape(a.size/2, 2))

		check = np.empty(array.size/2, dtype=int)
		check[:] = 2
		print(check)
		for i in range(0, array.size/2):
			if array[i][0] == array[i][1]:
				check = array[i][0]

		print(check)
		if 2 in check:
			return False
		else:
			self.constr(check)
			return True