import numpy as np
import matplotlib.pyplot as plt

# Define the piecewise function h_LP(n)
def h_Lp(n):
    return np.where((n != 0) & (n >= -100) & (n <= 100), np.sin(n * np.pi / 40) / (n * np.pi + 1e-20), 0)

# Generate values for n
n_values = np.arange(-480, 491)

# Calculate the function values
h_values = h_Lp(n_values)

# Calculate the DTFT using numpy's FFT
H_freq_response = np.fft.fftshift(np.fft.fft(h_values))

# Angular frequency axis (normalized)
omega_normalized = np.linspace(-np.pi/2, np.pi/2, len(n_values))

# Plotting
plt.plot(omega_normalized/np.pi, np.abs(H_freq_response))
plt.xlabel('($\omega$/pi)')
plt.ylabel('|H(r$\omega$)|')
plt.title('FIR LOW PASS FILTER')
plt.grid(True)

plt.savefig("plot7.png")
