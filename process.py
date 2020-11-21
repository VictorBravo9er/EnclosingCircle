"""Processing module."""

from os import stat
import numpy as np


class ProcessCircle:
    """Class for circle processing."""

    def __init__(self) -> None:
        """Construct new Processor."""
        super().__init__()
        self.state:list = []
        self.solution:dict = {}

    def reset(self):
        """Reset for further processind on different data-set."""
        self.state.clear()
        self.solution.clear()

    def streamProcess(self, datum):
        """Process one piece of data at a Point."""
        try:
            p1, p2 = self.state[0:2]
        except(ValueError):
            self.state.append(datum)
            if len(self.state) == 2:
                p1, p2 = self.state[0:2]
                self.solution["centre"] = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
                self.solution["radius"] = ProcessCircle.distance(p1,p2)
            return
        pass


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
        for data in ProcessCircle.reader(dataSrcName):
            processor.streamProcess(data)
        return processor.solution

    @staticmethod
    def distance(thisPoint, thatPoint):
        """Return distance between two points."""
        return ( ((thisPoint[1] - thatPoint[1]) ** 2) + ((thisPoint[0] - thatPoint[0]) ** 2) ) * 0.5
