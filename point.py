"""Module for Point."""
import numpy as np
from math import radians, atan, degrees, sqrt, cos, sin, inf, pi

class Point():
    f"""Description of class."""

    __name__ = "Point"
    def __init__(self, x:float, y:float):
        """Construct new Point."""
        super().__init__()
        self.X = x
        self.Y = y

    def angleTo(self, point):
        """Find angle(radians) to another point w.r.t. X-axis. -ve allowed."""
        angle = atan(self.slopeTo(point))
        if self.Y < point.Y:
            return angle
        return(angle * -1)

    def angleFromPoints(self, pointA, pointB):
        """Find angle(radian) subtended on self from A and B. -ve allowed."""
        a1 = self.angleTo(pointA)
        a2 = self.angleTo(pointB)
        angle = a2 - a1
        return(angle)

    def slopeTo(self, point):
        """Find slope(directionless) to another point w.r.t. X-axis. -ve allowed."""
        num = (self.Y - point.Y)
        den = (self.X - point.X)
        if den == 0:
            if num == 0:
                return 0
            return inf
        return(num / den)

    def angleFromLine(self, line):
        """Find angle(radian) subtended on self from endpoints of a line. -ve allowed."""
        return(self.angleFromPoints(line.start, line.end))

    def getPoint(self):
        """Return point coordinates as a tuple."""
        return(self.X, self.Y)
   
    def __ne__(self, point):
        """'!=' operator overload."""
        return not self.__eq__(point)

    def __eq__(self, point):
        """'==' operator overload."""
        if self.X == point.X and self.Y == point.Y:
            return True
        return False

    def __add__(self, other):
        """'+' operator overload."""
        new = Point(self.X + other.X, self.Y + other.Y)
        return new

    @classmethod
    def middlePoint(cls, point1, point2):
        """Return midPoint of 2 points."""
        return(cls((point1.X + point2.X)/2, (point1.Y + point2.Y)/2))

    def distanceSquared(self, o):
        """Return square of pythagorean distance."""
        return(((self.Y - o.Y) ** 2) + ((self.X - o.X) ** 2))

    def distanceL1(self, o):
        """L1 distance."""
        return( abs(self.Y - o.Y) + abs(self.X - o.X) )


    def distanceTo(self, o):
        """Distance to/from a point."""
        return sqrt(self.distanceSquared(o))

    def __str__(self):
        """Text return."""
        return(f"{self.__name__}: ({self.X}, {self.Y})")