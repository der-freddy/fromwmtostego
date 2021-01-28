

##########################################################
#AUDIO-KLASSE ZUR ERSTELLUNG VON SIGNAL MIT WASSERZEICHEN#
##########################################################


import librosa as lro, librosa.display, copy, numpy as np, math, matplotlib.pyplot as plt, scipy as sc, math, soundfile as sf

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
		self.delay0 = 15
		self.delay1 = 20
		self.dte = list(range(0, 44, 1))
		for i in range(0, 44):
			self.dte[i] =  math.exp(-0.5*(float(i)/8))
		self.ratio0 = self.dte[self.delay0]
		self.ratio1 = self.dte[self.delay1]

		self.ratio0 = 0.5
		self.ratio1 = 0.5
	#Copy Objekt
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

	#Cepstrum fuer ein variables Segment
	def CSeg(self, m, n):
		x = (np.fft.fft(self.y[m:n]))
		x = np.abs(np.log(x))
		ceps = np.abs(np.fft.ifft(x))
		return ceps 

	#Komplexes Cepstrum mit Fensterung
	def LogSpec(self, array):
		hann = np.hanning(array.size)
		x = np.fft.fft(array*hann)
		x = np.log(x)
		ceps = x

		return ceps

	def Ceps(self, array):
		hann = np.hanning(array.size)
		x = np.fft.fft(array*hann)
		x = np.log(x)
		ceps = np.abs(np.fft.ifft(x))

		return ceps
	#Power-Cepstrum mit Fesnterung
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

	# Darstellung von Auto-Korrelation
	def plotAc(self):
		ac = np.correlate(self.ceps, self.ceps, mode='full')
		ac = ac[:ac.size//2]
		plt.plot(ac)
		plt.xlabel('Quefrency (frames)')
		plt.ylabel('Amplitude')
		plt.title('Autocepstrum')
		plt.show()

	#Darstelung Komplex-Cepstrum
	def plotCeps(self):
		plt.plot(self.ceps)
		plt.xlabel('Quefrency (frames)')
		plt.ylabel('Absolute Magnitude')
		plt.title('Cepstrum')
		plt.show()

	#Darstellung Spektrum
	def plotSpec(self):
		absfft = np.abs(librosa.stft(self.y))
		librosa.display.specshow(librosa.amplitude_to_db(absfft,ref=np.max),y_axis='log', x_axis='time')
		plt.title('Power spectrogram')
		plt.colorbar(format='%+2.0f dB')
		plt.tight_layout()
		plt.show()

	#Mischung des OE-Signals und Echo-Signal
	def simpleMix(self, echo):
		stego = self.copy()
		for i in range(0, stego.size):
			#stego.y[i] = (ratio*stego.y[i])+((1-ratio)*echo.y[i])
			stego.y[i] = (stego.y[i]+echo.y[i])

		return stego

	#Erstellung Negativecho
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

	#Erstellung Doppel-Echo
	def buildDecho(self, delay, ratio):
		echo = self.copy()
		y = np.zeros(self.size)

		y[:self.size-delay] += self.y[delay:]*-(ratio)
		y[delay:] += self.y[:self.size-delay]*ratio

		echo.y = y
		echo.size = self.size
		return echo

	#Erstellung des Echos mit Kernel
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

	#Crossfader-methode
	def crossfader(self, m,echo):
			
		#self.y[m] = self.y[m]*0.5 + echo.y[m]*0.5
		for i in range(0,10):
			f = 0.1
			self.y[m-i]=(self.y[m-i]*f*i)+(echo.y[m-i]*f*(10-i))

	#Daempfung des OE-Signals
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

	#Erstellung kompletten Echo-Signals
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

		#Sinus-Verknuepfung
		#print('Mit Sinus')
		#echo.y = echo.y*S

		return echo
	#Speicher Traegersignal
	def write(self):
		path = self.export
		#lro.output.write_wav(path, self.y, self.getSampling())
		print(path)
		sf.write(path, self.y, self.getSampling())

	# Einbettung
	def encode(self, msg, export_path):

		if msg.msg == '':
			stego = self.copy()
			print('No Message embedded')			
		else:
			echo0 = self.buildEcho(self.delay0, self.ratio0)
			echo1 = self.buildEcho(self.delay1, self.ratio1)
			#EchoSig = self.EchoSignal(echo0, echo1, msg)
			EchoSig, key = self.EchoSignalKey(echo0, echo1, msg)

			#self.oe_decay(msg)

			stego = self.simpleMix(EchoSig)
			#print(stego.y[0:20])
			print('Message embedded')
		
		print(msg.mb)
		stego.write()
		#echo0.write('/home/fsukop/Documents/repos/thesis/echo_hiding/audio/decho/44 Pianisten 01-Promenade_echo0.wav')
		return stego, EchoSig, echo0, echo1, key

		#return stego


	def genKeySignal(self, msg):
		seg = msg.getMbLen()
		seg_size = int(math.floor((self.getSize())/(seg)))
		end = 0
		

		key = np.zeros(seg_size)
		#print(math.floor(seg_size/2))
		#print(math.floor(seg_size/2)+10)

		print('begin')
		for i in range(1, 10):
			key[math.floor(seg_size/2)+i] = i/10
			#print(key[math.floor(seg_size/2)+i])
			#print(math.floor(seg_size/2)+i)
			end = math.floor(seg_size/2)+i


		
		print('1')		
		for i in range(1, 100):
			key[end+i] = 1
			
		end = end+99

		print('end')

		for i in range(1, 10):
			key[end+i] = 1-(i/10)
		
		end = end+10

		#for i in range(math.floor(seg_size/2), math.floor(seg_size/2)+200):
		#	print(i)
		#	print(key[i])
		copy = key
		for i in range(0, msg.getMbLen()-1):
			key = np.append(key, copy)

		return key


	def EchoSignalKey(self, echo0, echo1, msg):

		key = self.genKeySignal(msg)

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

		print(echo.y.size)
		print(key.size)

		echo.y = echo.y*key

		return echo, key