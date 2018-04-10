import sys

numbers = []

for line in sys.stdin:

    if line == '\n':
        break

    number = int(line.strip())

    numbers.append(number)

N = 0

# Get N
for n in range(numbers[0], numbers[1] + 1):

    if sum(map(int, str(n))) == numbers[2]:
        N = n
        break

M = 0

# Get M
for n in reversed(range(numbers[0], numbers[1] + 1)):

    if sum(map(int, str(n))) == numbers[2]:
        M = n
        break

print(N)
print(M)