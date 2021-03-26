import librosa as lro, matplotlib.pyplot as plt, math,librosa.display, numpy as np, bitarray, datetime, os, scipy as sc, random
import random as rn
from audio import Audio
from message import Message
from scipy.signal import find_peaks
import bitarray
from embedded import Embedded
from scipy.signal import find_peaks
from keyGen import Keygen

#file = "44 Pianisten 01-Promenade.wav"

#ipath = '/media/sf_X_DRIVE/Documents/repros/fromwmtostego/export/dsss_test_data/'

ipath = 'import/44 Pianisten 01-Promenade.wav'
msg = Message('01010101', 13, 18)

time=int(30)

key = Keygen(time*44100, msg.len)


epath = '/media/sf_X_DRIVE/Documents/repros/fromwmtostego/export/'

audio = Audio(ipath, epath, 'test.wav', 5, time, 1)
stego, EchoSig, echo0, echo1, key = audio.encode(msg, epath, key)

print(key.fil.size)

b=3
corr = np.correlate(stego.y[0:165375], key.fil[0:165375]*1, 'valid')
print(corr)
corr = np.correlate(stego.y[165376*b:165376*b+165375], key.fil[165376*b:165376*b+165375]*1, 'valid')
print(corr)

#plt.plot(stego.y[165376*b:165376*b+165375])
#plt.plot(stego.y[0:165375])

#plt.plot(key.fil[165376*b:165376*b+165375])
plt.plot(EchoSig.y)
plt.show()

#find average, maxium, minimum (Statisical values)


#corr = np.correlate(stego, data1, 'valid')













#file = '44 Pianisten 01-Promenade.wav'
##pathtxt = 'export/44 Pianisten 01-Promenade.wav_key.txt'
#
#text = ''
#
#print(file)
#inp = os.path.join(ipath, file)
#pathtxt = os.path.join(ipath+"txt/", file+"_key.txt")
#cs = Embedded(inp, None, None, 100, 8, pathtxt)









#data0 = np.zeros(0)
#data1 = np.zeros(0)
#data2 = np.zeros(0)
#data3 = np.zeros(0)
#data4 = np.zeros(0)
#data5 = np.zeros(0)
#data6 = np.zeros(0)
#data7 = np.zeros(0)
#
##0
#for i in cs.position[0]:
#	data0 = np.append(data0, cs.y[i:i+100])
##1
#for i in cs.position[1]:
#	data1 = np.append(data1, cs.y[i:i+100])	
##0
#for i in cs.position[2]:
#	data2 = np.append(data2, cs.y[i:i+100])	
##1
#for i in cs.position[3]:
#	data3 = np.append(data3, cs.y[i:i+100])	
##0
#for i in cs.position[4]:
#	data4 = np.append(data4, cs.y[i:i+100])	
##1
#for i in cs.position[5]:
#	data5 = np.append(data5, cs.y[i:i+100])	
##0
#for i in cs.position[6]:
#	data6 = np.append(data6, cs.y[i:i+100])	
##1
#for i in cs.position[7]:
#	data7 = np.append(data7, cs.y[i:i+100])	
#
#
#corr = np.correlate(data2, data1, 'valid')
#print(corr)
#corr = np.correlate(data2, data2, 'valid')
#print(corr)
#corr = np.correlate(data2, data3, 'valid')
#print(corr)
#corr = np.correlate(data2, data4, 'valid')
#print(corr)
#corr = np.correlate(data2, data5, 'valid')
#print(corr)
#corr = np.correlate(data2, data6, 'valid')
#print(corr)
#corr = np.correlate(data2, data7, 'valid')
#print(corr)


#print(cs.position)
#print(cs.position[1][101])
#print(cs.position[1][102])
#print('-------------------------------')
#p1 = cs.position[1][101]+200
#p2 = cs.position[1][101]+200
#
#print(p1)
#print(p2)
#a = cs.y[p1:p1+100]
#v = cs.y[p2:p2+100]
#
#corr = np.correlate(a, v, 'valid')
#
#print(corr)

#print(cs.peaks)
#print(cs.msg)


