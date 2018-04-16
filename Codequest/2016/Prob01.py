# Import file
filename = 'Prob01.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        number = int(file.readline().strip())

        for n in range(number):
            print('*' * number)

        test_cases -= 1