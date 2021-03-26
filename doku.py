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

time=int(30)


msg = Message('01010101', 13, 18)

key = Keygen(time*44100, msg.len)

ipath = 'import/44 Pianisten 01-Promenade.wav'
epath = '/media/sf_X_DRIVE/Documents/repros/fromwmtostego/export/test_data_02/01010101/'
audio = Audio(ipath, epath, 'test.wav', 7, 30, 0.2)
stego, EchoSig, echo0, echo1, key = audio.encode(msg, epath, key)


fig, axs = plt.subplots(3)

#fig.suptitle('Key Signal/ Echo Signal')

axs[0].plot(EchoSig.y[0:1500], label='Echo Signal', color='red')
axs[0].set_title('Echo Signal')
axs[1].plot(key.fil[0:1500], label='Key Signal', color='green')
axs[1].set_title('Key Signal')
axs[1].set( ylabel='Magnitude')
axs[2].plot(key.fil[0:1500]*EchoSig.y[0:1500], label='Key Signal * Echo Signal', color='orange')
axs[2].set_title('Combination EchoSig and Key')
axs[2].set(xlabel='Frames')


#for ax in axs.flat:
#	ax.set(xlabel='Frames', ylabel='Magnitude')

#plt.plot(EchoSig.y, label='Echo Signal')
#plt.plot(key.fil, label='Key Signal')
plt.show()


#print(key.sig.size)

#for file in os.listdir(ipath):
#	print(os.path.join(ipath, file))
#	inp = os.path.join(ipath, file)
#	out = os.path.join(epath, file)
#	audio = Audio(inp, out, 'test.wav', 5, time, 0.2)
#	stego, EchoSig, echo0, echo1, key = audio.encode(msg, out, key)
#	stego.write(key, msg)

