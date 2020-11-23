
from process import ProcessCircle, getCircle as Circle
import matplotlib.pyplot as plt
from json import dumps

x = []
y = []
centres = []
radius = []
for (x, y, centre, rad) in ProcessCircle.processLIVE("data.txt"):
    centres.append(centre)
    radius.append(rad ** 0.5)
"""
d = {"x":x, "y":y,"centres":centres}

with open("log.json", mode="w") as file:
    file.write(dumps(d))
"""


exit()
l = len(x)
for i in range(l):
    cir = Circle(centres[i], radius[i])
    figure, axes = plt.subplots(1)
    axes.scatter(x[0:i], y[0:i], color="red")
    axes.scatter(centres[i][0], centres[i][1], color="green")
    axes.plot(*cir)
    axes.set_aspect(1)
    plt.show()