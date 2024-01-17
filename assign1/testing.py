import numpy as np
import matplotlib.pyplot as plt

# Define the wave equation
def wave_equation(x, t):
    return 2 * np.cos(3 * x - 4 * t)

# Generate x values
x_values = np.linspace(0, 10, 400)

# Generate t values for multiple time steps
t_values = np.linspace(0, 5, 5)

# Plot the wave for each time step
for t in t_values:
    y_values = wave_equation(x_values, t)
    plt.plot(x_values, y_values, label=f't = {t:.2f}')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Wave Equation: y = 2cos(3x - 4t)')
plt.legend()

# Show the plot
plt.savefig('graph.png')
plt.show()
