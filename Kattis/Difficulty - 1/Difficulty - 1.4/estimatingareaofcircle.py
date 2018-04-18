import math
import sys

for line in sys.stdin:

    if line == '\n':
        break

    if line.strip() == '0 0 0':
        break

    data = [float(n) for n in line.strip().split()]

    radius = data[0]
    points = data[1]
    accuratePoints = data[2]

    realArea = math.pi * math.pow(radius, 2)

    squareArea = math.pow((radius * 2), 2)

    estimatedArea = squareArea * float(accuratePoints / points)

    print('{:.6f} {:.6f}'.format(realArea, estimatedArea))