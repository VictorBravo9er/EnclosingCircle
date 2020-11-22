"""Processing module."""

from os import stat
from matplotlib.pyplot import draw
import numpy as np
from numpy import sin, cos, inf, pi
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


class ProcessCircle:
    """Class for circle processing."""

    def __init__(self) -> None:
        """Construct new Processor."""
        super().__init__()
        self.state:list = []
        # state Stores Diameter
        self.solution:list = []
        # solution stores updated solution after each data input

    def reset(self):
        """Reset for further processind on different data-set."""
        self.state.clear()
        self.solution.clear()

    def streamProcess(self, datum):
        """Process one piece of data at a Point."""
        print()
        print(datum)
        print(self.state)
        print(self.solution)
        l = len(self.state)
        if l == 0:
            self.state.append(datum)
            self.solution.append(datum)
            self.solution.append(0)
            return
        if l == 1:
            self.state.append(datum)
            p1, p2 = self.state[0:2]
            self.solution[0] = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
            self.solution[1] = ProcessCircle.distanceSquared(p1, p2)
            return
        if ProcessCircle.distanceSquared(self.solution[0], datum) < self.solution[1]:
            return
        self.newCentre(datum)

    def newCentre(self, newPoint):
        """Calculate new circle and diameter."""
        # y = mx + c
        point = self.state[0]
        if ProcessCircle.distanceSquared(newPoint, point) < ProcessCircle.distanceSquared(newPoint, self.state[1]):
            point = self.state[1]
        m = ProcessCircle.slope(point, self.solution[0])
        # x x_ + y y_ = (_x x_ + _y y_) / 2
        x_ = point[0] - newPoint[0]
        y_ = point[1] - newPoint[1]
        _x = point[0] + newPoint[0]
        _y = point[1] + newPoint[1]
        x = 0
        y = 0
        if m == inf:
            # y = (_x x_ + _y y_ - 2 x x_) / (2 y_)
            x = point[0]
            y = (_x * x_ + _y * y_ - 2 * x * x_) / (2 * y_)
        else:
            c = point[1] - m * point[0]
            x = (_x * x_ + (_y - 2 * c) * y_) /(2 * (x_ + m * y_))
            y = m * x + c
        self.solution[0] = (x,y)
        self.solution[1] = ProcessCircle.distanceSquared(newPoint, (x,y))
        self.state = [newPoint, point]
        #self.state = [point, newPoint]

    @staticmethod
    def reader(file):
        """Use this to read data from a file(filename)."""
        with open(file) as file:
            for line in file.readlines():
                temp = line.split()
                if temp.__len__() == 2:
                    temp = (int(temp[0]), int(temp[1]))
                    yield(temp)

    @staticmethod
    def process(dataSrcName):
        """Process data provided at once."""
        processor = ProcessCircle()
        data = []
        for datum in ProcessCircle.reader(dataSrcName):
            processor.streamProcess(datum)
            data.append(datum)
        processor.solution[1] **= 0.5
        return data, processor.solution

    @staticmethod
    def processLIVE(datasrc):
        """Process data provided at once."""
        processor = ProcessCircle()
        x = []
        y = []
        for datum in ProcessCircle.reader(datasrc):
            processor.streamProcess(datum)
            x.append(datum[0])
            y.append(datum[1])
            yield(x,y,processor.solution[0], processor.solution[1])

    @staticmethod
    def distanceSquared(thisPoint, thatPoint):
        """Return squared distance between two points."""
        return ( ((thisPoint[1] - thatPoint[1]) ** 2) + ((thisPoint[0] - thatPoint[0]) ** 2) ) * 0.5

    @staticmethod
    def distance(thisPoint, thatPoint):
        """Return distance."""
        return ProcessCircle.distanceSquared(thisPoint, thatPoint) ** 0.5

    @staticmethod
    def slope(thisPoint, thatPoint):
        """Find Slope."""
        den = (thisPoint[0] - thatPoint[0])
        if den == 0:
            return inf
        return ((thisPoint[1] - thatPoint[1]) / den)

    @staticmethod
    def rotate(thisPoint, centreOfRotation):
        """Return a rotated point."""
        ret = [(2 * centreOfRotation[0] - thisPoint[0]), (2 * centreOfRotation[1] - thisPoint[1])]
        return ret

def getCircle(centre, radius):
    """Return plottable graph of a circle."""
    theta = np.linspace(0, 2*pi, 100)

    a = radius*cos(theta) + centre[0]
    b = radius*sin(theta) + centre[1]
    return(a,b)

ProcessCircle.process("data.txt")