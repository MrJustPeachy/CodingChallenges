test_cases = int(input().strip())

while test_cases > 0:

    dataSetNum, number = [n for n in input().strip().split()]

    octal = 0
    hex = int(number, 16)

    try:
        octal = int(number, 8)
    except ValueError:
        pass

    print('%d %d %d %d' % (int(dataSetNum), octal, int(number), hex))

    test_cases -= 1
