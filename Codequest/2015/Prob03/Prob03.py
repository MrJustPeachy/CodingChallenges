# Import file
filename = 'Prob03.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        years = int(file.readline().strip())

        while years > 0:

            year = int(file.readline().strip())

            if year < 1582:
                print('No')
            elif year % 4 != 0:
                print('No')
            elif year % 100 != 0:
                print('Yes')
            elif year % 400 != 0:
                print('No')
            else:
                print('Yes')

            years -= 1

        test_cases -= 1