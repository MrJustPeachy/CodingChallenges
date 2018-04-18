import sys

numbers = []
total = 0

for line in sys.stdin:

    if line == '\n':
        break

    number = line.strip()

    numbers.append(number)

for n in range(int(numbers[0])):

    num = int(numbers[n + 1][:-1])
    power = int(numbers[n + 1][-1])

    total += (num ** power)

print(total)