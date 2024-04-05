import numpy as np
from scipy import signal, fft
import soundfile as sf
import matplotlib.pyplot as plt

def myfiltfilt(b, a, input_signal):
    # Ensure input signal is longer than 100 samples
    if len(input_signal) <= 100:
        raise ValueError("Input signal must be longer than 100 samples.")

    X = fft.fft(input_signal)
    w = np.linspace(0, 1, len(X), endpoint=False)
    W = np.exp(2j * np.pi * w)
    B = np.abs(np.polyval(b, W))**2
    A = np.abs(np.polyval(a, W))**2
    Y = B * (1 / A) * X
    filtered_signal = fft.ifft(Y).real

    return filtered_signal

# Read .wav file
input_signal, fs = sf.read('’Sound_With_ReducedNoise.wav')
print(f"Input signal length: {len(input_signal)} samples")

if len(input_signal.shape) > 1:
    input_signal = input_signal[:, 0]

# Sampling frequency of input signal
sampl_freq = fs

# Order of the filter
order = 6

# Cutoff frequency
cutoff_freq = 2000.0

# Digital frequency
Wn = 2 * cutoff_freq / sampl_freq

# Design the filter
b, a = signal.butter(order, Wn, 'low')

# Filter the input signal with butterworth filter
output_signal = signal.filtfilt(b, a, input_signal)
op1 = myfiltfilt(b, a, input_signal)

# Verify outputs by plotting
x_plt = np.arange(len(input_signal))
plt.plot(x_plt[1000:10000], output_signal[1000:10000], 'b.', label='Output by built-in function')
plt.plot(x_plt[1000:10000], op1[1000:10000], 'r.', label='Output by custom function')
plt.title("Verification of Audio Filter Outputs")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()
plt.savefig("plot8.png")
plt.show()
