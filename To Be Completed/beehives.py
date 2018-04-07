import sys

for line in sys.stdin:
    data = [float(n) for n in line.strip().split()]

    distance = data[0]
    hives = int(data[1])

    hivePositions = []

    while hives > 0:

        if hives == 0:
            break

        hivePositions.append([n for n in line.strip().split()])

        hives -= 1

    print(hivePositions)