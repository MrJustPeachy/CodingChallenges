sowCost = float(input().strip())

lawns = float(input().strip())

data = []

total = 0

while lawns > 0:

    lawn = input().strip().split()
    data.append([float(lawn[0]), float(lawn[1])])

    lawns -= 1

for n in range(len(data)):
    cost = data[n][0] * data[n][1] * sowCost

    total += cost

print("{:.7f}".format(total))