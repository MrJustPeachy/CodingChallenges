import math
import sys
from operator import itemgetter
from itertools import filterfalse

for line in sys.stdin:

    if line == '\n':
        break

    test_cases = int(line.strip())

    airportLocations = []

    while test_cases > 0:

        airportLocations.append([float(n) for n in input().strip().split()])

        test_cases -= 1

    for i in range(len(airportLocations)):
        distances = []
        for j in range(len(airportLocations)):
            if i != j:
                latDistance = math.pow((airportLocations[j][0] - airportLocations[i][0]), 2)
                longDistance = math.pow((airportLocations[j][1] - airportLocations[i][1]), 2)

                distances.append(math.sqrt(latDistance + longDistance))

        airportLocations[i].append(sum(distances) / len(distances))

    sortedLocations = sorted(airportLocations, key=itemgetter(2))

    latestLocal = []

    for x in list(filterfalse(lambda x: x[:][2] != sortedLocations[0][2], sortedLocations))[-1]:
        latestLocal.append(x)

    print('{:.2f} {:.2f}'.format(latestLocal[0], latestLocal[1]))
