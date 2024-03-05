import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the transfer function
num = [14.4]
den = [0.1, 1, 14.4]
sys = signal.TransferFunction(num, den)

# Create a frequency range
w = np.logspace(-1, 2, 1000)

# Calculate the magnitude and phase of the transfer function
w, mag, phase = signal.bode(sys, w)
plt.figure()

# Magnitude subplot
plt.subplot(2, 1, 1)
plt.semilogx(w, mag)
plt.ylabel(r'$20\log{|T|}$')
plt.grid(True)

# Phase subplot
plt.subplot(2, 1, 2)
plt.semilogx(w, phase)
plt.xlabel(r' $\omega$')
plt.ylabel('Phase [degrees]')
plt.grid(True)

plt.show()
plt.savefig("plot.png")
