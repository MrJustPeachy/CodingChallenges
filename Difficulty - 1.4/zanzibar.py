test_cases = int(input().strip())

while test_cases > 0:

    data = [int(n) for n in input().strip().split()]

    foreigners = 0

    for year in range(len(data)):
        if year > 0:
            if data[year] != 0:
                previousPopulation = data[year - 1]
                newResidents = previousPopulation * 2

                if data[year] - newResidents > 0:
                    difference = data[year] - newResidents
                    foreigners += difference

    print(foreigners)

    test_cases -= 1
