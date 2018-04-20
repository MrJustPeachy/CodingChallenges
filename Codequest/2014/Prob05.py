# Import file
filename = 'Prob05.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        lastYearList = file.readline().strip().split(',')
        currentYearList = file.readline().strip().split(',')

        lastYearOnly = []
        currentYearOnly = []
        bothYears = []

        for name in lastYearList:
            if name in currentYearList:
                bothYears.append(name)
            else:
                lastYearOnly.append(name)

        for name in currentYearList:
            if name not in bothYears:
                currentYearOnly.append(name)

        print(','.join(lastYearOnly))
        print(','.join(bothYears))
        print(','.join(currentYearOnly))

        test_cases -= 1