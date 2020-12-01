

##########################################################
#AUDIO-CLASS FOR EMBEDDING PROCESS#
##########################################################


import librosa as lro, librosa.display, copy, numpy as np, math, matplotlib.pyplot as plt, scipy as sc, math

#Konstrutor
class Audio(object):
	"""docstring for Audio"""
	def __init__(self, path, export,name, os, du):
		self.path = path
		self.export = export
		self.y, self.sr = lro.load(path, mono=True, sr=44100, offset=os, duration=du)
		self.size = self.y.size
		self.os = os
		self.du = du
		self.name = name
		self.delay0 = 20
		self.delay1 = 25
		self.dte = list(range(0, 44, 1))
		for i in range(0, 44):
			self.dte[i] =  math.exp(-0.5*(float(i)/8))
		#self.ratio0 = self.dte[self.delay0]
		#self.ratio1 = self.dte[self.delay1]

		self.ratio0 = 1
		self.ratio1 = 1
	#Copy Object
	def copy(self):
		return Audio(self.path, self.export,self.name, self.os, self.du)

	#Get Audiosignal
	def getWv(self):
		return self.y
	#Get Samplerate
	def getSampling(self):
		return self.sr
	#Get Array-Size
	def getSize(self):
		return self.size
	#Get Audioname
	def setName(self, name):
		self.name = name

	#Ceptrum of a segment (m=beginn, n=end, in sample points)
	def CSeg(self, m, n):
		x = (np.fft.fft(self.y[m:n]))
		x = np.abs(np.log(x))
		ceps = np.abs(np.fft.ifft(x))
		return ceps 

	#Complex Ceptrum with windowing
	def Ceps(self, array):
		hann = np.hanning(array.size)
		x = np.fft.fft(array*hann)
		x = np.log(x)
		ceps = np.abs(np.fft.ifft(x))

		return ceps
	#Power Cepstrum with windowing
	def hanniPC(self, array):
		hann = np.hanning(array.size)
		x = np.fft.fft(array*hann)
		x = (x)**2
		x = (np.log(x))
		ceps = np.abs(np.fft.ifft(x))**2
		return ceps

	#Autocepstrum with windowing
	def hanniAC(self, array):
		hann = np.hanning(array.size)
		ceps = np.abs(np.fft.ifft(np.log((np.fft.fft(array*hann)))**2))
		return ceps

	# Plot Auto-Correlation
	def plotAc(self):
		ac = np.correlate(self.ceps, self.ceps, mode='full')
		ac = ac[:ac.size//2]
		plt.plot(ac)
		plt.xlabel('Quefrency (frames)')
		plt.ylabel('Amplitude')
		plt.title('Autocepstrum')
		plt.show()

	# Plot Cepstrum
	def plotCeps(self):
		plt.plot(self.ceps)
		plt.xlabel('Quefrency (frames)')
		plt.ylabel('Absolute Magnitude')
		plt.title('Cepstrum')
		plt.show()

	#Plot Spectrum
	def plotSpec(self):
		absfft = np.abs(librosa.stft(self.y))
		librosa.display.specshow(librosa.amplitude_to_db(absfft,ref=np.max),y_axis='log', x_axis='time')
		plt.title('Power spectrogram')
		plt.colorbar(format='%+2.0f dB')
		plt.tight_layout()
		plt.show()

	#Generate Echo Signal
	def simpleMix(self, echo):
		stego = self.copy()
		for i in range(0, stego.size):
			#stego.y[i] = (ratio*stego.y[i])+((1-ratio)*echo.y[i])
			stego.y[i] = (stego.y[i]+echo.y[i])

		return stego

	#Negetiv Echo
	def buildNecho(self, delay, ratio):
		echo = self.copy()
		y = echo.y
		delta = delay # delta in Frames		
		CopyArray = np.copy(y)
		
		for i in range(0, echo.size):
			if i<delta:
				echo.y[i] = 0
			else:
				echo.y[i] = CopyArray[i-delta]*ratio

		return echo

	#Back-Forward-Echo
	def buildDecho(self, delay, ratio):
		echo = self.copy()
		y = np.zeros(self.size)

		#y[:self.size-delay] += self.y[delay:]*-(ratio)
		y[delay:] += self.y[:self.size-delay]*ratio

		echo.y = y
		echo.size = self.size
		return echo

	#Echo with defined kernels
	def buildEcho(self, delay, ratio):
		echo = self.copy()
		y = echo.y
		delta = delay # delta in Frames		
		CopyArray = np.copy(y)
		
		for i in range(0, echo.size):
			if i<delta:
				echo.y[i] = 0
			else:
				echo.y[i] = CopyArray[i-delta]*ratio

		return echo

	#Crossfader method (alternative mixer signals)
	def crossfader(self, m,echo):
			
		#self.y[m] = self.y[m]*0.5 + echo.y[m]*0.5
		for i in range(0,10):
			f = 0.1
			self.y[m-i]=(self.y[m-i]*f*i)+(echo.y[m-i]*f*(10-i))

	#dampling oe-signal
	def oe_decay(self, msg):
		oe_copy = self.copy()
		seg = msg.getMbLen()
		seg_size = int(math.floor((oe_copy.getSize())/seg))
		m = 0
		n = seg_size

		for i in range(0, msg.getMbLen()):
			if msg.mb[i]:
				self.y[m:n] = self.y[m:n]*(1-self.ratio1)
			else:
				self.y[m:n] = self.y[m:n]*(1-self.ratio0)

			m += seg_size+1
			n = (m+seg_size)

		return oe_copy

	#Build echo signal
	def EchoSignal(self, echo0, echo1, msg):

		t = np.linspace(0, 2*np.pi, self.size, endpoint=True)
		f = 10 #Frequenz in Hz
		A = 1.0 #Amplitude
		S = A * np.sin(np.pi*f*t) #Signal

		echo = self.copy()
		seg = msg.getMbLen()
		seg_size = int(math.floor((echo.getSize())/seg))
		m = 0
		n = seg_size

		for i in range(0, msg.getMbLen()):

			if msg.mb[i]:
				print(msg.mb[i])
				echo.y[m:n] = echo1.y[m:n]
				if m != 0:
					echo.crossfader(m-1, echo1)
			else:
				print(msg.mb[i])

				echo.y[m:n] = echo0.y[m:n]
				if m != 0:
					echo.crossfader(m-1, echo0)
			m += seg_size+1
			n = (m+seg_size)

		echo.y = echo.y

		#Sine link
		#echo.y = echo.y*S

		return echo
	#write carrier signal
	def write(self):
		path = self.export+self.name
		lro.output.write_wav(path, self.y, self.getSampling())

	# Embedding
	def encode(self, msg, export_path):

		if msg.msg == '':
			stego = self.copy()
			print('No Message embedded')			
		else:
			echo0 = self.buildEcho(self.delay0, self.ratio0)
			echo1 = self.buildEcho(self.delay1, self.ratio1)
			EchoSig = self.EchoSignal(echo0, echo1, msg)

			#self.oe_decay(msg)

			stego = self.simpleMix(EchoSig)
			#print(stego.y[0:20])
			print('Message embedded')
		print(msg.mb)
		stego.write()
		#echo0.write('/home/fsukop/Documents/repos/thesis/echo_hiding/audio/decho/44 Pianisten 01-Promenade_echo0.wav')
		#return stego, EchoSig,echo0, echo1

		#return stego
