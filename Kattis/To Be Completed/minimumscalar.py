test_cases = int(input().strip())

caseID = 1

while test_cases > 0:

    matrixLength = int(input().strip())

    list1 = sorted([int(n) for n in input().strip().split()])
    list2 = sorted([int(n) for n in input().strip().split()])

    scalar1 = []
    list1Reversed = list1[::-1]

    for i in range(len(list1)):
        scalar1.append(list1Reversed[i] * list2[i])

    print('Case #1: %d' % sum(scalar1))

    test_cases -= 1