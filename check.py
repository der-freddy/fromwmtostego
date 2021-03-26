import librosa as lro, matplotlib.pyplot as plt, math,librosa.display, numpy as np, bitarray, datetime, os, scipy as sc, random
import random as rn
from audio import Audio
from message import Message
from scipy.signal import find_peaks
import bitarray
from embedded import Embedded
from scipy.signal import find_peaks
from bitarray import bitarray

ipath = 'import/44 Pianisten 01-Promenade.wav'


y, sr = lro.load(ipath, mono=False, sr=44100, offset=5, duration=10)

upper = 1
lower = -1
K = 5000

row = y.size
bit = np.array([0,0,0,0,1,1,1,1])

L = int(row/len(bit))
print(L)
nframe = np.floor(row/L)

N = int(nframe - np.mod(nframe, 8))


bits = bit[:]

r = np.ones((L,1))

pr = np.reshape(r*np.ones((1,N)), N*L, order="C")
alpha = 0.005

#[mix, datasig] = mixer(L, bits, -1,1,22055)




K = K - np.mod(K,4)
N = len(bits)
encbit = np.transpose(np.floor(np.reshape(bits, N, order="C")))
print('1')
mix_sig = np.reshape(np.ones((L,1))*encbit, N*L, order='C')
print('2')
c = np.convolve(mix_sig, np.hanning(K))
w_norm = c/max(abs(c))
print('3')
w_sig = w_norm*(upper-lower)+lower
mix_sig = mix_sig*(upper-lower)+lower
print('4')
mix = alpha*w_sig
datasig = mix_sig

print(pr)


#out = data
#
stego = data[1:N*L+1,] + alpha*mix*pr

plt.plot(mix)
#plt.plot(pr)
plt.show()








#
#file = "44 Pianisten 01-Promenade.wav"
#
#inp = "export"
#
#path = os.path.join(inp, file)
#pathtxt = os.path.join(inp, file+"_key.txt")
#
##path = 'export/44 Pianisten 01-Promenade.wav'
##pathtxt = 'export/44 Pianisten 01-Promenade.wav_key.txt'
#
#cs = Embedded(path, None, None, 100, 8, pathtxt)
##cs = Embedded("export/test_file/44 Pianisten 01-Promenade.wav", None, None, 100, 8, pathtxt)
#
#print(cs.y[971])
#print(oe.y[971])
#plt.plot(cs.y)
#plt.plot(oe.y)
##plt.plot(peaks, test[peaks], 'x')
##plt.plot(peaks[max_v], test[peaks[max_v]], 'x')
##plt.plot(cs.ceps[1][0:44])
##plt.plot(cs.ceps[2][0:44])
##plt.plot(cs.ceps[3][0:44])
##plt.plot(cs.ceps[4][0:44])
##plt.plot(cs.ceps[5][0:44])
##plt.plot(cs.ceps[6][0:44])
##plt.plot(cs.ceps[7][0:44])
#plt.show()
#
#print(cs.msg)