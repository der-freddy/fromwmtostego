import librosa as lro, matplotlib.pyplot as plt, math,librosa.display, numpy as np, bitarray, datetime, os, scipy as sc
import random as rn
from audio import Audio
from message import Message
from scipy.signal import find_peaks
import bitarray
from embedded import Embedded

path = 'export/44 Pianisten 01-Promenade.wav'
pathtxt = 'export/44 Pianisten 01-Promenade.wav_key.txt'

cs = Embedded(path, None, None)

text_file = open(pathtxt, 'r')

keyseedtxt = text_file.read().split(';')

msglen = 8

keyseed = np.zeros(len(keyseedtxt), dtype=int)



for i in range(0, len(keyseedtxt)):
	keyseed[i] = keyseedtxt[i]


segsize = int(math.floor(cs.size/msglen))
seedlen = 100
sym = math.floor(segsize/seedlen)
hann = np.hanning(seedlen)
keysig = np.zeros(seedlen*sym)




id_p = np.where(keyseed == 1)
pos = id_p[0]*seedlen
id_n = np.where(keyseed == -1)
neg = id_n[0]*seedlen


Id = np.where((keyseed == 1) | (keyseed == -1))


pos = id_p[0]*100
neg = id_n[0]*100


data = cs.y[(pos[0]):(pos[0])+seedlen]*hann

for i in range(1,50):
	data = np.append(data, cs.y[(pos[i]):(pos[i])+seedlen]*hann)

ceps = cs.Ceps(data[:])

plt.plot(ceps[0:50])
plt.show()
