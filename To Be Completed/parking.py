import math

test_cases = int(input().strip())

while test_cases > 0:

    stores = int(input().strip())
    storePositions = [int(n) for n in input().strip().split()]

    storeDistances = []

    for i in range(1, 101):

        storesCalculations = []

        for store in storePositions:
            distance = math.sqrt((store - i) ** 2)
            storesCalculations.append(int(distance))

        storeDistances.append(sum(storesCalculations))

    test_cases -= 1

    print(storeDistances)