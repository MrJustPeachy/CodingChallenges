data = [int(n) for n in input().strip().split()]

problems = data[0]
test_cases = data[1]

totalInput = test_cases

while problems > 0:

    test_cases = totalInput

    string = []

    while test_cases > 0:

        string.append(input().strip())

        test_cases -= 1

    fixedString = []

    for s in string:
        modified = s.upper()

        fixedString.append()

    problems -= 1