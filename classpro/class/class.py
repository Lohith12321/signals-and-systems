import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Wave Amplitude
A = 5
# Wave Period
T = 0.02
# Time Samples
t = np.linspace(-2.5 * T, 2.5 * T, 10000)  # Corrected the number of samples to 10000

# Plot wave
plt.plot(t, A / 2 * (1 + signal.square(2 * np.pi * t / T)))
plt.ylim(-1, 6)
plt.grid()
plt.xlabel('$t$')
plt.ylabel('$g(t)$')

# Save figure # Cth

plt.savefig('clg.png')


plt.show()
