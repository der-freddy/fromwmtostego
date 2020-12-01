import librosa as lro, matplotlib.pyplot as plt, math,librosa.display, numpy as np, bitarray, datetime, os
from audio import Audio
from message import Message
from scipy.signal import find_peaks
import bitarray
from embedded import Embedded

path = 'export/'



#for file in os.listdir(path):
#	print(file)
#	cs = Embedded(path+file, None, None)
#	
#	cs.decode()


########################
#CEPSTUM/ AUTO-CEPSTRUM#
########################
path = 'export/44 Pianisten 01-Promenade_12_18.wav'
path2 = 'export/44 Pianisten 01-Promenade_20_25.wav'

cs = Embedded(path, None, None)
cs2 = Embedded(path2, None, None)
plt.axis([0, 45, -0.1, 1])

ceps = cs.Ceps(cs.y[55125:55125+10000])
ac = cs.hanniPC(cs.y[55125:55125+10000])

ceps2 = cs.Ceps(cs.y[165375:165375+10000])
ac2 = cs.hanniPC(cs.y[165375:165375+10000])

#plt.figure(figsize=(16, 9))

plt.plot(ceps, label='Komplexes Cepstrum')
#plt.plot(ac, label='Auto-Cepstrum')
plt.plot(ceps2, label='Komplexes Cepstrum 2')
#plt.plot(ac2, label='Auto-Cepstrum 2')
#plt.axis([0, 45, -0.1, 1])
plt.xlabel('Quefrency')
plt.ylabel('Amplitude')
plt.legend(loc=1)
plt.show()