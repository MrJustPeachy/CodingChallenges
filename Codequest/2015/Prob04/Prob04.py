# Import file
filename = 'Prob04.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        temps = int(file.readline().strip())

        while temps > 0:

            temp = file.readline().strip().split()
            originalTempNum = temp[0]
            tempNum = float(temp[0])
            typeOfTemp = temp[1]

            if typeOfTemp == 'C':
                equation = round((((9/5) * tempNum) + 32), 2)
                print('{:s} C = {:.1f} F'.format(originalTempNum, equation))
            else:
                equation = round(((5/9) * (tempNum - 32)), 2)
                print('{:s} F = {:.1f} C'.format(originalTempNum, equation))

            temps -= 1

        test_cases -= 1