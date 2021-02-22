import glob, os, matplotlib.pyplot as plt, numpy as np, math
from bitarray import bitarray
from message import Message
from keyGen import Keygen
from audio import Audio

msg = Message('0101010110101010', 15, 20)

ipath = 'import'
epath = 'export/test/0101010101010101/test_10/'
#audio = Audio(ipath, epath, 'test.wav', 7, 10)

time=int(10)

key = Keygen(time*44100, msg.len)

#print(key.sig.size)

for file in os.listdir(ipath):
	print(os.path.join(ipath, file))
	inp = os.path.join(ipath, file)
	out = os.path.join(epath, file)
	audio = Audio(inp, out, 'test.wav', 5, time, 0.3)
	stego, EchoSig, echo0, echo1, key = audio.encode(msg, out, key)
	stego.write(key, msg)

