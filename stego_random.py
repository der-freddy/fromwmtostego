import librosa as lro, matplotlib.pyplot as plt, math,librosa.display, numpy as np, bitarray, datetime, os, scipy as sc, random
import random as rn
from audio import Audio
from message import Message
from scipy.signal import find_peaks
import bitarray
from embedded import Embedded

file = "44 Pianisten 01-Promenade.wav"

inp = "export"



path = os.path.join(inp, file)
pathtxt = os.path.join(inp, file+"_key.txt")

#path = 'export/44 Pianisten 01-Promenade.wav'
#pathtxt = 'export/44 Pianisten 01-Promenade.wav_key.txt'

cs = Embedded(path, None, None, 100, 8, pathtxt)

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

for j in range(0,50):
	####Randomkey#####
	
	rand_n = np.random.rand(sym)
	
	rand_n[0] = 0
	rand_n[sym-1] = 0
	
	rand_n[np.where(rand_n < 0.5)] = 0
	rand_n[np.where(rand_n >= 0.5)] = 1
	
	keyseed = rand_n
	
	####RandomKey END#####
	
	id_p = np.where(keyseed == 1)
	pos = id_p[0]*seedlen
	#id_n = np.where(keyseed == -1)
	#neg = id_n[0]*seedlen
	
	
	Id = np.where((keyseed == 1))
	
	
	pos = id_p[0]*100
	#neg = id_n[0]*100
	
	
	####Postive 10% Negativ#####
	count_pos = int(pos.size)
	count_neg = int(math.floor(count_pos*0.1))
	
	data = cs.y[(pos[0]):(pos[0])+seedlen]*hann
	
	for i in range(1,int(count_pos)):
		data = np.append(data, cs.y[(pos[i]):(pos[i])+seedlen]*hann)
	
	
	ceps = cs.Ceps(data[:])
	
	plt.plot(ceps[0:50])
	plt.savefig('/media/sf_X_DRIVE/Documents/repros/fromwmtostego/export/doku/randomkey_decoding/'+str(j)+'.png')
	#plt.show()

	plt.close()
