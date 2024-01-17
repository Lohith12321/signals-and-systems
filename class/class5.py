import numpy as np
import matplotlib.pyplot as plt

# Filter Characteristics
R = 1e3  # 10K ohm resistance
C = 10e-6  # 10 uF capacitance

# Plotting the filter amplitude response
T = 0.02
f_0 = 1 / T
f = np.linspace(-1.5 * f_0, 1.5 * f_0, 100)
s = 1j * 2 * np.pi * f

den = np.polyval([1, -5, 6, 1], s * C * R)
H = 1 / den

plt.plot(f, abs(H))
plt.grid()  # Add minor gridlines
plt.xlabel('$f$ (Hz)')
plt.ylabel('$|H(f)|$')  # Added absolute value for clarity
# Save figure


plt.savefig('graph4.png')
plt.show()
