from json import loads
import matplotlib.pyplot as plt

data = loads("log.json")

x = data["x"]
y = data["y"]
c = data["centres"]
l = len(x)

for i in range(2,l):
    plt.scatter(x[0:i], y[0:i], color="red")