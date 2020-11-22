import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-0.5, 0.5, 100)
y = np.linspace(-0.5, 0.5, 100)

a, b = np.meshgrid(x,y)

C = a**2+b**2-0.2

figure, axes = plt.subplots()

axes.contour(a,b,C,[0])
axes.set_aspect(1)

plt.show()
