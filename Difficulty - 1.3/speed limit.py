import sys

for line in sys.stdin:

    if line.strip() == '-1':
        break

    test_cases = int(line.strip())

    previous_mile = 0

    miles = 0

    while test_cases > 0:

        data = input().strip().split()

        miles_diff = int(data[1]) - previous_mile

        miles += (miles_diff * int(data[0]))

        previous_mile = int(data[1])

        test_cases -= 1

    print(str(miles) + " miles")