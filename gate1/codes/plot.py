import numpy as np
import matplotlib.pyplot as plt

# Define the function
def y(t):
    return np.heaviside(t, 1) * (6 - 66 * np.exp(-10 * t))

# Generate values for t
t = np.linspace(-1, 5, 1000)

# Calculate y values
y_values = y(t)

# Plot the function
plt.figure(figsize=(10, 6))
plt.plot(t, y_values, label='y(t) = u(t) (6 - 66e^(-10t))')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid(True)
plt.savefig('plot.png')
plt.show()
