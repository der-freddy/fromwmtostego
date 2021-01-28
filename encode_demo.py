import glob, os, matplotlib.pyplot as plt, numpy as np, math
from audio import Audio
from message import Message


#Embedding/Encoding
import_path = 'import/'
export_path = 'export/'
#Nachrichten Object
msg = Message('R')

print(msg.mb_len)


#for all files in folder import_path
for file in os.listdir(import_path):

	path = import_path+file
	# object building
	cs = Audio(path, export_path, file,3, 10)
	#encode signal
	cs.encode(msg, export_path)

	print(path)

