length = input().strip()

data = input().strip().split()

under_zero = 0

for n in range(int(length)):
    if int(data[n]) < 0:
        under_zero += 1

print(under_zero)