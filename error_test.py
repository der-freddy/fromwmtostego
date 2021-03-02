import librosa as lro, matplotlib.pyplot as plt, math,librosa.display, numpy as np, bitarray, datetime, os, scipy as sc, random
import random as rn
from audio import Audio
from message import Message
from scipy.signal import find_peaks
import bitarray
from embedded import Embedded
from scipy.signal import find_peaks

#file = "44 Pianisten 01-Promenade.wav"

ipath = "/media/sf_X_DRIVE/Documents/repros/fromwmtostego/export/test_data_03/32bit_rand/"



#path = 'export/44 Pianisten 01-Promenade.wav'
#pathtxt = 'export/44 Pianisten 01-Promenade.wav_key.txt'

text = ''

for file in os.listdir(ipath):

	print(file)
	inp = os.path.join(ipath, file)
	pathtxt = os.path.join(ipath+"txt/", file+"_key.txt")
	cs = Embedded(inp, None, None, 100, 32, pathtxt)		
	print(cs.peaks)
	print(cs.msg)




