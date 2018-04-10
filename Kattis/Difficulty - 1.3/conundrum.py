string = input().strip().lower()

changes = 0

for i in range(len(string)):

    if i % 3 == 0 and string[i] != 'p':
        changes += 1
    elif i % 3 == 1 and string[i] != 'e':
        changes += 1
    elif i % 3 == 2 and string[i] != 'r':
        changes += 1

print(changes)