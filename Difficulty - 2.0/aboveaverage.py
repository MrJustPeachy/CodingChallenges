test_cases = int(input().strip())

while test_cases > 0:

    data = [int(n) for n in input().strip().split()]

    numbers = data[0]
    data.pop(0)

    average = sum(data) / len(data)

    aboveAverage = [n for n in data if float(n) > average]

    print('{:.3f}%'.format(round(((len(aboveAverage) / len(data)) * 100), 3)))

    test_cases -= 1