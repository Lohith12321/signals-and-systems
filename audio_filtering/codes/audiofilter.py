import soundfile as sf
from scipy import signal

# Read the input audio file
input_signal, fs = sf.read('song.wav')
print(input_signal)

# Check the shape of the input signal if it's multi-channel
# If it's multi-channel, take only the first channel
if len(input_signal.shape) > 1:
    input_signal = input_signal[:, 0]


# Define filter parameters
order = 6
cutoff_freq = 2000.0
Wn = 2 * cutoff_freq / fs

# Design the Butterworth low-pass filter
b, a = signal.butter(order, Wn, 'low')

print(a)
print(b)

# Apply the filter to the input signal
output_signal = signal.filtfilt(b, a, input_signal)

# Write the filtered signal to a new audio file
sf.write('’Sound_With_ReducedNoise.wav', output_signal, fs)

