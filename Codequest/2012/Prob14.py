import operator

# Import file
filename = 'Prob14.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    files = []

    while test_cases > 0:

        data = file.readline().strip().split(',')

        if data[1] == 'None':
            files.append([data[0]])
        else:
            files.append([data[1], data[0]])

        test_cases -= 1

    print(sorted())