test_cases = int(input().strip())

while test_cases > 0:

    data = [int(n) for n in input().strip().split()]

    dataSet = data[0]
    N = data[1]

    s1 = (N * (N + 1)) / 2
    s2 = N ** 2
    s3 = N * (N + 1)

    print('%d %d %d %d' % (dataSet, s1, s2, s3))

    test_cases -= 1
