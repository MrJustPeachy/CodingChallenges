test_cases = int(input().strip())

while test_cases > 0:

    data = input().strip()

    if data == 'P=NP':
        print('skipped')
    else:
        data = data.split('+')
        print(int(data[0]) + int(data[1]))

    test_cases -= 1