import glob, os, matplotlib.pyplot as plt, numpy as np, math
from bitarray import bitarray
from message import Message
from keyGen import Keygen
from audio import Audio

msg = Message('01101100', 15, 15)

ipath = 'import/44 Pianisten 01-Promenade.wav'
epath = 'export/44 Pianisten 01-Promenade.wav'
audio = Audio(ipath, epath, 'test.wav', 7, 10)

key = Keygen(audio.size, msg.len)

stego, EchoSig, echo0, echo1, key = audio.encode(msg, epath, key)

#stego.write(key)



id_p = np.where(key.oe == 1)
id_n = np.where(key.oe == -1)

Id = np.where((key.oe == 1) | (key.oe == -1)) 
#print((id_p[0]))
#print((id_n[0]))
#print((Id[0]))

#####TODO#####
#Negativ values einbauen!!!!#####

hann = np.hanning(key.seedlen)

print(id_p[0][0])
pos = id_p[0]*key.seedlen
print(pos[0])



###Positive Values only
#print(id_p[0][0]*key.seedlen)
#print((id_p[0][0]*key.seedlen)+key.seedlen)
#data = stego.y[(id_n[0][0]*key.seedlen):(id_n[0][0]*key.seedlen)+key.seedlen]*hann
#
#for i in range(1, 40):
#	#print(id_p[0][i]*key.seedlen)
#	#print((id_p[0][i]*key.seedlen)+key.seedlen)
#
#	data = np.append(data, stego.y[(id_n[0][i]*key.seedlen):(id_n[0][i]*key.seedlen)+key.seedlen]*hann)

###Negativ Values only
#print(id_n[0][0]*key.seedlen)
#print((id_n[0][0]*key.seedlen)+key.seedlen)
#data = signal[(id_n[0][0]*key.seedlen):(id_n[0][0]*key.seedlen)+key.seedlen]*hann
#
#for i in range(1, 50):
#	print(id_n[0][i]*key.seedlen)
#	print((id_n[0][i]*key.seedlen)+key.seedlen)
#
#	data = np.append(data, signal[(id_n[0][i]*key.seedlen):(id_n[0][i]*key.seedlen)+key.seedlen]*hann)



####Negativ and Positiv
#print(Id[0][0]*key.seedlen)
#print((Id[0][0]*key.seedlen)+key.seedlen)
#data = signal[(Id[0][0]*key.seedlen):(Id[0][0]*key.seedlen)+key.seedlen]*hann
#for i in range(1, 50):
#	print(Id[0][i]*key.seedlen)
#	print((Id[0][i]*key.seedlen)+key.seedlen)
#	data = np.append(data, signal[(Id[0][i]*key.seedlen):(Id[0][i]*key.seedlen)+key.seedlen]*hann)



#ceps = stego.Ceps(data[:])

#plt.plot(audio.y)
#plt.plot(signal)
#plt.plot(key.sig)
#plt.plot(signal)
plt.plot(key.sig)
plt.plot(key.fil)
plt.show()

###Key output
#f = open('key.txt', 'a')
#for i in range(0, len(key.oe)-1):
#	f.write(str(int(key.oe[i]))+';')
#f.write(str(int(key.oe[len(key.oe)-1])))
#f.close()