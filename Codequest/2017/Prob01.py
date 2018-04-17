# Import file
filename = 'Prob01.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        string = file.readline().strip()
        print(string)
        print(string)

        test_cases -= 1