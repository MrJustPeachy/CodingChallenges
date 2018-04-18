import sys
import math

for line in sys.stdin:

    if line.strip() == '0.0 0':
        break

    data = [float(n) for n in line.strip().split()]

    distance = data[0]
    hives = int(data[1])

    hivePositions = []

    while hives > 0:

        if hives == 0:
            break

        hivePositions.append([float(n) for n in input().strip().split()])

        hives -= 1

    for i in range(len(hivePositions)):
        for j in range(len(hivePositions)):
            if i != j:
                firstHive = hivePositions[i]
                secondHive = hivePositions[j]
                distanceBetweenHives = math.sqrt(math.pow((firstHive[0] - secondHive[0]), 2) + math.pow((firstHive[1] - secondHive[1]), 2))
                if distanceBetweenHives <= distance:
                    firstHive.append(1)
                    secondHive.append(1)

    sourCount = 0
    sweetCount = 0

    for hive in hivePositions:
        if len(hive) > 2:
            sourCount += 1
        else:
            sweetCount += 1

    print('%d sour, %d sweet' % (sourCount, sweetCount))
