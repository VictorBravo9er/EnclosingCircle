"""Read File."""

def reader(file):
    with open(file) as file:
        for line in file.readlines():
            temp = line.split()
            if temp.__len__() == 2:
                temp = (int(temp[0]), int(temp[1]))
                yield(temp)