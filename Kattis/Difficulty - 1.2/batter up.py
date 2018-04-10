length = input().strip()

data = input().strip().split()

bases = 0
bats = 0

for n in range(int(length)):
    if int(data[n]) != -1:
        bases += int(data[n])
        bats += 1

result = bases / bats

print(result)