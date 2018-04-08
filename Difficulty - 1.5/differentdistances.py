import math
import sys

for line in sys.stdin:

    if line.strip() == '0':
        break

    data = [float(n) for n in line.strip().split()]

    x1 = data[0]
    x2 = data[2]
    y1 = data[1]
    y2 = data[3]
    p = data[4]

    xDistances = math.pow(abs(x1 - x2), p)
    yDistances = math.pow(abs(y1 - y2), p)

    pNormDistances = math.pow((xDistances + yDistances), (1 / p))

    print('{:.6f}'.format(pNormDistances))