# Import file
filename = 'Prob05.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        country = file.readline().strip()

        gdpData = int(file.readline().strip())

        gdpList = []

        while gdpData > 0:

            data = file.readline().strip().split()
            gdpNum = float(data[0])
            year = int(data[1])

            gdpList.append([year, gdpNum])

            gdpData -= 1

        print('%s:' % country)

        gdpListSorted = sorted(gdpList, key=lambda x: x[0])

        for year, gdp in gdpListSorted:
            gdpRounded = int(round(gdp, -3) / 1000)

            print('%d %s' % (year, str((gdpRounded * '*'))))

        test_cases -= 1