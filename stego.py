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

test = cs.ceps[1]



peaks, _ = find_peaks(test[0:44])

ceps_mean = np.mean(test[peaks])

#print(ceps_mean)

peaks, pros = find_peaks(test[0:44], height=ceps_mean, width=1)

#print(peaks)
#print(pros)


max_v = (np.argmax(test[peaks]))


ceps1 = cs.Ceps(cs.y)


plt.plot(test[0:44])
#plt.plot(peaks, test[peaks], 'x')
plt.plot(peaks[max_v], test[peaks[max_v]], 'x')
#plt.plot(cs.ceps[1][0:44])
#plt.plot(cs.ceps[2][0:44])
#plt.plot(cs.ceps[3][0:44])
#plt.plot(cs.ceps[4][0:44])
#plt.plot(cs.ceps[5][0:44])
#plt.plot(cs.ceps[6][0:44])
#plt.plot(cs.ceps[7][0:44])
plt.show()

print(cs.msg)