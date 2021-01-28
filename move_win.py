import librosa as lro, matplotlib.pyplot as plt, math,librosa.display, numpy as np, bitarray, datetime, os
import random as rn
from audio import Audio
from message import Message
from scipy.signal import find_peaks
import bitarray
from embedded import Embedded

path = 'export/44 Pianisten 01-Promenade.wav'


cs = Embedded(path, None, None)

win = 100
start = 2400
step = 50
j = 0
#arr = np.empty([100,int(start/step)], dtype=float)
arr = np.empty([int(start/step),win], dtype=float)
print(arr[0,:])

for i in range(start, start+1000, step):
	
	ceps = cs.Ceps(cs.y[i:i+win])
	print(ceps.size)
	arr[j,:] = ceps 
	j = j+1

ip = False

while ip != 'True':
	ip = input('Input: ')
	plt.plot(arr[int(ip),0:44])
	plt.show()

#randomList = []
#
#leng = 100
#han = np.hanning(leng)
#
#for i in range(0, 1000):
#    # any random numbers from 0 to 1000
#	ran = rn.randint(0+i, cs.size-i)
#	randomList.append(ran)
#
#print(randomList)
#
#arr = []
#
#for i in randomList:
#	win = cs.y[i:i+leng]*han
#	arr = np.append(arr, win)
#
#ceps = cs.Ceps(arr[0:])
#
#plt.plot(ceps[0:44])
#plt.show()