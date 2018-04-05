test_cases = int(input().strip())

while test_cases > 0:

    firstString = input().strip()
    secondString = input().strip()

    print(firstString)
    print(secondString)

    errors = ''

    for i in range(len(firstString)):
        if firstString[i] != secondString[i]:
            errors += '*'
        else:
            errors += '.'

    print(errors)

    test_cases -= 1