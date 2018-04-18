test_cases = int(input().strip())

while test_cases > 0:

    message = input().strip()

    if message[:10] == 'simon says':
        print(message[11:])
    else:
        print()

    test_cases -= 1