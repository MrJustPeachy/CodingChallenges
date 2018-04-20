# Import file
filename = 'Prob07.in.txt'

for line in open(filename):

    amountOwed, amountGiven = [float(n) for n in line.strip().split(', ')]

    amountNeeded = amountGiven - amountOwed

    moneyGiven = []

    amountNeeded = round(amountNeeded, 2)

    if amountNeeded >= 1:
        if amountNeeded // 20 >= 1:
            moneyGiven.append(['TWENTY', int(amountNeeded // 20)])
            amountNeeded -= int(20 * int(amountNeeded // 20))

        if amountNeeded // 10 >= 1:
            moneyGiven.append(['TEN', int(amountNeeded // 10)])
            amountNeeded -= int(10 * int(amountNeeded // 10))

        if amountNeeded // 5 >= 1:
            moneyGiven.append(['FIVE', int(amountNeeded // 5)])
            amountNeeded -= int(5 * int(amountNeeded // 5))

        if amountNeeded // 1 >= 1:
            moneyGiven.append(['ONE', int(amountNeeded // 1)])
            amountNeeded -= int(1 * int(amountNeeded // 1))

    print(amountNeeded)

    if amountNeeded < 1:
        if amountNeeded // .25 >= 1:
            moneyGiven.append(['QUARTER', int(amountNeeded // .25)])
            amountNeeded -= .25 * int(amountNeeded // .25)

        if amountNeeded // .10 >= 1:
            moneyGiven.append(['DIME', int(amountNeeded // .10)])
            amountNeeded -= .10 * int(amountNeeded // .10)

        if amountNeeded // .05 >= 1:
            moneyGiven.append(['NICKEL', int(amountNeeded // .05)])
            amountNeeded -= .05 * int(amountNeeded // .05)

        print(amountNeeded)
        if amountNeeded // .01 >= 1:
            moneyGiven.append(['PENNY', int(amountNeeded // .01)])
            amountNeeded -= .01 * int(amountNeeded // .01)

    print(moneyGiven)
