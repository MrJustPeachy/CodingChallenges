# Import file
filename = 'Prob05.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        total = float(file.readline().strip()[1:])

        fifteenPercent = round((total * .15), 2)
        eighteenPercent = round((total * .18), 2)
        twentyPercent = round((total * .20), 2)

        print('Total of the bill: ${:.2f}'.format(total))
        print('15% = {:.2f}'.format(fifteenPercent))
        print('18% = {:.2f}'.format(eighteenPercent))
        print('20% = {:.2f}'.format(twentyPercent))

        test_cases -= 1