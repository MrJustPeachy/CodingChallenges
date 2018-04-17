# Import file
filename = 'Prob02.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        string, index = file.readline().strip().split()

        newString = ''

        for i in range(len(string)):
            if i != int(index):
                newString += string[i]

        print(newString)

        test_cases -= 1