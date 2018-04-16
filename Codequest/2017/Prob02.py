# Import file
filename = 'Prob02.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        dollarAmount = file.readline().strip()[1:].split('.')

        dollars = int(dollarAmount[0])
        change = int(dollarAmount[1])

        quarters = 0
        dimes = 0
        nickles = 0
        pennies = 0

        quarters += int(dollars / .25)

        # print(change)

        while change > 0:
            quarters += change // 25
            change -= 25 * (change // 25)
            # print(change // 25)

            dimes += change // 10
            change -= 10 * (change // 10)

            nickles += change // 5
            change -= 5 * (change // 5)

            pennies += change // 1
            change -= 1 * (change // 1)

        print('$%d.%s' % (dollars, dollarAmount[1]))
        print('Quarters=%d' % quarters)
        print('Dimes=%d' % dimes)
        print('Nickles=%d' % nickles)
        print('Pennies=%d' % pennies)

        test_cases -= 1