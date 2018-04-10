test_cases = int(input())

while test_cases > 0:

    number = int(input())

    if number % 2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")

    test_cases -= 1