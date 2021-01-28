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


####Randomkey#####

rand_n = np.random.rand(sym)

rand_n[0] = 0
rand_n[sym-1] = 0

rand_n[np.where(rand_n < 0.9)] = 0
rand_n[np.where(rand_n >= 0.9)] = 1

#keyseed = rand_n

####RandomKey END#####

id_p = np.where(keyseed == 1)
pos = id_p[0]*seedlen
#id_n = np.where(keyseed == -1)
#neg = id_n[0]*seedlen


Id = np.where((keyseed == 1))


pos = id_p[0]*100
#neg = id_n[0]*100

print(id_p)
print(pos)


####Negativ 10% Postiv#####
#count_neg = int(pos.size)
#count_pos = int(math.floor(count_neg*0.1))
#
#data = cs.y[neg[0]:neg[0]+seedlen]*hann
#for i in range(1, int(count_neg)):
#	data = np.append(data, cs.y[(neg[i]):(neg[i])+seedlen]*hann)
#
#for i in range(0, int(count_neg)):
#	data = np.append(data, cs.y[(pos[i]):(pos[i])+seedlen]*hann)


####Postive 10% Negativ#####
count_pos = int(pos.size)
count_neg = int(math.floor(count_pos*0.1))

data = cs.y[(pos[0]):(pos[0])+seedlen]*hann

for i in range(1,int(count_pos)):
	data = np.append(data, cs.y[(pos[i]):(pos[i])+seedlen]*hann)
#
#for i in range(0, int(count_neg)):
#	data = np.append(data, cs.y[(neg[i]):(neg[i])+seedlen]*hann)



ceps = cs.Ceps(data[:])

plt.plot(ceps[0:50])
plt.show()



#####RANDOM PICKS######
#id_p = np.where(keyseed == 1)
#pos = id_p[0]*seedlen
#id_n = np.where(keyseed == -1)
#neg = id_n[0]*seedlen
#
#picks = random.choice(id_p[0])
#
#print(id_p)
#
#for i in range(1, int(count_pos)):
#	picks = np.append(picks, random.choice(id_p[0]))
#
#
#for i in range(0, int(count_neg)):
#	picks = np.append(picks, random.choice(id_n[0]))
#
#print('picks')
#print(picks)
#
#Id = np.where((keyseed == 1) | (keyseed == -1))