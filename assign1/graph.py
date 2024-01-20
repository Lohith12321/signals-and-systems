import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
amplitude = 1.0
frequency = 1.0  
phase = 0.0  
duration = 5 
sampling_rate = 1000  # Number of samples per second

t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

wave = amplitude * np.sin(2 * np.pi * frequency * t + phase)

# Plot the wave
plt.plot(t, wave)
plt.title('Sound Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (cm)')
plt.grid(True)
plt.savefig('graph.png')
plt.show()
