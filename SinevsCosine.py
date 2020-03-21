import numpy as np
import matplotlib.pyplot as plt

wave_array = [-np.pi * 2, -(np.pi / 4) * 7, -(np.pi / 2) * 3, -(np.pi / 4) * 5, -np.pi, -(np.pi / 4) * 3, -np.pi / 2, -np.pi / 4, 0, np.pi / 4, np.pi / 2, (np.pi / 4) * 3, np.pi,
             (np.pi / 4) * 5, (np.pi / 2) * 3, (np.pi / 4) * 7, np.pi * 2]
sin_values = np.sin(wave_array)
cos_values = np.cos(wave_array)

plt.plot(wave_array, sin_values, color = "red", marker = "+")
plt.plot(wave_array, cos_values, color = "green", marker = "o")
plt.title("Sine vs. Cosine")
plt.xlabel("x")
plt.ylabel("y")
plt.show