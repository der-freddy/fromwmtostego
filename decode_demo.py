import librosa as lro, matplotlib.pyplot as plt, math,librosa.display, numpy as np, bitarray, datetime, os
import random as rn
from audio import Audio
from message import Message
from scipy.signal import find_peaks
import bitarray
from embedded import Embedded

path = '/media/sf_X_DRIVE/Documents/repros/fromwmtostego/export/doku/decay/1_01/'

fig, axs = plt.subplots(3)



file = '44 Pianisten 01-Promenade.wav'
inp = inp = os.path.join(path, file)
pathtxt = os.path.join(path+"txt/", file+"_key.txt")
cs0 = Embedded(inp, None, None, 100, 8, pathtxt)

axs[0].plot(cs0.Ceps(cs0.y)[0:44], label='Echo Signal', color='red')
axs[0].set_title(file)
axs[0].set( ylabel='Magnitude')
axs[0].set_ylim(-0.2, 0.5)

file = '44 Pianisten 03-Promenade 2.wav'
inp = inp = os.path.join(path, file)
pathtxt = os.path.join(path+"txt/", file+"_key.txt")
cs1 = Embedded(inp, None, None, 100, 8, pathtxt)


axs[1].plot(cs1.Ceps(cs1.y)[0:44], label='Echo Signal', color='orange')
axs[1].set_title(file)
axs[1].set( ylabel='Magnitude')
axs[1].set_ylim(-0.2, 0.5)
file = 'Sa Chen 1. Promenade.wav'
inp = inp = os.path.join(path, file)
pathtxt = os.path.join(path+"txt/", file+"_key.txt")
cs2 = Embedded(inp, None, None, 100, 8, pathtxt)

axs[2].plot(cs2.Ceps(cs2.y)[0:44], label='Echo Signal', color='blue')
axs[2].set_title(file)
axs[2].set_ylim(-0.2, 0.5)
axs[2].set(xlabel='Frames')
axs[2].set( ylabel='Magnitude')
plt.show()




#cs = Embedded(path, None, None)
#
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
#
#for file in os.listdir(path):
#	print(file)
#	cs = Embedded(path+file, None, None)
#	
#	cs.decode()


########################
#CEPSTUM/ AUTO-CEPSTRUM#
########################
#path = 'export/44 Pianisten 01-Promenade.wav'
#path2 = 'export/44 Pianisten 01-Promenade_20_25.wav'
#
#cs = Embedded(path, None, None)
#cs2 = Embedded(path2, None, None)
#plt.axis([0, 45, -0.1, 1])
#
#ceps = cs.Ceps(cs.y[55125:55125+10000])
#ac = cs.hanniPC(cs.y[55125:55125+10000])
#
#ceps2 = cs.Ceps(cs.y[165375:165375+10000])
#ac2 = cs.hanniPC(cs.y[165375:165375+10000])
#
##plt.figure(figsize=(16, 9))
#
#plt.plot(ceps, label='Komplexes Cepstrum')
##plt.plot(ac, label='Auto-Cepstrum')
#plt.plot(ceps2, label='Komplexes Cepstrum 2')
##plt.plot(ac2, label='Auto-Cepstrum 2')
##plt.axis([0, 45, -0.1, 1])
#plt.xlabel('Quefrency')
#plt.ylabel('Amplitude')
#plt.legend(loc=1)
#plt.show()