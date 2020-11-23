from process import ProcessCircle, getCircle as Circle
import matplotlib.pyplot as plt
from json import dumps

x = [20, 13, -12, -5, -9,-14, 5,  ]
y = [-15, 14, 11, -3,  3, 3, -17, ]

f, a = plt.subplots(1)

a.scatter(x,y)
a.scatter(19.17, 15.49, color="red")
a.set_aspect(1)

plt.show()