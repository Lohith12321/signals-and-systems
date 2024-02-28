import numpy as np
import matplotlib.pyplot as plt

# Define the function
def y(t):
    return np.heaviside(t, 1) * (6 - 6*np.exp(-10*t) - 60*t*np.exp(-10*t))

# Generate t values
t = np.linspace(0, 2, 1000)

# Generate y values
y_values = y(t)

# Plot the function
plt.figure(figsize=(10, 6))
plt.plot(t, y_values, label='y(t) = u(t) * (6 - 6e^(-10t) - 60t e^(-10t))')
plt.scatter(1, y(1), color='red', label='y(1)', zorder=5)
plt.axvline(x=1, color='gray', linestyle='--', label='t=1', zorder=0)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('plot.png')
