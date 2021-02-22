import librosa as lro, matplotlib.pyplot as plt, math,librosa.display, numpy as np, bitarray, datetime, os, scipy as sc, random
import random as rn
from audio import Audio
from message import Message
from scipy.signal import find_peaks
import bitarray
from embedded import Embedded
from scipy.signal import find_peaks

file = "44 Pianisten 01-Promenade.wav"

inp = "export"

path = os.path.join(inp, file)
pathtxt = os.path.join(inp, file+"_key.txt")

#path = 'export/44 Pianisten 01-Promenade.wav'
#pathtxt = 'export/44 Pianisten 01-Promenade.wav_key.txt'

cs = Embedded(path, None, None, 100, 8, pathtxt)

#print(cs.msg)



i = 0

peaks = np.zeros(0)


for row in cs.ceps:
	
	peak, _ = find_peaks(row[10:44])

	ceps_mean = np.mean(row[peak+10])


	peak, prob = find_peaks(row[10:44], height=ceps_mean)

	print(peak)

	peak = peak + 10

	max_v = np.argmax(row[peak])

	print(peak)

	print(max_v)

	peaks = np.append(peaks, peak[max_v])

	plt.plot(row[10:44])
#	plt.show()


print(peaks)

print(cs.msg)