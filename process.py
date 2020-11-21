"""Processing module."""

from os import stat
import numpy as np

class ProcessCircle:
    """Class for circle processing."""

    def __init__(self) -> None:
        """Construct new Processor."""
        super().__init__()
        self.solution:float

    def streamProcess(self, datum):
        """Process one piece of data at a Point."""
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
    def process(dataSrc):
        """Process data provided at once."""
        processor = ProcessCircle()
        for data in ProcessCircle.reader(dataSrc):
            processor.streamProcess(data)
        return processor.solution
