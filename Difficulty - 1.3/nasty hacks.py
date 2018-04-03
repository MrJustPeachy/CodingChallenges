import sys

test_cases = input().strip()

for line in sys.stdin:

    if line == '\n':
        break

    data = line.strip().split()

    noAdRevenue = int(data[0])
    adRevenue = int(data[1])
    advertisingCost = int(data[2])

    if (adRevenue - advertisingCost) > noAdRevenue:
        print("advertise")
    elif (adRevenue - advertisingCost) == noAdRevenue:
        print("does not matter")
    elif (adRevenue - advertisingCost) < noAdRevenue:
        print("do not advertise")