import glob, os, matplotlib.pyplot as plt, numpy as np, math
from audio import Audio
from message import Message


#Embedding/Encoding
import_path = 'import/'
export_path = 'export/'
#Nachrichten-Objekt
msg = Message('R')

print(msg.mb_len)


#Fuer alle Dateien in import_path
for file in os.listdir(import_path):

	path = import_path+file
	#Objekterstellung
	cs = Audio(path, export_path, file,3, 10)
	#Einbettung der Nachricht im Signal
	cs.encode(msg, export_path)

	print(path)

