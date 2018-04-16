# Import file
filename = 'Prob02.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        sands = int(file.readline().strip())

        sand = []

        while sands > 0:

            sandInput = int(file.readline().strip())
            sand.append(sandInput)

            sands -= 1

        print(sum(sand))

        test_cases -= 1