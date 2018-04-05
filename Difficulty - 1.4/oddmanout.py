from collections import Counter

test_cases = int(input().strip())

cases = 1

while test_cases > 0:

    guests = int(input().strip())

    ids = [int(n) for n in input().strip().split()]

    appearances = Counter(ids).most_common()

    print("Case #" + str(cases) + ': ' + str(appearances[-1][0]))

    cases += 1

    test_cases -= 1