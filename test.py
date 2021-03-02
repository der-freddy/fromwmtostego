import glob, os, matplotlib.pyplot as plt, numpy as np, math
from bitarray import bitarray
from message import Message
from keyGen import Keygen
from audio import Audio

rand_n = np.random.rand(32)

rand_n[np.where(rand_n < 0.5)] = 0
rand_n[np.where(rand_n >= 0.5)] = 1

print(str(rand_n))

test = str('')

for i in rand_n:
	test = test+str(int(i))

print(test)

msg = Message(test, 15, 20)

ipath = 'import'
epath = '/media/sf_X_DRIVE/Documents/repros/fromwmtostego/export/test_data_03/'
#audio = Audio(ipath, epath, 'test.wav', 7, 10)

time=int(30)

key = Keygen(time*44100, msg.len)

#print(key.sig.size)

for file in os.listdir(ipath):
	print(os.path.join(ipath, file))
	inp = os.path.join(ipath, file)
	out = os.path.join(epath, file)
	audio = Audio(inp, out, 'test.wav', 5, time, 0.3)
	stego, EchoSig, echo0, echo1, key = audio.encode(msg, out, key)
	stego.write(key, msg)

