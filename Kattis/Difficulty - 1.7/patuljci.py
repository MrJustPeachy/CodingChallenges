import sys

numbers = []

for line in sys.stdin:

    if line == '\n':
        break

    numbers.append(int(line.strip()))

sum100 = []

for i in range(len(numbers)):
    noI = list(numbers)
    noI.pop(i)
    for j in range(len(noI)):
        if i != j:
            noJ = list(noI)
            noJ.pop(j)
            if sum(noJ) == 100:
                sum100.append(noJ)

for num in sum100[0]:
    print(num)