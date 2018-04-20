# Import file
filename = 'Prob12.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        data = int(file.readline().strip())

        days = data

        purchases = 0.0
        dailyBalances = []

        while data > 0:

            day, purchase, payments = file.readline().strip().split(',')

            if len(purchase) == 0:
                purchase = 0.0

            if len(payments) == 0:
                payments = 0.0

            purchases += float(purchase)
            purchases -= float(payments)

            dailyBalances.append(purchases)

            data -= 1

        monthlyInterest = round(((sum(dailyBalances) / days) * (0.18 / 12)), 2)

        print('${:.2f}'.format(monthlyInterest))

        test_cases -= 1