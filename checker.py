
from numpy.lib.polynomial import polyint


n = 3
bname = f"simulation/out{n}.txt"

def makeList(name):
    points = None
    with open(name) as file:
        points = file.readline()
    points = points.split("), (")
    flag = True
    temp = ""
    for c in points[0]:
        if flag:
            if c == "(":
                flag = False
        else:
            temp += c
    points[0] = temp
    temp = ""
    for c in points[-1]:
        if c != ")":
            temp += c
        else:
            break
    points[-1] = temp

    le = len(points)
    for i in range(le):
        z = points[i].split(", ")
        points[i] = float(z[0]), float(z[1])
    return points

def checkRepetitions(points):
    
    checked = []
    count = 0
    for i in range(le):
        p = points[i]
        flag1 = False
        flag2 = False
        if i in checked:
            continue
        for j in range(i+1, le):
            if i == j:
                continue
            q = points[j]
            if p == q:
                if flag2:
                    count += 1
                    flag1 = True
                else:
                    count += 2
                    print(f"{p}\t{i}", end=" ")
                print(j, end=" ")
                flag2 = True
                checked.append(j)
        if flag2:
            print()
            if flag1:
                print("flagged")

    print(f"count: {count}")


def findLowest(points):
    idx = []
    lowest = points[0]
    for p in points:
        if lowest[1] > p[1]:
            lowest = p
    for p in range(len(points)):
        if lowest[1] == points[p][1]:
            idx.append(points[p])
    return idx
points = makeList(name=bname)
dx = findLowest(points=points)
print(dx)