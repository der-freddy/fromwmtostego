import copy, math
import numpy as np
from bitarray import bitarray


class Message(object):
	"""docstring for Message"""
	def __init__(self, bitstream, d0, d1):
		#for human readable strings
		#self.msg = msg
		self.mb = bitarray(bitstream)
		self.len = len(self.mb)
		self.delays = np.empty([3, self.len])
		self.delay0 = d0
		self.delay1 = d1
		self.dte = list(range(0, 44, 1))
		for i in range(0, 44):
			self.dte[i] =  math.exp(-0.5*(float(i)/8))
		self.ratio0 = self.dte[d0]
		self.ratio1 = self.dte[d1]
		point = 0

		for i in range(0, self.len):
			if self.mb[i]:
				self.delays[0, i] = 1
				self.delays[1, i] = d1
				self.delays[2, i] = self.ratio1
			else:
				self.delays[0, i] = 0
				self.delays[1, i] = d0
				self.delays[2, i] = self.ratio0

