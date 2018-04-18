test_cases = int(input().strip())

while test_cases > 0:

    instruction = input().strip()

    if instruction[:10] == 'Simon says':
        print(instruction[11:])

    test_cases -= 1
