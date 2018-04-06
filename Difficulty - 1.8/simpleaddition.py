import sys

numbers = []

for line in sys.stdin:

    if line == '\n':
        break

    number = int(line.strip())
    numbers.append(number)

print(sum(numbers))