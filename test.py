import glob, os, matplotlib.pyplot as plt, numpy as np, math
from audio import Audio
from message import Message


#Embedding/Encoding
import_path = 'import/'
export_path = 'export/'
#Nachrichten-Objekt
msg = Message('R')

print(msg.mb_len)

dte = list(range(0, 44, 1))
for i in range(0, 44):
	dte[i] =  math.exp(-0.5*(float(i)/8))

dte2 = list(range(0, 44, 1))
for i in range(0, 44):
	dte2[i] = 1

dte1 = list(range(0, 44, 1))
for i in range(0, 44):
	dte1[i] =  math.exp(-0.5*(float(i)/30))

#Fuer alle Dateien in import_path
#for file in os.listdir(import_path):
#
#	path = import_path+file
#	#Objekterstellung
#	cs = Audio(path, export_path, file,3, 10)
#	#Einbettung der Nachricht im Signal
#	oe, echo0, ws = cs.encode(msg, export_path)
#
#	print(path)


#ws2 = cs.Ceps(ws[10000:15000])

plt.figure(figsize=(16, 9))
print(dte2)
plt.plot(dte2, '.',label='DTE 1')
plt.plot(dte1, '.',label='DTE 2')
plt.plot(dte, '.',label='DTE 3')

#plt.plot(ws2, label='Cepstrum Segment 2')
#plt.plot(ws_ceps, label='Cepstrum eines Signals mit Wasserzeichen')
#plt.plot(oe_ceps, label='Cepstrum des Originalsignals')
#plt.plot(oe_ceps[12:], label='OE')
#plt.plot(mix, label='ECHO0')


plt.axis([0, 45, -0.1, 1.2])
plt.xlabel('Quefrency')
plt.ylabel('Amplitude')
plt.legend(loc=1)
plt.show()