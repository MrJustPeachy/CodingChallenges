import sys

for line in sys.stdin:

    numbers = line.split()

    r1 = int(numbers[0])
    s = int(numbers[1])

    r2 = (2 * s) - r1

    print(r2)
