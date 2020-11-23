"""Processing module."""

import numpy as np
from numpy import sin, cos, inf, pi
import matplotlib.pyplot as plt


class ProcessCircle:
    """Class for circle processing."""

    _limit = 0.00001

    def __init__(self) -> None:
        """Construct new Processor."""
        super().__init__()
        # state Stores Diameter
        self.centre: tuple
        self.radius: float
        self.m: float
        self.c: float
        # solution stores updated solution after each data input

    @staticmethod
    def orientation(pointA, pointB, target):
        """Orientation test. 0 - go for it, 1 - decide, -1 - no go, next please. O(1)."""
        if target in (pointA, pointB):
            return -1
        buf = (1,)
        buf = np.array(buf + pointA + buf + pointB + buf + target).reshape(3,-1)
        buf = np.linalg.det(buf)
        """Using a limit may cause bugs. 0.00001 for now."""
        if buf < -ProcessCircle._limit:
            return 0
        if buf < ProcessCircle._limit:
            return 1
        return -1

    def preProcess(self, data):
        """Preprocess data. find two lowest points to anchor circle around. O(n)."""
        lowest = data[0]
        nextPoint = lowest
        for point in data[1:]:
            """O(n)."""
            if lowest[1] > point[1]:
                lowest = point
        for point in data:
            """O(n)."""
            cond = ProcessCircle.orientation(lowest, nextPoint, point)
            if cond == -1:
                continue
            if cond == 0:
                nextPoint = point
                continue
            if cond == 1:
                if ProcessCircle.distanceSquared(lowest, nextPoint) < ProcessCircle.distanceSquared(lowest, point):
                    nextPoint = point
        centr = ((lowest[0] + nextPoint[0]) * 0.5, (lowest[1] + nextPoint[1]) * 0.5)
        radSq = ProcessCircle.distanceSquared(lowest, centr)
        self.centre, self.radius = centr, radSq
        m = ProcessCircle.slope(lowest, nextPoint)
        if m == 0:
            self.m = inf
            self.c = centr[0]
        elif m == inf:
            self.m = 0
            self.c = centr[1]
        else:
            m = -(1.0/m)
            self.m = m
            self.c = centr[1] - m * centr[0]
        """ m & c initialised."""
        return lowest, nextPoint

    def updateCircle(self, point, newPoint):
        """Update circele accordingly. O(1)."""
        """
        Equations used:
            y = mx + y - for perpendicular bisector of initial anchor points
            distance(anchor, newCentre) = distance(newPoint, newCentre)
            newCentre = (x,y)
        """
        x_ = point[0] - newPoint[0]
        y_ = point[1] - newPoint[1]
        _x = point[0] + newPoint[0]
        _y = point[1] + newPoint[1]
        m = self.m
        c = self.c
        if m == inf:
            # y = (_x x_ + _y y_ - 2 x x_) / (2 y_)
            x = c
            y = (_x * x_ + _y * y_ - 2 * x * x_) / (2 * y_)
        else:
            # x = (_x x_ + (_y - 2 c) y_) /(2 * (x_ + m * y_))
            x = (_x * x_ + (_y - 2 * c) * y_) / (2 * (x_ + m * y_))
            y = m * x + c
        """newCentre calculated."""
        self.centre = (x, y)
        self.radius = ProcessCircle.distanceSquared(point, (x,y))
        """Storing pythagorean distance(squared)."""

    def calculate(self, data):
        """Process all points at once. O(n)."""
        anc1, anc2 = self.preProcess(data)
        for point in data:
            """O(n)."""
            if point in (anc1, anc2):
                continue
            distSq = ProcessCircle.distanceSquared(self.centre, point)
            if distSq > self.radius:
                self.updateCircle(anc1, point)
        self.radius = self.radius ** 0.5
        self.target = (anc1, anc2)
        return 

    @staticmethod
    def reader(file):
        """Use this to read data from a file(filename). O(1)."""
        with open(file) as file:
            for line in file.readlines():
                temp = line.split()
                if temp.__len__() == 2:
                    temp = (float(temp[0]), float(temp[1]))
                    yield(temp)

    @staticmethod
    def process(dataSrcName):
        """Process data provided at once. O(n)."""
        processor = ProcessCircle()
        data = list(ProcessCircle.reader(dataSrcName))
        """O(n)."""
        processor.calculate(data)
        """O(n)."""
        return data, processor.target, processor.centre, processor.radius

    @staticmethod
    def distanceSquared(thisPoint, thatPoint):
        """Return squared distance between two points."""
        return( ((thisPoint[1] - thatPoint[1]) ** 2) + ((thisPoint[0] - thatPoint[0]) ** 2) )

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
    def test(data, centre, radius):
        """Test for correcctness."""
        for point in data:
            r = ProcessCircle.distance(centre,point)
            try:
                assert r < radius
            except(Exception):
                print(f"Error by {radius - r}")

    @staticmethod
    def getCircle(centre, radius):
        """Return plottable graph of a circle."""
        theta = np.linspace(0, 2*pi, 1000)

        a = radius*cos(theta) + centre[0]
        b = radius*sin(theta) + centre[1]
        return(a,b)
