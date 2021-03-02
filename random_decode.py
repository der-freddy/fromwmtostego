import librosa as lro, matplotlib.pyplot as plt, math,librosa.display, numpy as np, bitarray, datetime, os
import random as rn
from audio import Audio
from message import Message
from scipy.signal import find_peaks
import bitarray
from embedded import Embedded

file = '44 Pianisten 01-Promenade.wav'
inp = 'export'
path = os.path.join(inp, file)
pathtxt = os.path.join(inp, file+"_key.txt")


cs = Embedded(path, 5, 30, 100, 8, pathtxt)



leng = 100
han = np.hanning(leng)

for j in range(0,100):

	randomList = []
	for i in range(0, 1000):
	    # any random numbers from 0 to 1000
		ran = rn.randint(1, cs.size-leng)
		randomList.append(ran)


	
	randomList = np.sort(randomList)
	
	#print(randomList)
	
	arr = []
	
	for i in randomList:
		win = cs.y[i:i+leng]*han
		arr = np.append(arr, win)
	
	ceps = cs.Ceps(arr[0:])
	
	plt.plot(ceps[0:44], label='Random decoding (unknown segments)')
	plt.legend()
	plt.xlabel('Quefrency')
	plt.ylabel('Magnitude')
	#plt.show()
	plt.savefig('/media/sf_X_DRIVE/Documents/repros/fromwmtostego/export/doku/random_decoing/unkown_segments/oe/length_100/number_1000/detail/'+str(j)+'.png')
	plt.close()
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