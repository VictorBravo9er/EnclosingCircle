import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 100)

radius = 0.3

a = radius*np.cos(theta)
b = radius*np.sin(theta)

figure, axes = plt.subplots(1)

axes.plot(a, b)
axes.set_aspect(1)

plt.title('Circle using Parametric Equation')
plt.show()