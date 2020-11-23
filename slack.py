from process import ProcessCircle


def streamProcess(self, datum):
    """Process one piece of data at a Point."""
    print()
    l = len(self.state)
    if l == 0:
        self.state.append(datum)
        self.solution.append(datum)
        self.solution.append(0)
    elif l == 1:
        self.state.append(datum)
        p1, p2 = self.state[0:2]
        self.solution[0] = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
        self.solution[1] = ProcessCircle.distanceSquared(p1, p2)
    elif ProcessCircle.distanceSquared(self.solution[0], datum) > self.solution[1]:
        self.newCentre(datum)
        a = ProcessCircle.distanceSquared(self.state[0], self.solution[0])
        b = ProcessCircle.distanceSquared(self.state[1], self.solution[0])
        assert abs(a - b) < 0.00001
    print(datum)
    print(self.state)
    print(self.solution)
    return

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
def processReserve(dataSrcName):
    """Process data provided at once."""
    processor = ProcessCircle()
    data = []
    for datum in ProcessCircle.reader(dataSrcName):
        processor.streamProcess(datum)
        data.append(datum)
    processor.solution[1] = processor.solution[1] ** 0.5
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
