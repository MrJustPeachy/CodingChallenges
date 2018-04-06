test_cases = int(input().strip())

while test_cases > 0:

    data = [int(n) for n in input().strip().split()]

    dataSet = data[0]
    N = data[1]

    s1 = 0
    s2 = 0
    s3 = 0

    for i in range(1, N + 1):
        s1 += i
        if i % 2 == 0:
            s3 += i
        else:
            s2 += i

    print('%d %d %d %d' % (dataSet, s1, s2, s3))

    test_cases -= 1