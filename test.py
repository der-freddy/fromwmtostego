import glob, os, matplotlib.pyplot as plt, numpy as np, math
from bitarray import bitarray
from message import Message
from keyGen import Keygen
from audio import Audio

msg = Message('01010101', 12, 16)

ipath = 'import'
epath = 'export'
#audio = Audio(ipath, epath, 'test.wav', 7, 10)

key = Keygen(10*44100, msg.len)

#print(key.sig.size)

for file in os.listdir(ipath):
	print(os.path.join(ipath, file))
	inp = os.path.join(ipath, file)
	out = os.path.join(epath, file)
	audio = Audio(inp, out, 'test.wav', None, 10)
	stego, EchoSig, echo0, echo1, key = audio.encode(msg, out, key)
	stego.write(key)





