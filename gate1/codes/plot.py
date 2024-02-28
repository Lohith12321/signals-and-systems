import numpy as np
import matplotlib.pyplot as plt

# Read coordinates from the file
data = np.loadtxt('plot.txt')

# Extract t and y values
t = data[:, 0]
y = data[:, 1]

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(t, y, label='y(t) = u(t) * (6 - 6e^(-10t) - 60t e^(-10t))')
plt.scatter(1, y[np.where(t == 1)[0][0]], color='red', label='y(1)', zorder=5)
plt.axvline(x=1, color='gray', linestyle='--', label='t=1', zorder=0)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig("plot.png")

