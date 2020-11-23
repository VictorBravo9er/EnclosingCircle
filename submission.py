# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from process import ProcessCircle
import matplotlib.pyplot as plt



# %%

data, targets, centre, radius = ProcessCircle.process("data/data0.txt")
ProcessCircle.test(data, centre, radius)

print(centre, radius)
_, a = plt.subplots(1)
x = [x for (x, y) in data]
y = [y for (x, y) in data]
cirX, cirY = ProcessCircle.getCircle(centre, radius)
a.scatter(x, y, s=10)
a.scatter(*centre, color="red")
a.plot(cirX, cirY, color="green")
a.set_aspect(1)
plt.show()



# %%

data, targets, centre, radius = ProcessCircle.process("data/data1.txt")
ProcessCircle.test(data,centre,radius)

print(centre, radius)
_, a = plt.subplots(1)
x = [x for (x,y) in data]
y = [y for (x,y) in data]
cirX, cirY = ProcessCircle.getCircle(centre, radius)
a.scatter(x,y,s=10)
a.scatter(*centre, color="red")
a.plot(cirX, cirY, color="green")
a.set_aspect(1)
plt.show()


# %%

data, targets, centre, radius = ProcessCircle.process("data/data2.txt")
ProcessCircle.test(data,centre,radius)
print(centre, radius)
_, a = plt.subplots(1)
x = [x for (x,y) in data]
y = [y for (x,y) in data]
cirX, cirY = ProcessCircle.getCircle(centre, radius)
a.scatter(x,y,s=10)
a.scatter(*centre, color="red")
a.plot(cirX, cirY, color="green")
a.set_aspect(1)
plt.show()




# %%

data, targets, centre, radius = ProcessCircle.process("data/data3.txt")
ProcessCircle.test(data,centre,radius)

print(centre, radius)
_, a = plt.subplots(1)
x = [x for (x,y) in data]
y = [y for (x,y) in data]
cirX, cirY = ProcessCircle.getCircle(centre, radius)
a.scatter(x,y,s=10)
a.scatter(*centre, color="red")
a.plot(cirX, cirY, color="green")
a.set_aspect(1)
plt.show()

