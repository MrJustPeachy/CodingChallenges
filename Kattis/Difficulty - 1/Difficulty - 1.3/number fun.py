import sys

test_cases = input().strip()

for line in sys.stdin:

    if line == '\n':
        break

    data = line.strip().split()

    first = int(data[0])
    second = int(data[1])
    third = int(data[2])

    if ((first - second) == third) or ((second - first) == third) or ((first + second) == third) or ((first / second) == third) or ((second / first) == third) or ((first * second) == third):
        print("Possible")
    else:
        print("Impossible")