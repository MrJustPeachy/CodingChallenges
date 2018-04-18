data = [int(n) for n in input().strip().split()]

problems = data[0]
test_cases = data[1]

totalInput = test_cases

problemsSolved = 0

while problems > 0:

    test_cases = totalInput

    string = []

    while test_cases > 0:

        string.append(input().strip())

        test_cases -= 1

    fixedString = [[string[i][1:], string[i][1:].lower()] for i in range(len(string)) if string[i][1:] == string[i][1:].lower()]

    if len(fixedString) == totalInput:
        problemsSolved += 1

    problems -= 1

print(problemsSolved)
