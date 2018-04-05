data = [int(n) for n in input().strip().split()]

max = data[0]
events = data[1]

blocked = 0
residing = 0

while events > 0:

    event = input().strip().split()

    if event[0] == 'enter':
        if int(event[1]) + residing <= max:
            residing += int(event[1])
        else:
            blocked += 1
    else:
        residing -= int(event[1])

    events -= 1

print(blocked)