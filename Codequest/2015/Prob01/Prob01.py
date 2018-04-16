# Import file
filename = 'Prob01.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        names = int(file.readline().strip())

        while names > 0:

            name = file.readline().strip().upper().split()
            print('%s%s%s' % (name[0][0], name[2][0], name[1][0]))

            names -= 1

        test_cases -= 1