import numpy as np
import matplotlib.pyplot as plt

T_0 = 0.01
T = 0.02
f = 1 / T
A = 5
simlen = int(1e3)  # Convert simlen to an integer

# Generating points in t-axis
t = np.linspace(-2.5 * T, 2.5 * T, int(1e4))  # Convert 1e4 to an integer

g = np.zeros_like(t)  # Initialize the signal array

for n in range(21):
    if n == 0:
        g = A * T_0 / T
    else:
        cost = np.cos(2 * np.pi * n * f * t)  # Computing cosine term
        sint = np.sin(2 * np.pi * n * f * t)  # Computing sine term

        an = 2 * A * np.sin(2 * np.pi * n * f * T_0) / (2 * np.pi * n * f * T)  # Computing coefficients
        bn = 2 * A * (1 - np.cos(2 * np.pi * n * f * T_0)) / (2 * np.pi * n * f * T)  # Computing coefficients
        g = g + an * cost + bn * sint  # Evaluating the summation

plt.plot(t, g)
plt.grid()
plt.xlabel('$t$')
plt.ylabel('$g(t)$')

plt.savefig('graph2.png')

plt.show()
