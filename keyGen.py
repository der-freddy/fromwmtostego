import copy, numpy as np, math, matplotlib.pyplot as plt, scipy as sc, math, soundfile as sf, random as rn
##########################################################
#AUDIO-KLASSE ZUR ERSTELLUNG VON SIGNAL MIT WASSERZEICHEN#
##########################################################

#Konstrutor
class Keygen(object):
	"""docstring for Audio"""
	def __init__(self, siglen, msglen):
		
		self.size = int(math.floor(siglen/msglen))
		self.msgl = msglen
		self.siglen = siglen
		self.seedlen = 100
		self.sym = math.floor(self.size/self.seedlen)
		print(self.sym)
		
		#self.length = math.floor(self.size/self.sym)
		self.sig, self.oe, self.fil = self.buildKey()


	def buildKey(self):
		rand_n = np.random.rand(self.sym)

		rand_n[0] = 0
		rand_n[self.sym-1] = 0

		rand_n[np.where(rand_n < 0.5)] = 0
		#rand_n[np.where(np.logical_and(rand_n>=0.8, rand_n<0.9))] = -1
		rand_n[np.where(rand_n >= 0.5)] = 1

		sig = np.zeros(self.seedlen*self.sym)

		id_p = np.where(rand_n == 1)
		id_n = np.where(rand_n == -1)

		for i in id_p[0]:
			temp = int(i*self.seedlen)
			sig[temp:temp+self.seedlen] = 1

		#for i in id_n[0]:
		#	temp = int(i*self.seedlen)
		#	sig[temp:temp+self.seedlen] = -1

		h = sc.signal.get_window('triang', 50)
		fil = sc.signal.convolve(sig, h/h.sum())


		diff = self.size - (fil.size)
		
		if diff > 0:
			a = np.zeros(diff)
			fil = np.append(fil, a)
		else:
			fil = fil[0:self.size]
		



		diff = self.size - (sig.size)
		
		if diff > 0:
			a = np.zeros(diff)
			sig = np.append(sig, a)
		else: 
			sig = sig[0:self.size]


		s = sig
		f = fil

		for i in range(0, self.msgl-1):
			s = np.append(s, sig)
			f = np.append(f, fil)

		self.size = len(s)
		print('sig')
		print(sig.size)
		print(fil.size)

		diff = (self.siglen) - self.size

		print(diff)

		if diff > 0:
			a = np.zeros(diff)
			s = np.append(s, a)
			f = np.append(f, a)




		return s, rand_n, f