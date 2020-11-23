
from process import ProcessCircle, getCircle as Circle
import matplotlib.pyplot as plt
from json import dumps

x = []
y = []
radius = []

data, sol = ProcessCircle.process("data.txt")

centre = sol[0]
radius = sol[1]
x = [x for (x,y) in data]
y = [y for (x,y) in data]

cir = Circle(centre, radius)
figure, axes = plt.subplots(1)
axes.scatter(x, y, color="red")
axes.scatter(centre[0], centre[1], color="green")
axes.plot(*cir)
axes.set_aspect(1)
plt.show()

"""
d = {"x":x, "y":y,"centres":centres}

with open("log.json", mode="w") as file:
    file.write(dumps(d))
"""


