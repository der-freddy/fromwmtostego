
####################################################
#EMBEDDED-KLASSE ZUR RUEGEWINNUNG VON INFORMATIONEN#
####################################################

import librosa as lro, librosa.display, copy, numpy as np, math, matplotlib.pyplot as plt, scipy as sc, math, os
from message import Message
from scipy.signal import find_peaks
from scipy import signal
import peakutils
from audio import Audio

#Konstrutor
class Embedded(object):
	"""docstring for Embedd"""
	def __init__(self, path,os, du, multi, msg_len, keypath):
		if type(path) == str:
			self.y, self.sr = lro.load(path, mono=True, sr=44100,offset=os, duration=du)
			self.path = path
		else:
			self.y = path
			self.sr = sr
		self.size = self.y.size
		self.hann = np.hanning(multi)
		self.msg_len = msg_len
		self.segsize = int(math.floor(self.size/msg_len))
		self.sym = math.floor(self.segsize/multi)
		self.multi = multi
		self.keypath = keypath
		self.position = self.buildKey()
		self.ceps = self.keyCeps()
		self.peaks = self.Peaks()
		self.c1, self.c2 = self.Can()
		self.msg = self.Decode()


	def keyCeps(self):

		size = (self.position.shape[1]*self.multi)
		data = np.zeros([self.msg_len, size], dtype=float)

		n=0

		for i in self.position:
			row = np.zeros(0)
			for j in i:
				row = np.append(row, self.y[j:j+self.multi]*self.hann)
			data[n] = row
			n = n+1

		for i in range(0, self.msg_len):
			data[i] = self.Ceps(data[i])

		return data

	def buildKey(self):
		text_file = open(self.keypath, 'r')
		keyseedtxt = text_file.read().split(';')
		keyseed = np.zeros(len(keyseedtxt), dtype=int)

		for i in range(0, len(keyseedtxt)):
			keyseed[i] = keyseedtxt[i]

		id_p = np.where(keyseed == 1)
		pos = id_p[0]*self.multi
		pos = id_p[0]
		

		all_pos = (pos*self.multi)+self.segsize*0

		for i in range(1, self.msg_len):
			all_pos = np.vstack((all_pos, (pos*self.multi)+self.segsize*i))

		return all_pos
	#Cepstrum with windowing
	def Ceps(self, array):
		hann = np.hanning(array.size)
		x = np.fft.fft(array*hann)
		x = np.log(x)
		ceps = np.abs(np.fft.ifft(x))

		return ceps


	def Peaks(self):
		peaks = np.zeros(0, dtype=int)


		for row in self.ceps:
			peak, _ = find_peaks(row[10:44])

			ceps_mean = np.mean(row[peak+10])

			peak, _ = find_peaks(row[10:44], height=ceps_mean)

			peak =peak+10

			max_v = np.argmax(row[peak])

			peaks = np.append(peaks, int(peak[max_v]))
			
		return peaks



	#def Peaks(self):
	#	
	#	peaks = np.zeros(0)
	#	for row in self.ceps:
	#		peak, _ = find_peaks(row[0:44])
	#		ceps_mean = np.mean(row[peak])
	#		peak, _ = find_peaks(row[0:44], height=ceps_mean)
	#		#print(peak)
	#		max_v = np.argmax(row[peak])
	#		#print(peak[max_v])
	#		peaks = np.append(peaks, peak[max_v])
	#	return peaks

	def Can(self):

		can1 = int(self.peaks[0])
		can2 = 0
		b = 0

		while b == 0:
			for i in self.peaks:
				if i != can1:
					b = 1
					can2 = int(i)

		return can1, can2
	def Decode(self):
		msg = np.zeros(0)

		for i in self.peaks:
			if i == self.c1:
				msg = np.append(msg, int(0))
			elif i == self.c2:
				msg = np.append(msg, int(1))

		return msg