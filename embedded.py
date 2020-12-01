
####################################################
#EMBEDDED-KLASSE ZUR RUEGEWINNUNG VON INFORMATIONEN#
####################################################

import librosa as lro, librosa.display, copy, numpy as np, math, matplotlib.pyplot as plt, scipy as sc, math
from message import Message
from scipy.signal import find_peaks
from scipy import signal
import peakutils
from audio import Audio

#Konstrutor
class Embedded(object):
	"""docstring for Embedd"""
	def __init__(self, path,os, du):
		if type(path) == str:
			self.y, self.sr = lro.load(path, mono=True, sr=44100,offset=os, duration=du)
			self.path = path
		else:
			self.y = path
			self.sr = sr
		self.size = self.y.size
		self.ceps = self.hanniPC(self.y)
		self.can = self.Candidates()
		self.seg_size, self.msg_len = self.movWin()

	#Berechnung Auto-Cepstrum ohne Fensterung
	def getAC(self, data):
		spec = np.fft.fft(data)
		spec = np.abs(np.log(spec))**2
		ceps = np.abs(np.fft.ifft(spec))

		return ceps
	#Copy Objekt
	def copy(self):
		copy = Embedded(librosa.util.example_audio_file(), 0, 10)
		copy.y = self.y
		copy.sr = self.sr
		copy.size = copy.y.size
		copy.candidates = self.candidates
		copy.ceps = copy.CepsSeg(copy.y)

		return copy		

	#Cepstrum mit Fenster
	def Ceps(self, array):
		hann = np.hanning(array.size)
		x = np.fft.fft(array*hann)
		x = np.log(x)
		ceps = np.abs(np.fft.ifft(x))

		return ceps
	#Berechnung Verzoegerung-Kandidaten
	def Candidates(self):
		ceps_mean = np.mean(self.ceps[8:44])
		peaks, pros = find_peaks(self.ceps[0:45], distance=3, width=0.9, height=ceps_mean)
		clipped_data = peaks[(peaks > 10)]
		sort = np.sort(self.ceps[clipped_data])
		sort = sort[::-1]
		sort = sort[:2]

		result = np.where(self.ceps == sort[0])
		result = np.append(result, np.where(self.ceps == sort[1]))
		return result

	#Moving Window zur Berechnung der Segmentgroesse
	def movWin(self):
		w = 2000
		s = 0

		seg_ceps = self.hanniPC(self.y[s:w])

		null = seg_ceps[self.can[0]]
		one = seg_ceps[self.can[1]]

		while null > one:
			step = 200
			seg_ceps = self.hanniPC(self.y[s:w])
			null = seg_ceps[self.can[0]]
			one = seg_ceps[self.can[1]]

			s = s+step
			w = w+step
		size = (s+w)/2
		msg_len = round(float(float(self.y.size)/float(size)))-2
		print(msg_len)
		if msg_len%8:
			r = msg_len%8
			c = np.abs(r-8)
			msg_len = msg_len+c
		msg_len = msg_len+2

		seg_size = int(self.y.size/msg_len)
		

		print(seg_size)
		print(msg_len)
		return seg_size, msg_len

	#Rueckgewinnung der Nachricht
	def decode(self):
		msg = Message('')
		for i in range(2, int(self.msg_len)):

			m = self.seg_size*i
			ceps = self.hanniPC(self.y[m:m+self.seg_size])

			if ceps[self.can[0]] > ceps[self.can[1]]:
				msg.mb.append(False)
				
			elif ceps[self.can[0]] < ceps[self.can[1]]:
				msg.mb.append(True)
		#print(self.size)
		#print(self.seg_size)
		#print(self.msg_len)
		#print(msg.mb)
		msg.bitToString()
		
		print(msg.msg)


	#Power-Cepstrum mit Fensterung
	def hanniPC(self, array):
		hann = np.hanning(array.size)
		x = np.fft.fft(array*hann)
		x = (x)**2
		x = (np.log(x))
		ceps = np.abs(np.fft.ifft(x))**2
		return ceps

	#Auto-Cepstrum mit Fensterung
	def hanniAC(self, array):
		hann = np.hanning(array.size)
		ceps = np.abs(np.fft.ifft(np.log((np.fft.fft(array*hann)))**2))
		return ceps

	#Cepstrum-Ueberlagerung
	def combinedHanni(self):
		n = 8
		size =  int(math.floor(self.size/n))*n
		new = self.y[:size]
		segments =   np.reshape(new, (n, new.size/n))
		ceps = np.zeros(new.size/n)

		for i in range(0,n):
			ceps = ceps + self.hanniPC(segments[i])

		return ceps

	#Berechnung eines Selbstkorresponierendes echo
	def selfEcho(self, delay, m, n):
		copy = self.copy()
		
		A = np.zeros((n-m)+delay)
		B = self.y[m:n]

		for i in range(0, B.size):
			A[i+delay] = B[i]

		for i in range(0, B.size):
			A[i] = B[i]+A[i]

		copy.y = A
		copy.size = copy.y.size

		return copy

	#Auto-Cepstrum mit 
	def ACSeg(self, array):
		x = (np.fft.fft(array))
		x = np.abs(np.log(x))**2
		AC = np.abs(np.fft.ifft(x))
		return AC

	#Berchnung Segmentgroesse (alt)
	def segSize(self):

		m = 0
		n = self.size
		ws = 2000
		steps = 500
		can0 = self.candidates[0]
		can1 = self.candidates[1]
		check = False

		while check == False:
			hannipc = self.hanniPC(self.y[m:m+1000])

			value0 = hannipc[can0]
			value1 = hannipc[can1]

			if value0 > value1:
				check = False
			else:
				check = True
			size = m

			m = m+500

		segs = int(math.floor(self.size/size))

		return int(math.floor(self.size/segs)), segs


