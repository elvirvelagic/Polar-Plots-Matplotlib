import math

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

theta = np.linspace(0, 2 * math.pi, 1000)
r = np.exp(np.sin(theta)) - 2 * np.cos(4 * theta) + np.sin((2 * theta - np.pi) / 24) ** 5

plt.figure(figsize=(6,6))
ax = plt.subplot(111, polar=True)
ax.plot(theta, r)

plt.show()