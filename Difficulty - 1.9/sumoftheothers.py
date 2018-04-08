import sys

for line in sys.stdin:

    if line == '\n':
        break

    data = [int(n) for n in line.strip().split()]

    for i in range(len(data)):

        otherNums = []

        for j in range(len(data)):

            if i != j:
                otherNums.append(data[j])

        if sum(otherNums) == data[i]:
            print(data[i])
            break