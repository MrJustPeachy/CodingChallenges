test_cases = int(input().strip())


def findScores(summed, abssed):
    if summed == abssed:
        return [summed, 0]

    for i in range(1, summed // 2):
        for j in reversed(range(summed // 2 + 1, summed)):
            if i != j and i + j == summed and abs(i - j) == abssed:
                return [i, j]


while test_cases > 0:

    sumScore, absScore = [int(n) for n in input().strip().split()]

    scores = findScores(sumScore, absScore)

    if scores is not None:
        print('%d %d' % (max(scores), min(scores)))
    else:
        print('impossible')

    test_cases -= 1
