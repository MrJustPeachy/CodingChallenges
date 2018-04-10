import sys
import math

def legResult(x, y):
    result = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    return result

for line in sys.stdin:

    if line.strip() == '0 0 0':
        break

    data = [int(n) for n in line.strip().split()]

    leg1 = data[0]
    leg2 = data[1]
    leg3 = data[2]

    if legResult(leg1, leg2) == leg3 or legResult(leg2, leg3) == leg1 or legResult(leg1, leg3) == leg2:
        print('right')
    else:
        print('wrong')