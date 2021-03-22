import glob, os, matplotlib.pyplot as plt, numpy as np, math
from bitarray import bitarray
from message import Message
from keyGen import Keygen
from audio import Audio
import decomposition
from audio_file import AudioFile

# generate random bitstring
rand_n = np.random.rand(32)
rand_n[np.where(rand_n < 0.5)] = 0
rand_n[np.where(rand_n >= 0.5)] = 1

bitstring = str('')
for i in rand_n:
    bitstring = bitstring+str(int(i))

# assign delays and decay
delay0 = 13	    # 15
delay1 = 18		# 20
decay = 1		# 0.3

# generate message with delays
msg = Message(bitstring, delay0, delay1)

#
cover_audio_filepath = 'SaChenPromenade1.wav'
cover_audio = AudioFile(cover_audio_filepath)

# specify wavelet type and desired decomposition depth/level ('db2' can be used as default)
wavelet = 'haar'
decomposition_level = 2

# perform decomposition
all_coeffs, dc = decomposition.decomposition(
    cover_audio, wavelet_type=wavelet, level=decomposition_level, print_out=True)

# generate key
key = Keygen(len(dc), msg.len)

# perform embedding on extracted detail coefficients (dc)
out = f'output_files/out_dwt_level_{decomposition_level}_echo.wav'
output_name = f'out_dwt_level_{decomposition_level}_echo'
audio = Audio(path=cover_audio_filepath, export=out, name=output_name,
              os=0, du=0, decay=decay, array_signal=dc)
stego, EchoSig, echo0, echo1, key = audio.encode(msg, out, key)
stego.write(key, msg)

modified_dc = stego.y

# reconstruct audio file by passing unmodified coefficients (all_coeffs) and modified detail coefficients from
# decomposition_level (modified_dc) to function
reconstructed_audio = decomposition.reconstruct_w_modified_dcoeffs(
    all_coeffs, modified_dc, wavelet_type=wavelet, level=decomposition_level)

# write reconstructed file
reconstructed_file = AudioFile(out, sampling_rate=44100, read=False)
reconstructed_file.signal_data = reconstructed_audio
reconstructed_file.write_file(transpose=True)

### read and detect ###

# read in file
mod_audio_path = out
mod_audio = AudioFile(mod_audio_path)
print(f'{mod_audio.signal_data}')

mod_all_coeffs, mod_dc = decomposition.decomposition(mod_audio, wavelet_type=wavelet, level=decomposition_level,
                                                     print_out=True)

hann = np.hanning(mod_dc.size)
x = np.fft.fft(mod_dc*hann)
x = np.log(x)
ceps = np.abs(np.fft.ifft(x))

plt.plot(ceps[0:44])
plt.show()