#	def decoding(self):
#		
#		if self.candidates.size != 2:
#			print('Kein Decoding')
#		else:
#
#			size, segs = self.segSize()
#			msg = Message('')
#			
#			for i in range(0, size*segs, size):
#				
#				print(i)
#				print(i+size)
#				hanni = self.hanniPC(self.y[i:i+size])
#				if hanni[self.candidates[0]] > hanni[self.candidates[1]]:
#					msg.mb.append(False)
#				else:
#					msg.mb.append(True)
#			msg.bitToString()
#			print(msg.msg)


#	def getCandidate(self):
#
#		can = self.getPeaks(self.ceps, False)
#		for i in can[2:]:
#			if i%can[0] == 0:
#				can = np.delete(can, np.where(can == i))
#			if i%can[1] == 0:
#				can = np.delete(can, np.where(can == i))
#			if i%(can[0]+can[1]) == 0:
#				can = np.delete(can, np.where(can == i))
#
#
#		while can.size > 2:
#			value = min(self.ceps[can])
#			can = np.delete(can, np.where(self.ceps[can] == value))
#
#		check_peaks = self.checkCandidates()
#
#		for i in can:
#			if i not in check_peaks:
#				can = np.delete(can, np.where(can == i))
#			else:
#				break
#
#		
#		if can.size == 0:
#			print('Keine Kandidaten gefunden, keine Entschluesselung')
#
#		elif can.size == 1:
#			print('Einen Kandidaten gefunden, keine Entschluesselung')
#
#
#
#		return can


#	def checkCandidates(self):
#		n = 8
#		size = int(math.floor(self.size/n))*n
#		new = self.y[:size]
#
#		segments = np.reshape(new, (n, new.size/n))
#		ceps = np.zeros(new.size/n)
#
#		for i in range(0,n):
#			ceps = ceps + self.hanniPC(segments[i])
#
#		ceps_mean = np.mean(ceps[8:44])
#
#		peaks, _ = find_peaks(ceps[8:44], distance=5, height=ceps_mean)
#		peaks = peaks[(8 < peaks)]
#
#		peaks = peaks + 8
#
#		for i in peaks[2:]:
#			if i%peaks[0] == 0:
#				peaks = np.delete(peaks, np.where(peaks == i))
#			if i%peaks[1] == 0:
#				peaks = np.delete(peaks, np.where(peaks == i))
#			if i%(peaks[0]+peaks[1]) == 0:
#				peaks = np.delete(peaks, np.where(peaks == i))
#
#
#		return peaks

#	def getPeaks(self, ceps, mean):
#
#		if mean:
#			#mean wurde entfernt
#			peaks, _ = find_peaks(ceps[0:44], distance=5)
#			peaks = peaks[(8 < peaks)]
#		else:
#			ceps_mean = np.mean(ceps[8:44])
#			peaks, _ = find_peaks(ceps[0:44], distance=5, height=ceps_mean)
#			peaks = peaks[(8 < peaks)]
#
#
#		return peaks

#	def SegPeaks(self, ceps, max):
#		peaks = find_peaks(ceps[0:45], threshold=0.01)[0]
#		return peaks