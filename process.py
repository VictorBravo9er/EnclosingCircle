"""Processing module."""

from os import stat
import numpy as np


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
        try:
            p1, p2 = self.state[0:2]
        except(ValueError):
            l = len(self.state)
            if l >= 2:
                raise RuntimeError("Something was WRONG!!!")
            self.state.append(datum)
            if l == 1:
                self.solution.append(datum)
                self.solution.append(0)
            if l == 2:
                p1, p2 = self.state[0:2]
                self.solution[0] = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
                self.solution[1] = ProcessCircle.distance(p1, p2)
            return
        if ProcessCircle.distance(self.solution[0], datum) < self.solution[1]:
            return
        self.newCentre(p1, p2, datum)

    def newCentre(self, pointA, pointB, newPoint):
        """Calculate new circle and diameter."""
        # y = mx + c
        m = ProcessCircle.slope(pointA, pointB)


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
        return data, processor.solution

    @staticmethod
    def distance(thisPoint, thatPoint):
        """Return distance between two points."""
        return ( ((thisPoint[1] - thatPoint[1]) ** 2) + ((thisPoint[0] - thatPoint[0]) ** 2) ) * 0.5

    @staticmethod
    def slope(thisPoint, thatPoint):
        """Find Slope."""
        return ((thisPoint[1] - thatPoint[1]) / (thisPoint[0] - thisPoint[0]))

    @staticmethod
    def rotate(thisPoint, centreOfRotation):
        """Return a rotated point."""
        ret = [(2 * centreOfRotation[0] - thisPoint[0]), (2 * centreOfRotation[1] - thisPoint[1])]
        return ret