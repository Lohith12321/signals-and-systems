import numpy as np
import matplotlib.pyplot as plt

# Define the time range
t = np.linspace(0, 2, 1000)

# Define the unit step function
u = np.heaviside(t, 1)

# Define the equation for y(t)
y = u * (6 - 6*np.exp(-10*t) - 60*t*np.exp(-10*t))

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(t, y, label='y(t)')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid(True)
plt.legend()
plt.show()
plt.savefig('plot.png')
